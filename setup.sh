#!/bin/bash

# Jarvis Setup Script
# Installs dependencies and guides you through authentication

echo "========================================"
echo "Jarvis Chief of Staff - Setup"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or later."
    exit 1
fi

echo "✓ Python $(python3 --version) found"
echo ""

# Create virtual environment (optional but recommended)
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment exists"
    source venv/bin/activate
fi

echo ""
echo "Installing dependencies..."
pip install -q google-auth-oauthlib google-auth-httplib2 google-api-python-client
echo "✓ Google libraries installed"

echo ""
echo "========================================"
echo "Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo ""
echo "1. Download Google OAuth credentials:"
echo "   - Go to https://console.cloud.google.com"
echo "   - Create project 'Jarvis Chief of Staff'"
echo "   - Enable Gmail API"
echo "   - Create Desktop OAuth credentials"
echo "   - Download as JSON → credentials/google-oauth.json"
echo ""
echo "2. Authenticate your emails:"
echo "   python jarvis/authenticate-gmail.py --email kenyatta@ironbridgestrategy.com"
echo "   python jarvis/authenticate-gmail.py --email ksw@notavault.net"
echo "   python jarvis/authenticate-gmail.py --email wobblethecloud@sunniestsprouts.com"
echo "   python jarvis/authenticate-gmail.py --email shamon1121@gmail.com"
echo "   python jarvis/authenticate-gmail.py --email kw@notavaultllc.com"
echo ""
echo "3. Update profiles/users.json with your authenticated emails"
echo ""
