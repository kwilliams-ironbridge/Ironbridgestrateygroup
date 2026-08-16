# Jarvis Chief of Staff Workflow

## Overview

Jarvis operates as your AI-powered chief of staff, monitoring multiple email accounts and organizing communications into actionable intelligence.

## Core Workflow

### 1. Email Synchronization (Every 5 minutes)

```
[Gmail Accounts] 
    ↓
[Jarvis Email Sync]
    ↓
[Parse & Metadata Extract]
    ↓
[Local Cache]
```

Jarvis:
- Connects to all configured Gmail accounts
- Fetches new/unread messages
- Extracts sender, subject, labels, timestamp
- Stores locally for processing
- Updates sync status in profile

### 2. Prioritization & Scoring

```
[Cached Messages]
    ↓
[VIP Sender Check] → High Priority
[Keyword Analysis] → Medium Priority
[Domain Check] → Context Priority
[AI Scoring] → Intelligence Score (0-100)
    ↓
[Prioritized Queue]
```

Jarvis scores each email based on:
- **VIP Sender Status** (weight: 10/10)
  - Preset high-priority senders
  - Repeated frequent senders
- **Keywords** (weight: 7-8/10)
  - "Urgent", "action required", "decision needed", etc.
- **Sender Domain** (weight: 4-5/10)
  - Your organization, key partnerships
- **Thread History** (weight: 3-4/10)
  - Ongoing conversations, follow-ups
- **Time Sensitivity** (weight: 2-3/10)
  - Time-bound messages, deadlines

### 3. Summarization

```
[High-Priority Messages]
    ↓
[Extract Key Information]
    - Main topic/request
    - Action items
    - Deadlines
    - Required decisions
    ↓
[Generate Summary]
    ↓
[Add to Daily Digest]
```

For each important message, Jarvis:
- Extracts the core ask/information
- Identifies who needs to respond
- Flags deadlines and decisions needed
- Provides full context for action

### 4. Notification & Routing

```
[Prioritized Messages]
    ↓
[Determine Routing]
    ├→ [Obsidian] → Daily Log + Action Items
    ├→ [Slack] → Real-time alerts (high priority only)
    └→ [Console] → Admin logs
    ↓
[User Notification]
```

**Real-time Alerts:**
- VIP emails → Immediate notification
- Decision-required emails → Immediate notification
- Urgent keywords → Immediate notification

**Daily Digest:**
- Time: 6:00 AM (configurable)
- Summary of all overnight messages
- Top 5 priority items
- Action items for the day
- Deadlines within 48 hours

### 5. Action & Response

```
[Daily Digest/Alert]
    ↓
[User Review & Decision]
    ↓
[Jarvis Executes]
    ├→ [Reply] → Draft/send response
    ├→ [Schedule] → Calendar event
    ├→ [Task] → Add to Obsidian task list
    └→ [Archive] → Organize email
```

Jarvis can:
- Draft email responses for approval
- Suggest calendar times for meetings
- Create action items in Obsidian
- Auto-archive low-priority messages
- Tag and organize emails

## Configuration Options

### Sync Frequency
```json
{
  "emailMonitoring": {
    "syncInterval": "5m"  // Check: 5m, 15m, 30m, hourly
  }
}
```

### Digest Frequency
```json
{
  "notifications": {
    "dailyDigestTime": "06:00",  // When to send digest
    "timezone": "America/New_York"
  }
}
```

### Summarization Level
```json
{
  "jarvisSettings": {
    "summarizationLevel": "detailed"  // brief, detailed, comprehensive
  }
}
```

### Priority Threshold
```json
{
  "jarvisSettings": {
    "priorityThreshold": "high"  // all, medium, high
  }
}
```

## Using Jarvis with Claude

### In Claude Chat:

**Check email status:**
```
"Jarvis, what's on my plate today? Run my email digest."
```

Jarvis will:
- Query the local cache
- Generate current summary
- Present top priorities
- Suggest next actions

**Monitor specific account:**
```
"Check my Columbia email for urgent messages."
```

Jarvis will:
- Filter by email account
- Look for urgent keywords
- Report findings

**Get context on a sender:**
```
"Who's been reaching out from investors@example.com? What do they want?"
```

Jarvis will:
- Find all messages from sender
- Summarize conversation thread
- Extract asks/deadlines

### Integration with Claude's Tools:

Jarvis leverages Claude's capabilities:
- **Search & Analysis**: Query email for patterns
- **Summarization**: Condense long email threads
- **Action Planning**: Convert emails to tasks
- **Decision Support**: Present pros/cons of requests

## Daily Chief of Staff Routine

### Morning (6:00 AM)
1. Jarvis sends daily digest
2. You review top 5 priorities
3. Jarvis books calendar time for urgent items

### Throughout Day
1. High-priority alerts come through
2. You handle urgent items
3. Jarvis queues routine emails for review

### Evening
1. You review any remaining priority items
2. Jarvis archives handled messages
3. Prepares tomorrow's digest

### Weekly (Sunday Evening)
1. Review all handled emails
2. Identify patterns/trends
3. Adjust VIP senders or keywords as needed

## Email Organization Best Practices

### Use Gmail Labels Strategically

**By Account Type:**
- `inbox` - All incoming mail
- `action-needed` - Requires your response
- `decision` - Needs your decision
- `archive` - Handled, keep for reference

**By Sender Priority:**
- `vip` - Critical stakeholders
- `important` - Key contacts
- `follow-up-pending` - Waiting on response

**By Time Sensitivity:**
- `urgent` - Act within hours
- `this-week` - Act within week
- `backlog` - Low priority

### Jarvis Monitoring Tips

1. **Set Up VIP Senders** - Add key stakeholders to prioritySenders
2. **Use Keywords** - Add domain-specific urgent terms
3. **Exclude Noise** - Add marketing/newsletter labels to excludeLabels
4. **Label Important Accounts** - Subdivide each email account's labels

## Metrics & Monitoring

Jarvis tracks:

```json
{
  "syncStatus": {
    "lastSyncTime": "2026-08-16T07:30:00Z",
    "messageCount": 1247,
    "unreadCount": 23,
    "highPriorityCount": 3,
    "actionItemsCount": 5
  }
}
```

Review weekly:
- Messages per account
- VIP response times
- Action items completed
- Digest accuracy

## Troubleshooting

### "Email not showing up in digest"
- Check if label is in monitoringRules.excludeLabels
- Verify sender isn't filtered by keywords
- Ensure monitoring is enabled for that account

### "Too many alerts, too noisy"
- Increase priorityThreshold to "high"
- Remove non-critical keywords
- Narrow VIP senders list

### "Missing important emails"
- Add sender to prioritySenders
- Add relevant keywords
- Check excludeLabels for accidental filtering

### "Digest coming at wrong time"
- Verify dailyDigestTime in config
- Check timezone setting
- Ensure Jarvis service is running

---

**Next Steps:**
1. Configure your profiles with all email accounts
2. Set up VIP senders and keywords
3. Choose your digest time and summarization level
4. Run test sync to verify all accounts are connected
5. Start using Jarvis commands in Claude chat
