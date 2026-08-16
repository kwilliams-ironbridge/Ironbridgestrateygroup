# Ironbridge Strategy Group - Jarvis Chief of Staff System

## Project Overview

Jarvis is an AI-powered chief of staff system that operates across Obsidian, Claude, and Google services to manage professional communications, priorities, and workflows for Ironbridge Strategy Group leadership.

**Core Capability:** Jarvis monitors multiple email accounts associated with user profiles and orchestrates them as a unified communication system.

## Architecture

### 1. Profile Management (`profiles/`)
User profiles store:
- Basic profile info (name, organization role)
- Multiple email addresses with metadata
- Email authentication credentials (OAuth tokens)
- Email monitoring preferences
- Notification routing rules

### 2. Email Integration (`email/`)
- Gmail API authentication via OAuth 2.0
- Secure credential storage and refresh
- Multi-email account monitoring
- Email sync and organization

### 3. Jarvis Layer (`jarvis/`)
- Configuration for Claude/AI integration
- Email processing rules and priorities
- Communication orchestration
- Chief of staff workflow automation

## Key Files

| File | Purpose |
|------|---------|
| `profiles/schema.json` | Profile data structure definition |
| `profiles/users.json` | User profiles and email configurations |
| `email/gmail-config.json` | Gmail API settings and OAuth credentials |
| `jarvis/config.json` | Jarvis behavior and monitoring rules |
| `jarvis/email-monitoring.md` | Jarvis email monitoring procedures |
| `docs/gmail-setup.md` | Gmail API setup guide |
| `docs/jarvis-workflow.md` | Chief of staff workflow documentation |

## Quick Start

### Step 1: Set Up Gmail API
See `docs/gmail-setup.md` for OAuth token generation and credential management.

### Step 2: Create User Profile
Add your profile to `profiles/users.json` with your email addresses and authentication tokens.

### Step 3: Configure Jarvis
Update `jarvis/config.json` with monitoring preferences and email processing rules.

### Step 4: Connect to Claude/MCP
Jarvis uses Claude's tools to:
- Read email accounts
- Summarize messages
- Flag priorities
- Execute workflows

## Security

- OAuth tokens stored securely (not in git)
- Environment variables for sensitive data
- No plain-text passwords
- Credential refresh handled automatically

## Jarvis Capabilities

Jarvis monitors multiple email accounts and:
✓ Aggregates messages across accounts
✓ Identifies VIP senders and high-priority messages
✓ Summarizes daily digest
✓ Routes communications to appropriate workflows
✓ Maintains communication history in Obsidian
✓ Executes scheduled communication tasks

## Status

- [x] Profile architecture designed
- [x] Email integration framework established
- [ ] Gmail API setup completed
- [ ] First user profile created
- [ ] Jarvis monitoring active
