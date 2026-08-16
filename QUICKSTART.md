# Jarvis Quick Start Guide

Get Jarvis monitoring your emails in 15 minutes.

## Step 1: Install Dependencies (2 min)

Open your terminal and navigate to the project:

```bash
cd /path/to/Ironbridgestrateygroup
```

Run the setup script:

```bash
bash setup.sh
```

This will:
- Check Python installation
- Create a virtual environment
- Install Google libraries

## Step 2: Get Google OAuth Credentials (5 min)

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. **Create a new project**:
   - Click "Select a Project" → "New Project"
   - Name: `Jarvis Chief of Staff`
   - Click "Create"

3. **Enable Gmail API**:
   - Go to "APIs & Services" → "Library"
   - Search "Gmail API"
   - Click → "Enable"

4. **Create OAuth credentials**:
   - Go to "APIs & Services" → "Credentials"
   - Click "+ Create Credentials" → "OAuth client ID"
   - If prompted, configure OAuth consent screen:
     - Select "External"
     - Fill in app name: `Jarvis`
     - Add your email as a test user
     - Skip optional fields
     - Save & Continue
   - Back to credentials:
     - Application type: **Desktop application**
     - Name: `Jarvis Email Monitor`
     - Click "Create"

5. **Download & Save**:
   - Click the download icon (↓)
   - Save as: `credentials/google-oauth.json`
   - ✓ Keep this file private (don't commit to git)

## Step 3: Authenticate Your Emails (8 min)

Activate the virtual environment first:

```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

Run authentication for each email:

```bash
python jarvis/authenticate-gmail.py --email kenyatta@ironbridgestrategy.com
python jarvis/authenticate-gmail.py --email ksw@notavault.net
python jarvis/authenticate-gmail.py --email wobblethecloud@sunniestsprouts.com
python jarvis/authenticate-gmail.py --email shamon1121@gmail.com
python jarvis/authenticate-gmail.py --email kw@notavaultllc.com
```

**What happens:**
1. Browser opens → Google login page
2. You authorize Jarvis to access Gmail
3. Script saves your refresh token securely
4. Repeat for each email

**Troubleshooting:**
- Browser won't open? Use `--no-browser` flag:
  ```bash
  python jarvis/authenticate-gmail.py --email user@gmail.com --no-browser
  ```
- Copy the URL, paste in browser, then paste auth code back in terminal

## Step 4: Update Your Profile (optional but recommended)

Copy the example profile:

```bash
cp profiles/users.example.json profiles/users.json
```

Edit `profiles/users.json`:
- Update your emails
- Add VIP senders (key stakeholders)
- Add keywords that matter to you
- Set Obsidian vault path if using

Example:
```json
{
  "emailAddress": "kenyatta@ironbridgestrategy.com",
  "monitoringRules": {
    "prioritySenders": [
      "board@example.com",
      "investors@example.com"
    ],
    "keywords": ["urgent", "decision needed", "deadline"]
  }
}
```

## Step 5: Test Connections

Verify all emails are connected:

```bash
python jarvis/authenticate-gmail.py --email kenyatta@ironbridgestrategy.com --test
python jarvis/authenticate-gmail.py --email ksw@notavault.net --test
# ... etc for each email
```

Expected output:
```
✅ Connection successful for kenyatta@ironbridgestrategy.com
✅ Connection successful for ksw@notavault.net
✅ Connection successful for wobblethecloud@sunniestsprouts.com
✅ Connection successful for shamon1121@gmail.com
✅ Connection successful for kw@notavaultllc.com
```

## 🎉 You're Done!

Jarvis is now ready to:
- ✓ Monitor 5 email accounts
- ✓ Prioritize important messages
- ✓ Send daily digest
- ✓ Alert on urgent emails
- ✓ Integrate with Claude

## What's Next?

### Start Using Jarvis

In Claude chat, ask:
```
"Jarvis, give me my email digest for today"
"Check my VIP emails"
"Who's been trying to reach me?"
```

### Configure Advanced Features

Edit `jarvis/config.json`:
```json
{
  "notifications": {
    "dailyDigestTime": "06:00",    // When to send digest
    "channels": ["obsidian", "slack"]  // Where to send
  },
  "prioritization": {
    "vipSenders": { "weight": 10 },
    "keywords": {
      "urgent": { "weight": 8 },
      "decision": { "weight": 7 }
    }
  }
}
```

### Connect to Obsidian

Set in `profiles/users.json`:
```json
{
  "integrations": {
    "obsidianVault": "/path/to/your/Obsidian/Ironbridge"
  }
}
```

Jarvis will automatically create daily summaries there.

## Files Reference

| File | Purpose |
|------|---------|
| `credentials/google-oauth.json` | Your Google API credentials (GITIGNORED) |
| `credentials/tokens/` | Email authentication tokens (GITIGNORED) |
| `profiles/users.json` | Your profile and email configuration (GITIGNORED) |
| `jarvis/config.json` | Jarvis behavior settings |
| `jarvis/authenticate-gmail.py` | Authentication script |

## Security Reminders

✓ Never share `credentials/google-oauth.json`
✓ Never commit `credentials/tokens/*` to git
✓ `.gitignore` prevents accidental leaks
✓ Tokens refresh automatically
✓ You can revoke access anytime in Google Account settings

## Help & Troubleshooting

**Authentication failing?**
- Verify OAuth credentials are in `credentials/google-oauth.json`
- Check that Gmail API is enabled
- Try authenticating again

**Email not appearing in digest?**
- Check `monitoringRules.excludeLabels` in profile
- Verify sender isn't filtered by keywords
- Test connection: `python jarvis/authenticate-gmail.py --email user@gmail.com --test`

**Token expired?**
- Just re-run the authentication command
- Script will refresh the token automatically

See [docs/gmail-setup.md](docs/gmail-setup.md) for detailed setup guide.
See [docs/jarvis-workflow.md](docs/jarvis-workflow.md) for how Jarvis works.

---

Ready to go? Run:
```bash
bash setup.sh
```

Then authenticate your emails above! 🚀
