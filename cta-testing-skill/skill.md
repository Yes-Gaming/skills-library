---
name: cta-testing
description: Systematic methodology for testing call-to-action (CTA) copy and button text with synthetic gambling personas. Use when running comparative CTA tests, conversion optimization studies, or button copy research with any user persona.
---

# CTA Testing Skill

## Overview

This skill provides a structured methodology for testing call-to-action (CTA) copy, button text, and action-oriented messaging with synthetic user personas. It ensures consistent, methodical testing across multiple rounds to identify conversion-optimized copy and understand user motivation drivers.

## When to Use This Skill

Activate this testing framework when:
- Running A/B or A/B/C CTA button text comparisons
- Testing primary vs secondary action copy
- Evaluating conversion messaging across different personas
- Optimizing landing page CTAs, registration flows, or deposit prompts
- Testing urgency-driven vs value-driven messaging
- Need to control for order bias and presentation effects

## Testing Methodology

### Standard Test Structure

**Default Configuration:**
- **Rounds per persona:** 10 (adjustable based on needs)
- **Order randomization:** Yes (prevents order bias)
- **Context variation:** Highly recommended (CTA effectiveness is context-dependent)
- **Question consistency:** Same questions each round for comparability

### Round Format

Each round follows this structure:

1. **Context Setup** (CRITICAL for CTA testing)
   - Where the CTA appears (landing page hero, registration flow, deposit prompt, email)
   - User's current state/goal (browsing, ready to sign up, considering deposit)
   - Device context (mobile button, desktop, in-app)
   - Surrounding elements (what else is visible)

2. **Stimulus Presentation**
   - Present 2-5 CTA options in randomized order
   - Show as they would appear (button, link, text)
   - Can test standalone or in full context
   - Keep visual formatting consistent across options

3. **Response Collection**
   - Mix of forced-choice and open-ended questions
   - Focus on action intent and motivation
   - Capture friction points and hesitations

4. **Record Keeping**
   - Log which option was presented first each round
   - Track all responses systematically
   - Note contextual variables (especially for CTAs)

## Question Templates

### Core Question Set (Recommended for CTA testing)

**Q1: Action Intent (Forced Choice)**
"Which call-to-action would you most likely [click/tap/act on]?"
- Provides: Clear preference data, action prediction
- Focus: Immediate behavioral intent

**Q2: Motivation (Open-ended)**
"What about it makes you want to take action? What's compelling?"
- Provides: Understanding of conversion drivers, psychological triggers
- Focus: Why it works, what motivates

**Q3: Friction Detection (Open-ended)**
"Which CTA would you ignore or skip? What makes you hesitate?"
- Provides: Conversion barriers, trust issues, hesitation factors
- Focus: What prevents action, red flags

**Q4: Value Perception (Forced Choice)**
"Which CTA creates the strongest sense of [value/urgency/benefit]?"
- Provides: Perceived value and urgency assessment
- Focus: What drives conversion beyond just clicks

### Optional Additional Questions for CTA Testing

**Q5: Clarity**
"Which makes it clearest what will happen when you click?"
- Tests: Transparency and expectation setting

**Q6: Trust**
"Which feels safest to click? Which makes you most comfortable taking action?"
- Tests: Trust and risk perception

**Q7: Urgency**
"Which creates the strongest feeling that you should act now?"
- Tests: FOMO and urgency effectiveness

**Q8: Differentiation**
"Which feels most different from typical gambling app CTAs?"
- Tests: Standing out vs blending in

**Q9: Context Fit**
"Which feels most appropriate for [this specific context]?"
- Tests: Context-appropriateness (critical for CTAs)

## Context Scenarios for CTA Testing

CTAs are highly context-dependent. Test in these scenarios:

### 1. Landing Page Hero CTA
**Context:** User just arrived from ad/search, hasn't signed up yet
**Persona State:** Curious, evaluating options, comparison shopping
**Test Focus:** Initial conversion, sign-up motivation
**Example CTAs:** "Start Playing Free," "Join Now," "Get Started," "Claim Bonus"

### 2. Registration Flow CTA
**Context:** Mid-registration, deciding whether to complete
**Persona State:** Partially committed, evaluating effort vs value
**Test Focus:** Registration completion, reducing drop-off
**Example CTAs:** "Create Account," "Sign Up," "Continue," "Almost Done"

### 3. First Deposit CTA
**Context:** Registered but hasn't deposited, reviewing payment options
**Persona State:** Cautious, evaluating trust and value
**Test Focus:** First deposit conversion, trust building
**Example CTAs:** "Make First Deposit," "Add Funds," "Deposit & Play," "Fund Account"

### 4. Promotional CTA
**Context:** Email or in-app notification about bonus/promotion
**Persona State:** Existing user, evaluating offer value
**Test Focus:** Engagement, promotional uptake
**Example CTAs:** "Claim Bonus," "Get Offer," "Activate Now," "Use Bonus"

### 5. Re-engagement CTA
**Context:** Dormant user, received win-back communication
**Persona State:** Lapsed, considering return
**Test Focus:** Reactivation, return motivation
**Example CTAs:** "Welcome Back," "Return & Play," "Come Back," "Restart Now"

### 6. Mobile In-App CTA
**Context:** In-app during active session
**Persona State:** Engaged, mid-activity
**Test Focus:** Continued engagement, next action
**Example CTAs:** "Play Now," "Bet Now," "Go," "Continue"

## Response Recording Format

For each round, record:

```
ROUND [N] - [PERSONA NAME]
Context: [Specific scenario - e.g., "Landing page hero, mobile, just arrived from Instagram ad"]
Persona State: [e.g., "Curious, comparing to other apps"]
Presentation Order: [List CTAs in order shown]

Q1 Choice: [CTA selected]
Q2 Motivation: "[Direct quote - what compels action]"
Q3 Friction: "[Direct quote - what creates hesitation]"
Q4 Value/Urgency: [CTA selected]

Additional Notes: [Any surprising reactions or context-specific insights]
---
```

## Analysis Framework

After completing all rounds, analyze:

### Quantitative Analysis

1. **Action Intent Frequency**
   - Count Q1 selections across all rounds
   - Calculate click-through prediction percentages
   - Note if one CTA dominates or if context-dependent

2. **Position Bias Check**
   - Compare selection rates when CTA shown first vs. second vs. third
   - Identify if order effects are present

3. **Intent vs. Value Gap**
   - Compare Q1 (action intent) to Q4 (value perception)
   - Note when they diverge (e.g., would click A but perceives B as more valuable)
   - Critical for understanding short-term vs long-term conversion

4. **Context Performance**
   - How does each CTA perform across different contexts?
   - Is there a universal winner or context-specific winners?
   - Which CTA is most versatile vs specialized?

### Qualitative Analysis

5. **Motivation Drivers from Q2**
   - What themes emerge in "why I'd click" responses?
   - Cluster motivations: urgency, value, clarity, trust, curiosity, FOMO
   - Identify which CTA taps into strongest motivations

6. **Friction Points from Q3**
   - What creates hesitation or resistance?
   - Common concerns: vague, pushy, confusing, untrustworthy, boring
   - Deal-breaker language or tone issues

7. **Persona Comparison**
   - How do different personas respond differently?
   - Casual vs serious users, young vs old, trust-sensitive vs risk-tolerant
   - Which CTA has broadest appeal vs niche appeal?

8. **Context-CTA Fit Analysis**
   - Which CTAs work best in which contexts?
   - Mismatches between CTA and context
   - Opportunities for context-optimized variations

## Output Format

### Summary Report Structure

```
# CTA TEST RESULTS

## Test Configuration
- Personas tested: [List with age/type]
- Rounds per persona: [N]
- Contexts tested: [List all scenarios]
- CTAs tested: [List all with exact copy]
- Date conducted: [Date]

## Quantitative Results

### Overall Action Intent (Q1) - Across All Contexts
[Persona 1 Name]:
- CTA A: X/10 (X%)
- CTA B: X/10 (X%)
- CTA C: X/10 (X%)

[Persona 2 Name]:
- CTA A: X/10 (X%)
- CTA B: X/10 (X%)
- CTA C: X/10 (X%)

### Context-Specific Performance
[Context 1 - e.g., Landing Page Hero]:
- CTA A: X votes
- CTA B: X votes
- CTA C: X votes

[Context 2 - e.g., First Deposit]:
- CTA A: X votes
- CTA B: X votes
- CTA C: X votes

### Value/Urgency Perception (Q4)
[Same structure as Q1]

### Intent vs. Value Gap Analysis
- CTAs where intent > value: [List - good for clicks, may not convert]
- CTAs where value > intent: [List - good for conversion, need better visibility]
- Aligned CTAs: [List - click intent matches value perception]

### Order Bias Analysis
[Note if any CTA performed significantly better/worse based on position]

## Qualitative Insights

### Why Winners Won
[Key motivation drivers from Q2 responses for top performers]
- Theme 1: [e.g., "Clear immediate value"]
- Theme 2: [e.g., "Creates urgency without being pushy"]
- Theme 3: [e.g., "Low friction, easy to understand"]

Representative quotes:
- "[Quote 1]"
- "[Quote 2]"

### Why Losers Lost
[Key friction points from Q3 responses about rejected CTAs]
- Barrier 1: [e.g., "Too vague about what happens next"]
- Barrier 2: [e.g., "Feels too salesy"]
- Barrier 3: [e.g., "No clear benefit"]

Representative quotes:
- "[Quote 1]"
- "[Quote 2]"

### Persona-Specific Patterns
[Persona 1]: [Key behaviors and preferences]
[Persona 2]: [Key behaviors and preferences]
[Contrasts]: [How personas differed]

### Context-Specific Insights
[Context 1]: [What works best and why]
[Context 2]: [What works best and why]
[Cross-context winners]: [CTAs that work everywhere]
[Context-dependent winners]: [CTAs that work in specific scenarios only]

## Recommendations

### Primary CTA Recommendation
**For [Context 1 - e.g., Landing Page]:** Use "[CTA X]"
- **Why:** [Key reasons from data]
- **Expected Impact:** [Conversion improvement estimate]
- **Works Best For:** [Persona types]

**For [Context 2 - e.g., Deposit Flow]:** Use "[CTA Y]"
- **Why:** [Key reasons from data]
- **Expected Impact:** [Conversion improvement estimate]
- **Works Best For:** [Persona types]

### Universal vs. Specialized Strategy
[Recommend whether to use one CTA everywhere or optimize per context]

### Segmentation Opportunities
[If different personas respond very differently, recommend segmentation strategy]

### Avoid These CTAs
- **"[CTA Z]":** [Why it failed, what was wrong]
- **"[CTA W]":** [Why it failed, what was wrong]

### Follow-up Testing Recommendations
[If needed, what to test next - e.g., variations on winner, new contexts, A/B test in production]

## A/B Testing Roadmap

### High Priority Tests (Run First)
1. **Test:** [CTA A] vs [CTA B] on [Context]
   - **Hypothesis:** [What you expect based on synthetic data]
   - **Success Metric:** [CTR, conversion rate, etc.]
   - **Sample Size Needed:** [Estimate]

### Medium Priority Tests
[Additional tests to run after high priority]

### Validation Tests
[Tests to validate synthetic findings with real users]
```

## Best Practices

### Do's
- **Always test CTAs in specific contexts** - never in isolation
- **Vary persona state** across rounds (curious, ready, hesitant, etc.)
- **Randomize presentation order** every round
- **Test on appropriate device** context (mobile vs desktop matters for CTAs)
- **Record verbatim motivation** - "why" is critical for CTAs
- **Look for intent-value gaps** - most important CTA metric
- **Test at least 10 rounds** per persona-context combination
- **Consider micro-copy** around CTA (supporting text matters)
- **Note persona hesitations** - friction is make-or-break for conversion

### Don'ts
- **Don't test CTAs without context** - they're meaningless in isolation
- **Don't ignore value perception (Q4)** - it predicts actual conversion, not just clicks
- **Don't assume universal CTAs work** - context matters enormously
- **Don't test too many at once** (2-4 is ideal, max 5)
- **Don't skip friction analysis (Q3)** - understanding "no" is as important as "yes"
- **Don't forget mobile vs desktop** - CTA effectiveness differs significantly
- **Don't test final copy without testing tone** variations (urgent vs casual, benefit vs feature, etc.)

## Common Test Scenarios

### Scenario 1: Landing Page Hero CTA Optimization
- 3 CTA options, 10 rounds per persona, 3 personas
- Context: Landing page hero section, new visitor
- Focus: Initial conversion, sign-up motivation
- All 4 core questions

### Scenario 2: Multi-Context CTA Testing
- 2 CTA options tested across 4 different contexts
- 10 rounds per context-persona combination
- Identifies universal winner or need for context-specific CTAs

### Scenario 3: Urgency vs. Value Testing
- Compare urgency-driven CTAs ("Limited Time," "Act Now") vs value-driven ("Get Bonus," "Start Free")
- Test across trust-sensitive vs risk-tolerant personas
- Identify which approach works for which audience

### Scenario 4: Trust-Building CTA Test
- Test CTAs with different trust signals
- Focus on Trust Seeker persona (40+, security-conscious)
- Context: First deposit decision point
- Critical for conversion optimization

### Scenario 5: Mobile vs Desktop CTA Optimization
- Same CTAs tested in mobile and desktop contexts
- Identify if brevity matters more on mobile
- Optimize for device-specific behavior

## Integration with Persona Skills

This skill should be used in conjunction with:
- `casual-entertainer` - Tests entertainment-focused CTAs
- `casino-explorer` - Tests discovery and variety CTAs
- `sports-enthusiast` - Tests betting action CTAs
- `trust-seeker` - Tests security and trust CTAs
- `cross-entertainment-engager` - Tests integrated experience CTAs

**Protocol:**
1. Load this CTA testing skill first
2. Load target persona skill(s)
3. Define context(s) to test
4. Run test rounds as persona in each context
5. Compile results using this skill's framework
6. Generate summary report with context-specific recommendations

## CTA-Specific Metrics

### Intent-to-Value Ratio
- **High Intent, High Value:** Ideal CTA (clicks and converts)
- **High Intent, Low Value:** Clickbait risk (clicks but doesn't convert)
- **Low Intent, High Value:** Missed opportunity (good CTA, needs better placement/design)
- **Low Intent, Low Value:** Failed CTA (rewrite or discard)

### Context Versatility Score
- Universal CTAs: Work well across all contexts (rare but valuable)
- Specialized CTAs: Work great in specific contexts (common, optimize per use case)
- Context-Dependent CTAs: Performance varies wildly by context (risky, need careful placement)

### Friction Coefficient
- Count friction mentions in Q3 per CTA
- Lower friction = higher conversion likelihood
- Types of friction: unclear, pushy, untrustworthy, confusing, boring

## Notes on CTA Testing vs. Other Testing

**CTAs are different from taglines:**
- **Context is critical** - same CTA performs differently in different places
- **Action intent matters more** than general preference
- **Friction detection is crucial** - small hesitations kill conversion
- **Value perception predicts conversion** better than click intent
- **Micro-copy matters** - supporting text around CTA affects performance
- **Device context matters** - mobile CTAs need different approach than desktop

**Use this framework specifically for:**
- Button copy
- Link text
- Action-oriented messaging
- Conversion-focused copy
- Email CTAs
- Registration flow actions
- Deposit/payment actions

**Do NOT use for:**
- Brand taglines (use tagline-testing skill)
- Descriptive copy
- Navigation labels
- Passive messaging

## Notes on Statistical Validity

With 10 rounds per persona-context combination:
- **7-3 split** suggests moderate preference (70% vs 30%)
- **8-2 or stronger** suggests strong preference
- **5-5 split** suggests no clear winner OR context-dependency
- **Intent-value alignment** matters more than raw vote counts
- **Consistent friction themes** are deal-breakers even with decent vote counts

This is synthetic testing, not real user research. Use results to:
- Inform CTA decisions and narrow options
- Identify potential conversion barriers before real testing
- Generate hypotheses for A/B testing
- Prioritize what to test in production
- NOT as replacement for actual conversion rate testing

**Always validate CTA winners with real A/B tests before full rollout.**
