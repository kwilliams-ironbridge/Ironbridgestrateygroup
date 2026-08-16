# Ironbridge Strategy Group - Jarvis Chief of Staff System

Professional AI-powered chief of staff for managing communications across multiple email accounts, powered by Claude and integrated with Obsidian and Google services.

## Quick Start

1. **Set up Gmail API** → See [docs/gmail-setup.md](docs/gmail-setup.md)
2. **Create your profile** → Copy `profiles/users.example.json` to `profiles/users.json`
3. **Configure Jarvis** → Customize `jarvis/config.json` for your workflow
4. **Start monitoring** → Jarvis begins email sync and daily digest

## Directory Structure

```
.
├── CLAUDE.md                           # Project documentation
├── README.md                           # This file
├── ironbridge_landing_page.html        # Company landing page
│
├── profiles/                           # User profile management
│   ├── schema.json                     # Profile data structure definition
│   ├── users.example.json              # Example user configuration
│   └── users.json                      # GITIGNORED - Your profiles
│
├── jarvis/                             # Jarvis chief of staff system
│   ├── config.json                     # Jarvis behavior configuration
│   ├── email-monitoring.py             # Email sync & processing (future)
│   ├── authenticate-gmail.py           # OAuth setup script (future)
│   └── test-gmail-connection.py        # Connection tester (future)
│
├── email/                              # Email integration
│   ├── gmail-config.json               # Gmail API settings (GITIGNORED)
│   └── gmail-credentials.json          # OAuth tokens (GITIGNORED)
│
├── credentials/                        # Secure credential storage
│   └── .gitkeep
│
├── cache/                              # Local message cache
│   └── .gitkeep
│
├── logs/                               # Jarvis activity logs
│   └── .gitkeep
│
└── docs/                               # Documentation
    ├── gmail-setup.md                  # Gmail API setup guide
    ├── jarvis-workflow.md              # Chief of staff workflow
    └── SECURITY.md                     # Security best practices (future)
```

## Features

✓ **Multi-Account Monitoring** - Track multiple email addresses simultaneously
✓ **Smart Prioritization** - AI-powered scoring of message importance
✓ **Daily Digest** - Consolidated summary delivered each morning
✓ **Real-time Alerts** - Instant notification for high-priority messages
✓ **VIP Tracking** - Automatic flagging of messages from key stakeholders
✓ **Obsidian Integration** - Store summaries and action items in your vault
✓ **Claude Integration** - Use Claude chat to query and manage emails
✓ **Secure OAuth** - Google OAuth 2.0 for safe credential management

## Configuration Files

### `profiles/users.json`
Stores user profiles with email accounts, monitoring rules, and preferences.

**Key fields:**
- `emails[]` - Array of email accounts to monitor
- `monitoringRules` - VIP senders, keywords, excluded labels
- `jarvisSettings` - Digest frequency, summarization level
- `integrations` - Obsidian vault path, Slack channel

### `jarvis/config.json`
Configures Jarvis behavior, capabilities, and notification system.

**Key settings:**
- `emailMonitoring.syncInterval` - How often to check emails (default: 5m)
- `notifications.dailyDigestTime` - When to send digest (default: 6:00 AM)
- `prioritization` - Scoring weights for VIP, keywords, domains
- `logging.level` - Log verbosity (info, debug, error)

## Setup Steps

### 1. Prerequisites
- Python 3.8+ (for email monitoring scripts - coming soon)
- Google Cloud account
- Obsidian vault (optional)

### 2. Clone & Configure
```bash
git clone <repo-url>
cd Ironbridgestrateygroup
cp profiles/users.example.json profiles/users.json
```

### 3. Gmail API Setup
Follow [docs/gmail-setup.md](docs/gmail-setup.md) to:
- Create Google Cloud project
- Enable Gmail API
- Generate OAuth credentials
- Authenticate each email account

### 4. Customize Configuration
Edit `profiles/users.json`:
- Add your email addresses
- Set VIP senders
- Define keywords
- Configure integrations

### 5. Start Jarvis
```bash
python jarvis/email-monitoring.py
```

## Usage

### Command Line
```bash
# Test all email connections
python jarvis/test-gmail-connection.py --user-id kenyatta-williams-001

# Generate current digest
python jarvis/generate-digest.py --user-id kenyatta-williams-001

# Authenticate new email account
python jarvis/authenticate-gmail.py --email your-email@gmail.com
```

### In Claude Chat
```
"Jarvis, what's on my plate today?"
"Check my VIP emails from this week."
"Summarize the conversation with [sender@example.com]"
"Create a task for everything marked urgent."
```

### In Obsidian
Daily digests automatically sync to:
```
Inbox/Jarvis Daily Digest/2026-08-16.md
```

## Security & Privacy

- ✓ Credentials stored locally, never in git
- ✓ OAuth tokens use refresh tokens, not passwords
- ✓ All data encrypted in transit (HTTPS/TLS)
- ✓ No email content logged to disk (metadata only)
- ✓ Automatic credential refresh every 50 minutes
- ✓ File permissions restricted (chmod 600)

**Never commit:**
- `profiles/users.json` (has credentials)
- `credentials/` directory
- `email/gmail-credentials.json`
- `.env.local` files

See [SECURITY.md](docs/SECURITY.md) for detailed security practices.

## Troubleshooting

**Emails not appearing?**
- Check `monitoringRules.excludeLabels` in profile
- Verify sender isn't filtered by keywords
- Ensure monitoring is enabled for account

**Too many notifications?**
- Increase `priorityThreshold` to "high"
- Refine VIP senders list
- Adjust keyword scoring

**Connection failing?**
- Re-authenticate with `authenticate-gmail.py`
- Check OAuth consent screen test users
- Verify API is enabled in Google Cloud Console

See [docs/jarvis-workflow.md](docs/jarvis-workflow.md) for detailed workflow and troubleshooting.

## Roadmap

- [ ] Email monitoring daemon (background service)
- [ ] Auto-responder for common requests
- [ ] Slack integration for alerts
- [ ] Meeting scheduling assistant
- [ ] Email draft suggestions
- [ ] Sentiment analysis
- [ ] Competitor tracking from emails
- [ ] Decision logging and archive

## License

Ironbridge Strategy Group © 2026

---

**Questions?** See [CLAUDE.md](CLAUDE.md) for project architecture, or [docs/jarvis-workflow.md](docs/jarvis-workflow.md) for workflow details.
