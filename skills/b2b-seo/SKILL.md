---
name: b2b-seo
description: When the user wants to build or improve SEO for a B2B SaaS or software company. Use when the user mentions "B2B SEO," "SaaS SEO," "comparison pages," "competitor alternatives," "jobs-to-be-done SEO," "bottom-of-funnel content," "ROI calculator SEO," "use-case pages," "integration pages," or "category page." For general SEO audits, see seo-audit. For content planning, see content-strategy. For programmatic at scale, see programmatic-seo.
---

# B2B SEO

You are a B2B SEO strategist. B2B SEO differs from general SEO: lower search volumes but much higher buyer intent, longer sales cycles, and content that must satisfy both the champion and the economic buyer.

## Before You Start

**Check for product marketing context first:**
If `.claude/product-marketing-context.md` exists, read it before asking questions.

Key context to gather:
1. **Product and ICP** — What do you sell, and who buys it?
2. **Current SEO state** — Domain authority, traffic, ranking keywords?
3. **Sales cycle** — How long, how many stakeholders?
4. **Competitors** — Who are the top 3-5 competitors?
5. **Goal** — Pipeline, signups, brand awareness?

---

## B2B SEO vs. General SEO

| Dimension | B2B SEO | General SEO |
|-----------|---------|------------|
| Search volume | Low (50-2,000/mo typical) | High (10K-1M+) |
| Buyer intent | High | Mixed |
| Content depth | Very deep | Moderate |
| Sales cycle | 1-12 months | Days-weeks |
| Conversion | Demo/trial signup | Purchase or lead |
| Decision makers | 5-10 stakeholders | 1 person |
| Priority pages | Bottom-of-funnel | Top-of-funnel |

**Implication**: In B2B, a page ranking for 200 searches/month that converts 5% to demo requests is worth far more than a page ranking for 20,000 searches/month with 0.1% conversion.

---

## B2B SEO Page Types (Priority Order)

### 1. Bottom-of-Funnel Pages (Highest Priority)

These pages target buyers who already know they have a problem and are evaluating solutions.

**Competitor Alternative Pages**
- Target: "[Competitor] alternative" / "[Competitor] competitors"
- Intent: Buyer unhappy with or evaluating competitor
- Format: Honest comparison, your strengths, migration info
- See: **competitor-alternatives** skill for full framework

**Category / Comparison Pages**
- Target: "best [category] software," "top [category] tools"
- Intent: Buyer researching the market
- Format: Table comparing options, your differentiators highlighted
- Include: Pricing, key features, ideal use case per option

**[Competitor] vs. [You] Pages**
- Target: "[Your product] vs [Competitor]"
- Intent: Buyer doing final comparison
- Format: Structured comparison with clear differentiation
- Include: Feature comparison table, customer quotes, pricing transparency

**Pricing Pages (SEO-Optimized)**
- Target: "[Your product] pricing"
- Include: Schema markup, clear pricing tiers, FAQ
- Optimize for: Informational intent (people just want to know what it costs)

**ROI / Value Calculator**
- Target: "[Category] ROI," "cost of [problem]," "[category] calculator"
- Format: Interactive calculator + results page
- Benefit: Captures intent + generates shareable output
- Bonus: Each unique result URL can be indexed

### 2. Integration and Use-Case Pages

**Integration Pages**
- Target: "[Your product] + [popular tool]" or "[tool] integration"
- Why: Buyers search for their existing stack + new software
- Format: What the integration does, step-by-step setup, use cases
- Generate at scale: One page per major integration (Salesforce, HubSpot, Slack, etc.)

**Use-Case Pages**
- Target: "[Role] + [outcome]" or "[industry] + [product category]"
- Examples: "CRM for startups," "project management for agencies," "analytics for SaaS"
- Format: Problem → how you solve it for this specific context → social proof from same persona

**Persona-Specific Landing Pages**
- Target: "[Job title] + [tool/outcome]" — "marketing ops manager [tool]," "VP Sales [outcome]"
- Format: Role-specific pain → solution → proof from similar job titles

**Industry-Specific Pages**
- Target: "[Category] for [industry]" — "HR software for healthcare," "CRM for real estate"
- Format: Industry pain points → how your product addresses them → industry-specific customers

### 3. Middle-of-Funnel Pages

**Problem-Awareness Content**
- Target: "how to [solve problem your product addresses]"
- Intent: Buyer knows they have a problem, looking for approaches
- Format: Educational, solution-agnostic content → soft CTA

**Category Education Pages**
- Target: "what is [category]," "guide to [methodology]"
- Intent: Buyer learning about the space
- Format: Comprehensive guides, your brand as the authority

**Case Studies (SEO-Optimized)**
- Target: "[Industry] + [outcome] + case study"
- Optimize: Customer name, industry, outcome in title and H1
- Include: Metrics, timeline, specific use case

### 4. Top-of-Funnel Pages

**Trend and Research Content**
- Original data, benchmarks, state-of-[industry] reports
- Target: "[Industry] statistics," "[metric] benchmarks"
- High shareability + backlink potential

**Glossary / Definition Pages**
- Target: "what is [term]," "[jargon] definition"
- Intent: Buyer learning the vocabulary
- Low competition, good for brand building

**Educational Guides**
- Target: "how to [do something related to your category]"
- Intent: Research and skill-building
- Format: Comprehensive, structured, evergreen

---

## Keyword Strategy

### Keyword Categories for B2B
```
1. Brand: [Your product name] + variations
2. Competitor: [Competitor] + alternative, pricing, reviews
3. Category: [Your category] + software/tool/platform
4. Problem: [Problem your product solves] + solution
5. Use case: [Role/industry] + [outcome or tool type]
6. Integration: [Your product] + [other tool]
7. Educational: how to + [related topic]
8. BOFU: [Your product] + pricing, demo, reviews
```

### Keyword Research Process
1. Seed list: Start with your product, competitors, and ICP's job title
2. Expand with tools: Ahrefs, SEMrush, Keywords Everywhere
3. Mine competitor content: `site:competitor.com/blog` → what are they ranking for?
4. Mine G2/Capterra: Review language = exact searcher language
5. Mine sales calls: What do buyers call the problem? → those are search queries

### Prioritization Framework
Score each keyword:
- **Business relevance** (0-3): How closely does this relate to what you sell?
- **Buyer intent** (0-3): Is the searcher likely a buyer?
- **Search volume** (0-3): Enough volume to matter?
- **Competition** (0-3 inverse): Can you realistically rank?

Total score = buy intent × relevance is more important than volume.

---

## On-Page Optimization for B2B

### Title Tag Formula
`[Primary Keyword] | [Value Prop or Brand] — [Year if evergreen]`

Examples:
- "Salesforce Alternatives for SMBs (2026) | [Your Product]"
- "Best CRM for Startups: Compared and Reviewed | [Your Product]"
- "[Competitor] vs [You]: Which CRM Wins in 2026?"

### Meta Description
- 120-155 characters
- Include primary keyword
- Lead with the benefit or insight
- End with soft CTA ("Compare plans," "See the full breakdown")

### Heading Structure
- H1: Primary keyword, matches search intent
- H2: Main sections — for comparison pages, each competitor or feature category
- H3: Subsections
- Each heading should answer a likely question

### Content Structure for BOFU Pages
1. Hero: Clear statement of what this page is (for whom, what outcome)
2. Quick comparison table (scannable)
3. Detailed breakdown (for each option)
4. Your differentiation section (why you win)
5. Social proof (customer logos, quotes, case study snippet)
6. FAQ (capture long-tail and answer intent)
7. CTA (demo, trial, contact)

### Schema Markup (B2B Priorities)
- `SoftwareApplication` — for product/feature pages
- `FAQPage` — for FAQ sections
- `HowTo` — for tutorial content
- `Review` / `AggregateRating` — for comparison pages
- `BreadcrumbList` — site navigation
- See **schema-markup** skill for implementation

---

## Link Building for B2B

### Highest-Leverage B2B Link Sources
1. **Integration partners** — Request links on their integration directory pages
2. **Customers** — Case study pages on their site link back to yours
3. **Industry associations** — Member directories, tool recommendations
4. **G2/Capterra/TrustRadius** — Profile pages (high DA, relevant)
5. **Podcast appearances** — Host links to guests
6. **Co-authored research** — Share authorship = shared distribution + links
7. **Press / earned media** — PR for original data, product launches

### Content That Earns Links Naturally
- Original research and data studies
- Free tools and calculators
- Comprehensive definitive guides
- Frameworks that get named and cited

---

## Technical SEO for B2B SaaS

### Critical Technical Issues to Fix First
- Slow page speed (Core Web Vitals) — especially for JavaScript-heavy apps
- Duplicate content (especially on pricing/feature pages across plans)
- Crawl budget waste (paginated URLs, session IDs, infinite scroll)
- Broken links to high-authority external sources
- Missing or incorrect canonical tags

### For SaaS Specifically
- Ensure app subdomain (`app.yourproduct.com`) is properly partitioned from marketing site
- Don't block `app.` in robots.txt if you want help pages indexed
- Use `hreflang` if serving multiple languages/regions
- Ensure login walls don't block crawlers on public content

---

## Measuring B2B SEO Success

### Metrics by Stage
| Stage | Metric | Tool |
|-------|--------|------|
| Visibility | Organic impressions, keyword rankings | GSC, Ahrefs |
| Traffic | Organic sessions, new visitors | GA4 |
| Engagement | Bounce rate, scroll depth, time on page | GA4 |
| Conversion | Demo requests, trial signups from organic | GA4 + CRM |
| Pipeline | Opportunities sourced from organic | CRM attribution |
| Revenue | Closed-won from organic channel | CRM |

### B2B SEO Benchmarks (rough)
- Content takes 3-12 months to rank
- BOFU pages convert at 2-8%
- Integration pages: lower traffic, high conversion
- Comparison pages: moderate traffic, high intent, high conversion

---

## B2B SEO Roadmap (90 Days)

**Month 1: Foundation**
- Technical audit and fix critical issues
- Keyword research by funnel stage
- Optimize existing high-traffic, low-converting pages

**Month 2: BOFU Pages**
- Build/improve competitor alternative pages
- Build/improve category comparison pages
- Optimize pricing page for SEO

**Month 3: Use Case + Integration Pages**
- Launch integration pages for top 10 integrations
- Launch 3-5 use-case or industry pages
- Begin link building from integration partners

---

## Task-Specific Questions

1. What's your product, and who's the primary buyer?
2. Who are your top 3 competitors by name?
3. What does your current organic traffic look like (rough estimate)?
4. Which page types do you not have yet — comparison, use-case, integration?
5. What are your top 3 integrations? (highest customer usage)

---

## Related Skills

- **seo-audit**: For technical and on-page SEO audit
- **competitor-alternatives**: For building full competitor comparison pages
- **programmatic-seo**: For generating pages at scale
- **content-strategy**: For top-of-funnel content planning
- **schema-markup**: For structured data implementation
- **demand-generation**: For connecting SEO to pipeline programs
