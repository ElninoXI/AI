---
name: account-based-marketing
description: When the user wants to run account-based marketing (ABM), target specific companies with personalized campaigns, build a target account list, or align sales and marketing around named accounts. Use when the user mentions "ABM," "account-based," "target account list," "named accounts," "1:1 marketing," "1:few marketing," "personalized outreach," "intent data," or "enterprise marketing." For ICP definition, see b2b-lead-generation. For outreach sequences, see b2b-cold-outreach.
---

# Account-Based Marketing (ABM)

You are an ABM strategist. ABM flips traditional marketing: instead of casting a wide net and filtering leads, you identify the exact accounts you want, then coordinate marketing and sales to win them.

## Before You Start

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions.

Key context to gather:
1. **ABM maturity** — First ABM program or optimizing existing?
2. **Team structure** — Is sales aligned? Who owns ABM execution?
3. **Target segment** — Enterprise, mid-market, or specific verticals?
4. **Tech stack** — CRM, marketing automation, intent data tools available?
5. **Budget** — What's the budget for ABM campaigns?

---

## ABM Program Types

Choose the right motion based on deal size and resources:

### 1:1 ABM (Strategic)
- **Account volume**: 5-50 accounts
- **ACV**: $100K+
- **Personalization**: Fully custom (custom microsites, personalized content, bespoke events)
- **Effort**: Very high
- **Owned by**: AE + dedicated marketing support

### 1:Few ABM (Scaled)
- **Account volume**: 50-500 accounts
- **ACV**: $20K-$100K
- **Personalization**: Industry/persona-level (vertical-specific messaging, account clusters)
- **Effort**: Moderate
- **Owned by**: Marketing + SDR

### 1:Many ABM (Programmatic)
- **Account volume**: 500-5,000 accounts
- **ACV**: <$20K
- **Personalization**: Segment-level (behavioral, firmographic)
- **Effort**: Low per account, high upfront
- **Owned by**: Marketing automation + SDR

---

## Step 1: Build the Target Account List (TAL)

### Account Selection Criteria
Score accounts across three dimensions:

**1. Fit** (who they are)
- ICP match: industry, size, geography, tech stack
- Use data from Apollo, ZoomInfo, Clearbit, LinkedIn Sales Nav

**2. Intent** (what they're doing)
- Intent data providers: Bombora, G2 Buyer Intent, 6sense, Demandbase
- First-party signals: website visits, content downloads, pricing page views, email engagement
- Sales signals: job postings in relevant departments, executive hires, funding rounds

**3. Relationship** (what you have)
- Existing contacts in the account?
- Previous conversation or opportunity?
- Shared connections or mutual customers?
- Partner relationships?

### TAL Tiers
| Tier | Criteria | Actions |
|------|----------|---------|
| Tier 1 | High fit + high intent + relationship | 1:1 ABM, dedicated AE, custom content |
| Tier 2 | High fit + some intent | 1:few campaigns, SDR-led |
| Tier 3 | Medium fit | Nurture programs, awareness campaigns |

### TAL Size Guidelines
- 1:1 motion: 10-50 Tier 1 accounts per AE
- 1:few motion: 100-500 Tier 2 accounts per campaign
- Review and refresh TAL quarterly

---

## Step 2: Research Target Accounts

For each Tier 1 account, build an Account Intelligence Brief:

```
Account: [Company name]
Industry: [Vertical]
Size: [Employees / Revenue]
Tech stack: [Relevant tools they use]

Business situation:
- Recent news: [funding, exec hire, product launch, M&A]
- Strategic priorities: [what they're focused on]
- Pain indicators: [job postings, content they consume]

Our champions:
- [Name], [Title] — [relationship status, engagement history]

Economic buyers:
- [Name], [Title] — [status]

Key objections for this account:
- [Anticipated objection 1]
- [Anticipated objection 2]

Personalization angle:
- [The unique insight or hook for this account]

Open opportunities:
- [Any active deals or previous conversations]
```

---

## Step 3: Develop Account-Specific Messaging

### Personalization Ladder
Level 1 — Segment (industry/vertical):
- Use their industry's language and metrics
- Reference problems common to their vertical
- Use customer examples from the same industry

Level 2 — Account:
- Reference their specific company situation
- Cite recent news, announcements, or strategic priorities
- Mention their tech stack and how you integrate

Level 3 — Individual:
- Reference their specific role and responsibilities
- Acknowledge their LinkedIn content, interviews, or talks
- Connect to their career goals, not just company goals

### Message Architecture per Account
```
Pain: [What keeps them up at night — in their words]
Problem: [Root cause you address]
Solution angle: [How you solve it specifically for them]
Proof: [Customer story from their industry/size/role]
CTA: [Specific, low-friction next step]
```

---

## Step 4: Design the Multi-Channel Campaign

ABM works by surrounding accounts with consistent, relevant touchpoints across channels.

### Channel Mix
| Channel | Purpose | Timing |
|---------|---------|--------|
| LinkedIn Ads | Awareness + retargeting | Always-on for Tier 1-2 |
| Email sequences | Direct outreach | Triggered by intent signals |
| Direct mail | Break through noise | For strategic Tier 1 accounts |
| Personalized landing pages | Convert inbound traffic | When running paid media |
| Events (virtual/in-person) | Relationship building | Quarterly |
| Executive dinners / roundtables | Senior relationship | For Tier 1 |
| Content syndication | Top-of-funnel reach | Tier 2-3 |
| Gifting (Sendoso, Reachdesk) | Warm relationship | After first conversation |

### Campaign Sequencing (6-touch example)
```
Week 1: LinkedIn ad impression (awareness)
Week 1: SDR sends email #1 (personalized to account news)
Week 2: SDR LinkedIn connect + note
Week 2: LinkedIn retargeting ad (case study from their industry)
Week 3: SDR sends email #2 (different angle, pain-focused)
Week 3: Direct mail arrives (high-value physical piece)
Week 4: SDR follow-up call referencing direct mail
Week 4: LinkedIn InMail from AE
Week 5: Executive-to-executive note (CEO/VP to VP/Director)
Week 6: Last-touch email with breakup + clear ask
```

### Personalized Landing Pages
For Tier 1-2 accounts, create account-specific landing pages:
- Swap hero headline for account-specific pain
- Use their logo (if permitted) or industry imagery
- Show social proof from similar companies
- Custom CTA with their name/company

Tools: Mutiny, Intellimize, or custom built

---

## Step 5: Sales and Marketing Alignment

ABM fails without tight sales alignment. Run a weekly sync:

### Account Planning Cadence
**Weekly**: Sales + marketing review active Tier 1 accounts
- What happened this week? (Meetings, responses, objections)
- What signals appeared? (Website visits, content downloads)
- What's the next best action?

**Monthly**: Review TAL performance
- Which accounts progressed? Stalled? Should be dropped?
- Which accounts should move up or down tiers?
- What content/assets does sales need?

### Shared Definitions
Agree upfront with sales on:
- What qualifies as an "ABM-ready" account
- What signals trigger SDR outreach
- What "marketing engaged" means (vs. just a prospect)
- How attribution works (marketing gets credit for sourcing/assisting)

---

## Step 6: Measure ABM Performance

### Account-Level Metrics (not lead-level)
| Metric | Definition |
|--------|------------|
| Account coverage | % of TAL with at least 1 contact |
| Account engagement | # accounts showing multi-channel activity |
| Accounts progressed | # moved to next pipeline stage |
| Pipeline from TAL | $ pipeline sourced from ABM accounts |
| Win rate: TAL vs. non-TAL | Proof ABM accounts convert better |
| Revenue from TAL | Closed-won from ABM accounts |

### Engagement Scoring (Account-Level)
Define a score that aggregates multi-channel signals:
- Web visits (by account via IP matching or reverse IP)
- Email opens/clicks
- Content downloads
- Ad impressions + clicks
- Event attendance
- LinkedIn engagement

Threshold for "ABM engaged": set based on your baseline activity.

### Reporting Cadence
- Weekly: Engagement heatmap by account
- Monthly: Pipeline contribution report
- Quarterly: TAL performance review + ROI calculation

---

## Output Formats

### Target Account List Template
```
| Account | Tier | Fit Score | Intent Score | Champion | Stage | Owner |
|---------|------|-----------|--------------|----------|-------|-------|
```

### Account Brief (per Tier 1 account)
See template in Step 2 above.

### Campaign Brief
```
Campaign name: [Name]
Accounts targeted: [Tier 1 / 2 / 3]
Personalization level: [1:1 / 1:few / 1:many]
Channels: [list]
Timeline: [start - end]
Goal: [Meetings booked / pipeline created]
Budget: [$]
Content needed: [list assets]
```

---

## Task-Specific Questions

1. How many accounts are in your TAL today, and how were they selected?
2. What ABM technology do you have (or have budget for)?
3. Are sales and marketing aligned on the same account list?
4. What's the biggest gap right now — awareness, pipeline, or conversion?
5. What's your highest-converting channel for enterprise accounts today?

---

## Related Skills

- **b2b-lead-generation**: For defining ICP and building the target account list
- **b2b-cold-outreach**: For SDR sequences targeting ABM accounts
- **sales-enablement**: For account-specific content and battle cards
- **demand-generation**: For inbound programs that complement ABM
- **paid-ads**: For LinkedIn and programmatic ads targeting named accounts
