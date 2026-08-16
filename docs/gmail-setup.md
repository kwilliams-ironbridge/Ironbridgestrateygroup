# Gmail API Setup Guide

This guide walks you through setting up Google OAuth 2.0 authentication for Jarvis to monitor multiple Gmail accounts.

## Prerequisites

- Google Account(s) for each email you want to monitor
- Access to Google Cloud Console (https://console.cloud.google.com)

## Step 1: Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Click **Select a Project** → **New Project**
3. Name it: `Jarvis Chief of Staff`
4. Click **Create**

## Step 2: Enable Gmail API

1. In the Cloud Console, go to **APIs & Services** → **Library**
2. Search for "Gmail API"
3. Click on **Gmail API**
4. Click **Enable**

## Step 3: Create OAuth 2.0 Credentials

### For Desktop/Local Application:

1. Go to **APIs & Services** → **Credentials**
2. Click **+ Create Credentials** → **OAuth client ID**
3. If prompted, configure the OAuth consent screen first:
   - Select **External** user type
   - Fill in required fields (app name, support email, etc.)
   - Add scopes: `gmail.readonly`, `gmail.labels`
   - Add test users (your email addresses)
4. After consent screen, create credentials:
   - Application type: **Desktop application**
   - Name: `Jarvis Email Monitor`
   - Click **Create**
5. Click the download icon to download as JSON
6. Save as `google-oauth-credentials.json` (do NOT commit to git)

### For Web Application:

If hosting Jarvis on a server:

1. Application type: **Web application**
2. Authorized JavaScript origins: `https://yourdomain.com`
3. Authorized redirect URIs: `https://yourdomain.com/auth/callback`

## Step 4: Store Credentials Securely

**IMPORTANT: Never commit credentials to git**

1. Create `.gitignore` entries:
   ```
   credentials/*
   !credentials/.gitkeep
   email/gmail-credentials.json
   .env.local
   ```

2. Store credentials in secure location:
   ```bash
   cp google-oauth-credentials.json credentials/google-oauth.json
   chmod 600 credentials/google-oauth.json
   ```

3. For each email account, you'll need to:
   - Authorize the app (visit the OAuth URL)
   - Store the refresh token securely
   - Update the profile in `profiles/users.json`

## Step 5: Authenticate Each Email Account

For each email you want to monitor, run:

```bash
python jarvis/authenticate-gmail.py --email your-email@gmail.com
```

This will:
1. Open a browser for OAuth authorization
2. Request permission to access Gmail
3. Store the refresh token securely
4. Update your profile configuration

## Step 6: Test Connection

```bash
python jarvis/test-gmail-connection.py --user-id your-user-id
```

Expected output:
```
✓ Connected to kenyatta@ironbridgestrategy.com
✓ Connected to kenyatta.williams@columbia.edu
✓ Connected to kenyattawilliams1121@gmail.com
✓ 3/3 accounts ready for monitoring
```

## Troubleshooting

### "invalid_grant" Error
- Refresh token has expired
- Re-authenticate the account
- Check that credentials weren't rotated elsewhere

### "Not authorized to access this resource"
- Scopes are insufficient
- Re-create credentials with both `gmail.readonly` and `gmail.labels`
- Add user to OAuth consent screen test users

### Token Refresh Failing
- Check that refresh token is stored correctly
- Verify credentials file is readable
- Ensure system clock is in sync

## Security Best Practices

- ✓ Use refresh tokens, not access tokens in long-term storage
- ✓ Rotate credentials annually
- ✓ Keep `.env` and credential files local only
- ✓ Use restrictive file permissions (chmod 600)
- ✓ Monitor API quota usage in Cloud Console
- ✓ Set up billing alerts

## Gmail API Quotas

- Daily quota: 1,000,000,000 units per day
- Per-user rate limit: 250 requests per second
- For typical email monitoring: ~1-5 quota units per message read

## Revoking Access

To revoke Jarvis access to an email account:

1. Go to [myaccount.google.com/permissions](https://myaccount.google.com/permissions)
2. Find "Jarvis Chief of Staff"
3. Click remove access
4. Delete the credentials from storage

---

**Next Step:** Once authenticated, update `profiles/users.json` with your email accounts and configure `jarvis/config.json` to customize monitoring behavior.
