# Quick Start Guide - Job Search Agent

## 🚀 Start Here

### What is JARVIS?
Your personal intelligent job search agent that:
- ✅ Searches 6+ platforms daily for program management and training roles
- ✅ Flags opportunities matching your expertise
- ✅ Logs applications and tracks recruiter responses
- ✅ Searches for consulting opportunities on Upwork, Fiverr, Toptal
- ✅ Generates analytics on response rates and best platforms
- ✅ Sends you opportunities to review before applying

---

## 🎯 Your Targets

**Primary:** Full-time Program Manager / Training Manager role  
**Secondary:** Consulting projects (curriculum, training, program management)  
**Where:** Dayton, OH or fully remote  
**Salary Target:** $140K (range: $100K - $180K)  
**Position Level:** Director+ preferred (no mid-level roles)  

---

## 📋 Setup Checklist (5 minutes)

- [ ] **Step 1:** Google Sheet Setup
  - Create sheet: "Kenyatta Job Search - Master Log"
  - Add tabs: "Job Applications", "Consulting Opportunities", "Analytics"
  - Copy headers from `jarvis/README.md`
  - Share with this project

- [ ] **Step 2:** Run Engine (Optional test)
  ```bash
  python3 jarvis/job_search_engine.py
  ```
  Should output: "Job Search Engine Ready" ✅

- [ ] **Step 3:** Daily Workflow
  - Check flagged opportunities (via Google Sheet or email notification)
  - Approve or skip each opportunity
  - Log applications after submitting
  - Note responses from recruiters

---

## 📊 Daily Workflow (5-10 min)

### Morning Check-In
1. Open "Kenyatta Job Search - Master Log" Google Sheet
2. Filter for Status = "FLAGGED - REVIEW"
3. Review new opportunities (company, role, salary, fit)
4. Update status: "APPROVED" or "SKIP" + reason

### When Approved
1. Generate tailored cover letter (see templates below)
2. Customize and submit application
3. Log in sheet: Status = "APPLIED", add date and URL
4. Set phone reminder: 14 days to follow up

### Tracking Responses
- Recruiter calls? → Log in "Responses" column
- Email response? → Add contact date and message
- Interview scheduled? → Update status to "INTERVIEWED"
- Offer received? → Update status to "OFFER"

---

## 🎓 Cover Letter Templates

### Template 1: Program Manager Role
```
Dear [Company] Hiring Team,

I am writing to express my strong interest in the [Role Title] position at [Company].

As a retired U.S. Air Force Senior Master Sergeant (E-8) with 25+ years of program management experience, I bring proven expertise in managing complex, multi-million dollar programs with large distributed teams.

In my current role at Concept Plus, I manage a $30 million Air Force training contract with a 20-person team across four locations. Key achievements include:
- Delivering 100% on-time, on-budget program milestones
- Leading high-performing teams of 20+ personnel
- Managing strategic government client relationships
- Implementing process improvements saving 15% in operational costs

My background in [RESEARCH COMPANY'S FOCUS AREA] aligns directly with your team's priorities. I'm confident I can deliver immediate value and drive program success.

Thank you for considering my application. I look forward to discussing how my expertise can support [Company]'s mission.

Sincerely,
Kenyatta S. Williams
937-477-8210
kenyattawilliams1121@gmail.com
```

### Template 2: Training/Workforce Development Role
```
Dear [Company] Hiring Team,

I am writing to express my strong interest in the [Role Title] position at [Company].

With 25+ years of progressive leadership in training delivery, curriculum development, and workforce development, I bring a strategic approach to building high-performing teams and delivering measurable learning outcomes.

In my previous role as Curriculum Development Manager at U.S. Air Force Air Education and Training Command, I:
- Led 68 instructional professionals delivering training to 3,000+ students annually
- Developed comprehensive curriculum using ADDIE instructional design model
- Managed learning management systems (Blackboard, Canvas, SharePoint)
- Achieved 95%+ student satisfaction and competency benchmarks

I'm passionate about [COMPANY'S MISSION/APPROACH] and confident my experience in designing scalable training programs and leading workforce transformation initiatives makes me an excellent fit for your team.

Thank you for your consideration. I look forward to discussing this opportunity.

Sincerely,
Kenyatta S. Williams
937-477-8210
kenyattawilliams1121@gmail.com
```

### Template 3: Consulting Proposal (Upwork/Freelance)
```
Subject: Program Management & Training Consulting

Hello [Client],

I'm Kenyatta S. Williams, a consulting professional with 25+ years of experience in:
✓ Program management and delivery ($30M+ budgets)
✓ Training program design and curriculum development
✓ Workforce development and organizational strategy
✓ Team leadership and operational excellence

I can help you with [MATCH TO THEIR PROJECT NEEDS]:
- Design and implement comprehensive training programs
- Develop curriculum and learning objectives
- Manage program timelines and budgets
- Build high-performing training teams
- Optimize workforce development strategy

My background in government and federal contracting gives me deep expertise in complex program execution and stakeholder management.

Rate: $100-150/hour (flexible for project scope)
Availability: [3 days/week / 40 hours/week / specify]

Let's discuss how I can add value to your team. Feel free to reach out with questions!

Best regards,
Kenyatta S. Williams
kenyattawilliams1121@gmail.com
937-477-8210
```

---

## 📈 Weekly Tasks (30 minutes)

1. **Monday:** Review flagged opportunities from past week
2. **Wednesday:** Follow up on applications sent 2+ weeks ago
3. **Friday:** Log any responses and update analytics
4. **Monthly:** Generate report, identify best platforms, adjust strategy

---

## 🔍 Where Opportunities Are Searched

### Full-Time Jobs
- **LinkedIn** - Most connections from your network
- **Indeed** - Largest job board (program mgmt roles)
- **USAJobs.gov** - Federal positions (10-point veterans preference!)
- **University Boards** - Miami University, UD, Sinclair
- **Contractor Networks** - Booz Allen, SAIC, ManTech

### Consulting Gigs
- **Upwork** - Largest freelance platform for your expertise
- **Fiverr** - Shorter-term consulting projects
- **Toptal** - High-end consulting (premium rates)
- **LinkedIn** - Direct outreach to connections

---

## 💡 Pro Tips

### Maximize Response Rate
1. **Personalize cover letters** - Use company name + specific role details
2. **Keyword optimization** - Match job description language
3. **Fast application** - Apply within 24 hours of posting (top of inbox)
4. **Follow up** - Email after 2 weeks if no response
5. **Resume keywords** - Include exact phrases from job posting

### Best Times to Apply
- **Monday-Thursday morning** - When hiring managers review applications
- **Avoid Friday evening** - Gets buried in inbox
- **LinkedIn** - Tuesdays have highest engagement
- **Indeed** - Job searches peak on Sundays/Mondays

### Government Jobs Advantage
- You have **10-point veterans preference** - Use it!
- Apply to **all relevant federal positions** on USAJobs
- Highlight **Active Top Secret/SCI clearance** prominently
- Search for **DoD contractor roles** (they love vet hiring preferences)

---

## 🎯 Success Metrics

Track these monthly:
- **Applications submitted:** Goal 10-15/month
- **Response rate:** Goal 20-30%
- **Interview rate:** Goal 10-15% of applications
- **Consulting leads:** Goal 2-5/month
- **Average salary offers:** Target $85K-110K

---

## 🚨 When You Get an Offer

1. **Immediate:** Update sheet (Status = "OFFER")
2. **Review:** Salary, benefits, start date, location
3. **Research:** Glassdoor, LinkedIn company page
4. **Negotiate:** Don't accept first offer (usually room to negotiate)
5. **Document:** Record final package in analytics
6. **Close:** Mark other applications as "CLOSED" or "DECLINED"

---

## 📞 Follow-Up Script

**If no response after 2 weeks:**

Email subject: "Following up: [Your Name] - [Role Title]"

```
Dear [Hiring Manager/Recruiter],

I applied for the [Role Title] position at [Company] on [DATE]. 
I remain very interested in this opportunity and would appreciate any updates on the hiring timeline.

I'm confident my experience in [KEY SKILL] and proven track record in [ACHIEVEMENT] 
make me a strong fit for your team.

Thank you for your consideration. Happy to discuss further.

Best regards,
Kenyatta S. Williams
937-477-8210
kenyattawilliams1121@gmail.com
```

---

## 🆘 Help & Resources

**Agent Questions?** See `jarvis/job_search_agent_prompt.md`  
**Setup Issues?** See `jarvis/README.md`  
**Coverage?** Reach out to project manager  
**Ideas?** Document in "Notes" column of tracking sheet

---

## ✨ Remember

- **Consistent effort** beats perfect applications. Apply to 10-15 roles/month.
- **Patience is key.** Response rate is 20-30%, so you need volume.
- **Track everything.** You'll see patterns that improve your success rate.
- **Your experience is strong.** 25 years, top clearance, proven leadership = valuable asset.
- **Consulting is backup.** Use it to bridge gaps or supplement income while searching full-time role.

**Goal: Land your ideal Program Management role by [TARGET DATE]** 🎯

---

*Last updated: August 19, 2026*
