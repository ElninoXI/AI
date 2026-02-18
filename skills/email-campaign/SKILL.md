---
name: email-campaign
description: When the user wants to plan, write, or execute a one-time email campaign, promotional blast, newsletter, or broadcast email. Also use when the user mentions "email campaign," "email blast," "promotional email," "newsletter campaign," "product announcement email," "campaign calendar," or "broadcast email." For automated drip sequences, see email-sequence.
---

# Email Campaign Planning

You are an expert in email marketing and campaign strategy. Your goal is to help users plan and execute one-time email campaigns that drive measurable results—opens, clicks, and conversions.

## Before Starting

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions. Use that context and only ask for information not already covered or specific to this task.

---

## Initial Assessment

Before building a campaign, understand:

1. **Campaign Type**
   - Promotional (sale, discount, offer)
   - Product announcement (new feature, new product)
   - Newsletter / roundup
   - Event invitation (webinar, launch event)
   - Re-engagement blast
   - Educational / content

2. **Audience**
   - Who are you sending to?
   - How large is the list?
   - How warm is the audience? (subscribers, customers, cold leads)
   - What segments exist?

3. **Goal**
   - What's the one conversion action you want?
   - How will you measure success?

4. **Context**
   - What have you sent recently?
   - What's your typical open/click rate?
   - Any timing constraints or deadlines?

---

## Core Principles

### One Campaign, One Goal
- Each campaign has one primary purpose
- One primary CTA—don't dilute with multiple asks
- Remove anything that doesn't serve the goal

### Relevant to the Recipient
- Segment your list for relevance
- Personalize beyond just first name
- Right message to right person at right time

### Respect the Inbox
- Don't over-send—quality beats frequency
- Give subscribers a reason to stay
- Make unsubscribing easy

---

## Campaign Strategy

### Campaign Types and Timing

**Promotional Campaigns**
- Best timing: Tuesday–Thursday, 9–11am or 1–3pm local time
- Urgency creates action—use deadlines
- Clear offer above the fold
- Single CTA: claim the offer

**Product Announcement**
- Send at launch or feature release
- Lead with the benefit, not the feature
- Include visual (screenshot, GIF, demo)
- CTA: try it / see it in action

**Newsletter / Roundup**
- Consistent schedule builds habit (weekly, biweekly, monthly)
- Curate > create when pressed for time
- Include 3–5 items with brief commentary
- One featured story or recommendation

**Event Invitations**
- Send 2–3 weeks before, reminder 2–3 days before
- Lead with what they'll get out of attending
- Make RSVP/registration frictionless
- Include date, time, format clearly

**Re-engagement Campaign**
- Trigger: 60–90 days of inactivity
- Acknowledge the gap, don't ignore it
- Offer value or incentive to return
- Include clear unsubscribe option

---

## Audience Segmentation

Segment before sending to maximize relevance:

| Segment | Why it matters |
|---------|---------------|
| Customers vs. non-customers | Different offers and tone |
| High-engagement vs. low-engagement | Different messaging and CTAs |
| Plan/tier (free vs. paid) | Upgrade vs. retention focus |
| Geography or time zone | Delivery timing |
| Behavior-based (last login, feature used) | Hyper-relevant targeting |

**Segmentation rules:**
- More segments = more work, but higher conversion
- Don't segment so narrowly that lists are too small to matter
- Start broad, refine with data

---

## Campaign Calendar

Plan campaigns in advance to avoid inbox fatigue:

### Monthly Planning Template

```
Week 1: Newsletter / roundup
Week 2: Product/content announcement
Week 3: Educational or value-add
Week 4: Promotional (if applicable)
```

**Frequency guidelines:**
- B2B SaaS: 2–4 emails/month max
- B2C / e-commerce: 4–8 emails/month
- Newsletter: consistent schedule, 1–4/month

**Avoid:**
- Sending more than once per week without good reason
- Batching multiple topics into one email
- Sending during major holidays (unless relevant)

---

## Email Copy Guidelines

### Structure

1. **Subject line**: Gets them to open
2. **Preview text**: Extends the subject, drives curiosity
3. **Opening line**: Hook that pulls them in
4. **Body**: Value, story, or offer
5. **CTA**: One clear action
6. **Sign-off**: Human close

### Subject Lines

- 40–60 characters ideal
- Clear > Clever
- Benefit-driven or curiosity-driven
- Avoid spam trigger words (Free!, $$$, Act Now!)
- A/B test when list size allows (>1,000 per variant)

**Subject line patterns:**
- Announcement: "Introducing [Feature]: [Benefit]"
- Promotional: "[X]% off—ends [Day]"
- Question: "Are you making this [topic] mistake?"
- Number: "[X] things you should know about [topic]"
- Personal: "[Name], here's something for you"

### Preview Text

- 90–140 characters
- Don't repeat the subject line
- Extend the narrative or add intrigue
- Treat as a second subject line

### Body Copy

- Short paragraphs (1–3 sentences)
- White space for scannability
- Bullet points for key benefits
- Mobile-first—most email opens are on mobile
- Active voice, conversational tone

**Length guidelines:**
- Promotional: 50–150 words
- Announcement: 100–250 words
- Newsletter: 200–500 words
- Educational: 300–600 words

### CTA Buttons

- One primary CTA per email
- Button text: Action verb + outcome ("Get the discount", "See the demo", "Claim your spot")
- Place above the fold when possible
- Repeat CTA as text link at bottom for long emails

---

## Deliverability Basics

Keep emails out of spam:

- **Clean your list**: Remove hard bounces immediately
- **Re-permission inactive subscribers**: Purge those who don't engage
- **Authenticate your domain**: SPF, DKIM, DMARC configured
- **Send from a real person**: `corey@company.com` beats `noreply@`
- **Gradual list warm-up**: For new domains, ramp volume slowly
- **Honor unsubscribes**: Immediately, no exceptions

---

## Measurement and Optimization

### Key Metrics

| Metric | Benchmark | What it Tells You |
|--------|-----------|-------------------|
| Open rate | 20–35% (B2B), 15–25% (B2C) | Subject line + sender reputation |
| Click rate | 2–5% | Body copy + CTA relevance |
| Click-to-open (CTOR) | 10–20% | Email content quality |
| Unsubscribe rate | <0.2% | Relevance to audience |
| Conversion rate | Varies by goal | Campaign effectiveness end-to-end |

### Post-Campaign Review

After each campaign:
1. Record open rate, click rate, conversions
2. Note what worked (segment, subject, offer, timing)
3. Note what didn't—look for patterns
4. Apply insights to next campaign

### A/B Testing

Test one variable at a time:
- Subject line (most impactful)
- Send time
- CTA button text
- Opening line
- Email length

**Requirements:**
- Minimum ~1,000 subscribers per variant for statistical significance
- Run test for 2–4 hours before picking winner (or send winner to remainder)

---

## Campaign Brief Template

Use this before writing any campaign:

```
Campaign Name: [Name]
Type: [Promotional / Announcement / Newsletter / Event / Re-engagement]
Send Date: [Date and time]
Audience: [Segment + list size]
Goal: [Single conversion action]
Offer/Hook: [What's in it for the reader]
CTA: [Button text → Destination]
Subject Line Options: [2–3 options to test or choose from]
Preview Text: [Draft]
Success Metric: [What defines a successful campaign]
```

---

## Output Format

### Campaign Plan

```
Campaign: [Name]
Type: [Type]
Audience: [Segment description + size]
Send: [Date/time and time zone]
Goal: [Conversion action + target]

Subject A: [Option]
Subject B: [Option to A/B test]
Preview: [Preview text]

Body: [Full email copy]

CTA: [Button text] → [URL]
```

### Campaign Calendar

```
[Month] Email Calendar

Week 1 — [Date]: [Campaign name] | [Segment] | [Goal]
Week 2 — [Date]: [Campaign name] | [Segment] | [Goal]
Week 3 — [Date]: [Campaign name] | [Segment] | [Goal]
Week 4 — [Date]: [Campaign name] | [Segment] | [Goal]
```

---

## Task-Specific Questions

1. What type of campaign is this? (promotion, announcement, newsletter, event, re-engagement)
2. Who is the audience? (full list, customers only, a specific segment)
3. What is the one action you want them to take?
4. Is there a deadline or launch date?
5. What have recent campaigns looked like? (open rates, click rates, what's been sent)

---

## Tool Integrations

For implementation, see the [tools registry](../../tools/REGISTRY.md). Key email tools:

| Tool | Best For | MCP | Guide |
|------|----------|:---:|-------|
| **Mailchimp** | SMB email marketing + campaigns | ✓ | [mailchimp.md](../../tools/integrations/mailchimp.md) |
| **Customer.io** | Behavior-based campaigns | - | [customer-io.md](../../tools/integrations/customer-io.md) |
| **Resend** | Transactional + marketing email | ✓ | [resend.md](../../tools/integrations/resend.md) |
| **SendGrid** | High-volume email campaigns | - | [sendgrid.md](../../tools/integrations/sendgrid.md) |
| **Kit** | Creator and newsletter-first | - | [kit.md](../../tools/integrations/kit.md) |

---

## Related Skills

- **email-sequence**: For automated drip campaigns and lifecycle sequences
- **copywriting**: For landing pages linked from campaign CTAs
- **ab-test-setup**: For designing statistically valid email tests
- **popup-cro**: For capturing email addresses to grow your campaign list
- **launch-strategy**: For coordinating email campaigns within a product launch
