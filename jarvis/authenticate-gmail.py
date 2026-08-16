#!/usr/bin/env python3
"""
Gmail OAuth 2.0 Authentication Script for Jarvis

Authenticates a single Gmail account and stores the refresh token securely.
Run this for each email account you want Jarvis to monitor.

Usage:
    python authenticate-gmail.py --email your-email@gmail.com
    python authenticate-gmail.py --email another@gmail.com --no-browser
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
import webbrowser

try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.exceptions import RefreshError
except ImportError:
    print("Error: Required Google libraries not installed.")
    print("Install with: pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)

# Gmail API scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.labels']

# Paths
REPO_ROOT = Path(__file__).parent.parent
CREDENTIALS_DIR = REPO_ROOT / 'credentials'
OAUTH_CREDS_FILE = CREDENTIALS_DIR / 'google-oauth.json'
TOKENS_DIR = CREDENTIALS_DIR / 'tokens'
PROFILES_FILE = REPO_ROOT / 'profiles' / 'users.json'


def setup_directories():
    """Create necessary directories if they don't exist."""
    CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)
    TOKENS_DIR.mkdir(parents=True, exist_ok=True)


def get_oauth_credentials():
    """Load OAuth credentials from google-oauth.json."""
    if not OAUTH_CREDS_FILE.exists():
        print(f"\n❌ ERROR: OAuth credentials file not found!")
        print(f"Expected location: {OAUTH_CREDS_FILE}")
        print("\nTo get credentials:")
        print("1. Go to https://console.cloud.google.com")
        print("2. Create a new project")
        print("3. Enable Gmail API")
        print("4. Create Desktop OAuth credentials")
        print("5. Download as JSON and save to: credentials/google-oauth.json")
        sys.exit(1)

    return OAUTH_CREDS_FILE


def authenticate_email(email: str, no_browser: bool = False):
    """
    Authenticate a Gmail account and save the refresh token.

    Args:
        email: Email address to authenticate
        no_browser: If True, print URL instead of opening browser
    """
    print(f"\n{'='*60}")
    print(f"Authenticating: {email}")
    print(f"{'='*60}")

    oauth_creds_file = get_oauth_credentials()
    token_file = TOKENS_DIR / f"{email.replace('@', '_at_')}.json"

    try:
        # Create OAuth flow
        flow = InstalledAppFlow.from_client_secrets_file(
            oauth_creds_file,
            SCOPES
        )

        # Get authorization
        if no_browser:
            # Terminal-based auth
            print("\nOpen this URL in your browser and authorize the app:")
            print(flow.authorization_url()[0])
            print("\nPaste the authorization code here:")
            auth_code = input().strip()
            flow.fetch_token(code=auth_code)
        else:
            # Browser-based auth
            print("\n✓ Opening browser for authentication...")
            print("(If browser doesn't open, copy the URL from the terminal)")
            credentials = flow.run_local_server(port=0)

        # Get credentials
        if not no_browser:
            credentials = flow.credentials
        else:
            credentials = flow.credentials

        # Save token
        token_data = {
            "email": email,
            "token": credentials.token,
            "refresh_token": credentials.refresh_token,
            "token_uri": credentials.token_uri,
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
            "scopes": credentials.scopes,
            "authenticated_at": datetime.utcnow().isoformat()
        }

        with open(token_file, 'w') as f:
            json.dump(token_data, f, indent=2)

        os.chmod(token_file, 0o600)  # Restrict permissions

        print(f"\n✅ Successfully authenticated: {email}")
        print(f"✓ Token saved to: {token_file}")

        # Update profile
        update_profile_with_token(email, credentials.refresh_token)

        return True

    except Exception as e:
        print(f"\n❌ Authentication failed for {email}")
        print(f"Error: {str(e)}")
        return False


def update_profile_with_token(email: str, refresh_token: str):
    """Update the user profile with the authenticated email and refresh token."""
    try:
        # Load or create profile
        if PROFILES_FILE.exists():
            with open(PROFILES_FILE, 'r') as f:
                data = json.load(f)
        else:
            data = {"users": []}

        # For now, just update the first user (you can extend this)
        if data.get("users"):
            user = data["users"][0]

            # Check if email already exists
            email_exists = False
            for email_config in user.get("emails", []):
                if email_config["emailAddress"] == email:
                    email_config["credentials"]["refreshToken"] = refresh_token
                    email_config["credentials"]["tokenExpiryTime"] = (
                        datetime.utcnow().isoformat() + "Z"
                    )
                    email_exists = True
                    break

            # If email doesn't exist in profile yet, notify user to add it manually
            if not email_exists:
                print(f"\n⚠️  Note: Add this email to profiles/users.json:")
                print(f"   - emailAddress: {email}")
                print(f"   - refreshToken: {refresh_token}")

    except Exception as e:
        print(f"\n⚠️  Could not auto-update profile: {str(e)}")
        print(f"Please manually add to profiles/users.json:")
        print(f"   - emailAddress: {email}")
        print(f"   - refreshToken: {refresh_token}")


def test_connection(email: str):
    """Test that the authenticated email can connect to Gmail."""
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials

        token_file = TOKENS_DIR / f"{email.replace('@', '_at_')}.json"

        if not token_file.exists():
            print(f"❌ No token found for {email}")
            return False

        with open(token_file, 'r') as f:
            token_data = json.load(f)

        # Create credentials from token
        credentials = Credentials(
            token=token_data['token'],
            refresh_token=token_data['refresh_token'],
            token_uri=token_data['token_uri'],
            client_id=token_data['client_id'],
            client_secret=token_data['client_secret']
        )

        # Refresh token
        request = Request()
        credentials.refresh(request)

        print(f"✅ Connection successful for {email}")
        return True

    except Exception as e:
        print(f"❌ Connection failed for {email}: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Authenticate Gmail account for Jarvis monitoring',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python authenticate-gmail.py --email user@gmail.com
  python authenticate-gmail.py --email user@gmail.com --no-browser
  python authenticate-gmail.py --email user@gmail.com --test
        """
    )

    parser.add_argument('--email', required=True, help='Email address to authenticate')
    parser.add_argument('--no-browser', action='store_true',
                       help='Use terminal-based auth instead of browser')
    parser.add_argument('--test', action='store_true',
                       help='Test connection to already-authenticated email')

    args = parser.parse_args()

    # Setup
    setup_directories()

    # Test mode
    if args.test:
        print("\nTesting connection...")
        success = test_connection(args.email)
        sys.exit(0 if success else 1)

    # Authenticate
    success = authenticate_email(args.email, args.no_browser)

    if success:
        print("\n" + "="*60)
        print("NEXT STEPS:")
        print("="*60)
        print(f"1. Update profiles/users.json with refresh token for {args.email}")
        print(f"2. Add to 'emails' array with monitoringRules")
        print(f"3. Run: python authenticate-gmail.py --email {args.email} --test")
        print(f"4. Repeat for each email account you want to monitor\n")

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
