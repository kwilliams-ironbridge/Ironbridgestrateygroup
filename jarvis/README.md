# Kenyatta's Intelligent Job Search & Consulting Agent (JARVIS)

## Overview
JARVIS is an automated job search and consulting opportunity tracking system designed to help Kenyatta S. Williams find, evaluate, and apply for roles and consulting engagements aligned with expertise in program management, workforce development, and training delivery.

**Goal:** Secure full-time role + identify consulting opportunities through conventional and unconventional methods.

---

## System Components

### 1. **Job Search Agent Prompt** (`job_search_agent_prompt.md`)
The master prompt defining:
- Candidate profile and expertise areas
- Target job titles and roles
- Search platforms and strategies
- Application workflow
- Consulting opportunity criteria
- Success metrics and KPIs

### 2. **Job Search Engine** (`job_search_engine.py`)
Python-based automation engine with:
- Opportunity flagging system
- Application logging and tracking
- Response management
- Report generation
- CSV export functionality

**Key Classes:**
- `JobSearchEngine` - Core engine for managing opportunities
- `LinkedInSearcher` - LinkedIn job search (requires API setup)
- `IndeedSearcher` - Indeed job search (requires scraping setup)
- `USAJobsSearcher` - Federal job search
- `UpworkSearcher` - Consulting opportunity search
- `ApplicationDraftGenerator` - Generate tailored cover letters and summaries

### 3. **Configuration** (`search_config.json`)
Centralized configuration including:
- Candidate profile
- Target roles and salary ranges
- Platform search settings
- Keywords and criteria
- Consulting services and rates
- Application strategy
- Tracking setup

### 4. **Tracking Database**
- **CSV File:** `jarvis/job_tracking.csv` (local backup)
- **Google Sheet:** "Kenyatta Job Search - Master Log" (primary tracking)
  - **Tab 1:** Job Applications (company, role, salary, date applied, status)
  - **Tab 2:** Consulting Opportunities (client, project, rate, contract status)
  - **Tab 3:** Analytics (response rates, interview rates, conversion metrics)

---

## Workflow

### Phase 1: Discovery
1. Agent searches platforms daily/weekly
2. Flags opportunities meeting criteria as "FLAGGED - REVIEW"
3. Logs in Google Sheet with link and summary

### Phase 2: Review & Decision
1. User reviews flagged opportunities
2. Updates status: "APPROVED" or "SKIP"
3. Agent notes reason if skipped

### Phase 3: Application
1. Agent generates tailored cover letter draft (if auto-generate enabled)
2. User customizes and submits application
3. Logs submission details and timestamp

### Phase 4: Tracking & Response Management
1. Log all recruiter/employer contacts
2. Track response dates and types (email, phone, interview, offer)
3. Analyze patterns (best platforms, response rates, salary ranges)

### Phase 5: Analytics & Optimization
1. Monthly reporting on key metrics
2. Identify high-ROI search channels
3. Refine keywords and criteria based on data

---

## Getting Started

### Step 1: Initial Setup
```bash
# Clone/ensure files exist
ls -la jarvis/
# Should contain:
# - job_search_agent_prompt.md
# - job_search_engine.py
# - search_config.json
# - job_tracking.csv (will be created)
```

### Step 2: Configure Search
Edit `jarvis/search_config.json`:
- Update target roles if needed
- Adjust salary range
- Add/remove platforms
- Set consulting rates

### Step 3: Start the Engine
```bash
python3 jarvis/job_search_engine.py
```

Expected output:
- Log file created at `jarvis/job_search.log`
- Example opportunity flagged
- Ready for integration with platforms

### Step 4: Set Up Google Sheet
1. Create Google Sheet: "Kenyatta Job Search - Master Log"
2. Create tabs: "Job Applications", "Consulting Opportunities", "Analytics"
3. Set up column headers per schema below
4. Share with this project for automated logging

### Step 5: Platform Integration
Each platform requires setup:

**LinkedIn:**
- [ ] Set up LinkedIn API credentials or use scraping library
- [ ] Implement `LinkedInSearcher.search_jobs()`
- [ ] Configure daily search schedule

**Indeed:**
- [ ] Set up web scraping (Selenium, BeautifulSoup) or API
- [ ] Implement `IndeedSearcher.search_jobs()`
- [ ] Configure daily search schedule

**USAJobs.gov:**
- [ ] Obtain USAJobs API key
- [ ] Implement `USAJobsSearcher.search_jobs()`
- [ ] Configure weekly search schedule

**Upwork:**
- [ ] Set up Upwork API or scraping
- [ ] Implement `UpworkSearcher.search_consulting()`
- [ ] Configure twice-weekly search

---

## Tracking Database Schema

### Job Applications Sheet
```
Date Found | Company | Role Title | Salary | Location | Source | Status | Date Applied | Response | Interview? | Notes
```

**Status Values:**
- FLAGGED - REVIEW (awaiting user review)
- APPROVED - READY TO APPLY (approved, waiting to apply)
- APPLIED (application submitted)
- DECLINED (user chose to skip)
- REJECTED (employer rejected)
- SHORTLISTED (selected for consideration)
- INTERVIEWED (interview scheduled/completed)
- OFFER (offer received)
- ACCEPTED (offer accepted)
- CLOSED (not moving forward)

### Consulting Opportunities Sheet
```
Date Found | Client/Platform | Project | Rate | Budget | Duration | Status | Date Proposed | Response | Contract Status
```

### Analytics Sheet
```
Metric | Value | Notes
---
Total Opportunities Found | [count] | 
Response Rate (%) | [%] | responses / applications
Interview Rate (%) | [%] | interviews / applications
Best Performing Platform | [name] | highest response rate
Average Response Time | [days] | 
Salary Offers Range | [min-max] | 
Consulting Leads Generated | [count] | 
Consulting Conversion Rate | [%] |
```

---

## Key Features

### ✅ Automated Opportunity Flagging
- Searches multiple platforms simultaneously
- Applies intelligent filtering
- Flags only relevant opportunities for review

### ✅ Smart Filtering
- Salary range validation
- Role/experience matching
- Geographic preferences
- Security clearance considerations

### ✅ Application Draft Generation
- Tailored cover letters using resume keywords
- Job fit analysis
- Application preparation checklists

### ✅ Response Tracking
- Log all recruiter contacts (email, phone, LinkedIn)
- Track interview dates and outcomes
- Monitor offer details and timeline

### ✅ Analytics Dashboard
- Response rate by platform
- Interview conversion rate
- Salary offer analysis
- Identify high-ROI search channels

### ✅ Consulting Opportunity Integration
- Parallel search on Upwork, Fiverr, Toptal
- Project-based opportunity tracking
- Rate and budget filtering
- Separate conversion funnel

---

## Success Metrics

**Primary Goal:** Secure full-time Program Management or Training/Workforce Development role

**Target Metrics:**
- Applications submitted/month: 10-15
- Response rate: 20-30%
- Interview rate: 10-15% of applications
- Consulting leads/month: 2-5
- Consulting conversion rate: 30-50%

**Timeline:** [TARGET DATE]

---

## Advanced Usage

### Custom Search Queries
Modify `search_keywords` in `search_config.json` for specialized searches:
```json
"search_keywords": [
  "program management government",
  "training manager remote",
  "workforce development consulting",
  "federal contract manager dayton"
]
```

### Multiple Profiles
Create separate config files for different job search strategies:
- `search_config_primary.json` - Full-time roles
- `search_config_consulting.json` - Consulting-only
- `search_config_dodjobs.json` - DoD-specific roles

### Integration with Email
Forward recruiter emails to tracking system:
- Auto-log contacts
- Extract salary/role details
- Flag urgent responses

### Salary Negotiation Tracking
Add "Salary Offered" column to applications sheet:
- Track market rates
- Identify undervalued offers
- Support negotiation strategy

---

## Troubleshooting

### Issue: No opportunities found
- [ ] Check platform API keys/credentials
- [ ] Verify keywords in `search_config.json`
- [ ] Ensure platforms are enabled
- [ ] Check job logs for errors: `tail -f jarvis/job_search.log`

### Issue: Too many irrelevant flagged opportunities
- [ ] Tighten filtering criteria in `search_config.json`
- [ ] Update must-have keywords
- [ ] Adjust minimum salary threshold
- [ ] Add negative keywords (roles to exclude)

### Issue: Low response rate
- [ ] Analyze applications tab - are you applying to right fit?
- [ ] Review cover letters for keywords alignment
- [ ] Check resume matches job description
- [ ] Increase application volume

### Issue: Google Sheet integration not working
- [ ] Verify sheet exists and is shared
- [ ] Check authentication credentials
- [ ] Ensure column headers match schema
- [ ] Review integration logs

---

## API Keys & Credentials

Store securely (not in repository):
```
.env file:
LINKEDIN_API_KEY=xxx
INDEED_API_KEY=xxx
USAJOBS_API_KEY=xxx
UPWORK_API_KEY=xxx
GOOGLE_SHEET_API_KEY=xxx
```

**Never commit credentials to repository!**

---

## Next Steps

1. [ ] Configure `search_config.json` with your preferences
2. [ ] Set up Google Sheet tracking database
3. [ ] Implement platform-specific searchers (LinkedIn, Indeed, etc.)
4. [ ] Run first job search: `python3 jarvis/job_search_engine.py`
5. [ ] Review flagged opportunities daily
6. [ ] Log applications and responses
7. [ ] Generate weekly reports
8. [ ] Analyze metrics and optimize

---

## Questions?
Refer to `job_search_agent_prompt.md` for detailed agent instructions and philosophy.
