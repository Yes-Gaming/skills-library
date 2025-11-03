# Simulation Configuration Template

Use this template to quickly configure and run a new synthetic simulation.

## Simulation Details

**Test Date:** [YYYY-MM-DD]
**Test Name:** [Brief descriptive name]
**Testing Subject Type:** [Taglines / CTAs / Visual Assets / UX Flows / Features / Other]

## Testing Materials

**Language:** [English / Danish / Both / Other]

**Materials to Test:**
1. [Material 1 - exact copy or description]
2. [Material 2 - exact copy or description]
3. [Material 3 - exact copy or description]
4. [Material 4 - exact copy or description]
5. [Material 5 - exact copy or description]
6. [Material 6 - exact copy or description]

## Persona Selection

**Personas to Include:** (check all that apply)
- [ ] Casual Entertainer (22-28, entertainment-focused)
- [ ] Casino Explorer (20-30, variety-seeking)
- [ ] Sports Enthusiast (25-35, betting-focused)
- [ ] Trust Seeker (40+, security-conscious)
- [ ] Cross-Entertainment Engager (18-40, integrated experience)

## Test Parameters

**Rounds per Persona Variation:** [Default: 10]
**Total Expected Tests:** [personas × 10 variations × rounds] = [total]

## Question Framework

**For this test type, use:**

### Q1 - Preference
**Question:** [Which would you most likely click/choose/use?]
**Measures:** Initial appeal, acquisition potential

### Q2 - Reasoning
**Question:** [Why did you choose that one?]
**Measures:** Qualitative insights, appeal factors

### Q3 - Rejection
**Question:** [Which would you least likely click/avoid?]
**Measures:** Repulsion factors, risks to avoid

### Q4 - Trust/Value/Urgency
**Question:** [Which suggests trustworthy/premium/urgent value?]
**Measures:** Conversion potential, credibility

## Success Criteria

**This test will be successful if:**
1. [Criterion 1 - e.g., "Identify clear winner with >40% preference"]
2. [Criterion 2 - e.g., "Understand preference-trust gaps"]
3. [Criterion 3 - e.g., "Get actionable recommendations for A/B testing"]

## Context & Background

**Why we're running this test:**
[Explain business context, what decision this will inform]

**Current hypothesis:**
[What do we think will perform best and why?]

**Target audience:**
[Who will see these materials in production?]

**Use case:**
[Where will winning option be used? App store, landing page, ads, etc.]

## Expected Timeline

**Execution Time:** [Estimated time for simulation]
**Results Delivery:** [When results needed by]
**Implementation:** [When winning option will be deployed]

## Stakeholders

**Results will be shared with:**
- [Name/Team 1]
- [Name/Team 2]
- [Name/Team 3]

## Notes

**Special considerations:**
[Any special requirements, constraints, or considerations]

**Previous tests:**
[Link to any related previous simulation results]

---

## Example: Completed Template

### Simulation Details

**Test Date:** 2025-11-03
**Test Name:** Q4 2025 Holiday Campaign CTAs
**Testing Subject Type:** CTAs (call-to-action buttons)

### Testing Materials

**Language:** English

**Materials to Test:**
1. "Start Playing Free"
2. "Claim Your Bonus"
3. "Join & Win"
4. "Play Now"
5. "Get Started"

### Persona Selection

**Personas to Include:**
- [x] Casual Entertainer (22-28, entertainment-focused)
- [x] Casino Explorer (20-30, variety-seeking)
- [ ] Sports Enthusiast (25-35, betting-focused) - Not relevant for casino campaign
- [x] Trust Seeker (40+, security-conscious)
- [x] Cross-Entertainment Engager (18-40, integrated experience)

### Test Parameters

**Rounds per Persona Variation:** 10
**Total Expected Tests:** 4 personas × 10 variations × 10 rounds = 400 tests

### Question Framework

**For CTA testing:**

### Q1 - Preference
**Question:** "Which call-to-action would you most likely tap/click?"
**Measures:** Initial appeal, click-through potential

### Q2 - Reasoning
**Question:** "What about it makes you want to take action?"
**Measures:** Motivation factors, appeal elements

### Q3 - Rejection
**Question:** "Which CTA would you ignore or distrust?"
**Measures:** Red flags, trust barriers

### Q4 - Urgency
**Question:** "Which creates the strongest sense of urgency or value?"
**Measures:** Conversion driver, FOMO factor

### Success Criteria

**This test will be successful if:**
1. Identify clear winner with >35% preference across all personas
2. Understand if different personas need different CTAs
3. Find CTA that balances acquisition (clicks) and trust (conversion)
4. Get specific recommendations for landing page vs ad usage

### Context & Background

**Why we're running this test:**
Planning Q4 holiday campaign. Need high-performing CTA for hero section of landing page and primary CTA in Facebook/Instagram ads.

**Current hypothesis:**
"Claim Your Bonus" will perform best due to explicit value proposition, but may underperform on trust with Trust Seeker segment.

**Target audience:**
All user segments, but focusing on acquisition (new users, not existing customers).

**Use case:**
- Primary: Landing page hero CTA button
- Secondary: Facebook/Instagram ad CTA button

### Expected Timeline

**Execution Time:** 2 hours for simulation
**Results Delivery:** EOD today (need for Monday stakeholder meeting)
**Implementation:** Campaign launches Nov 15, 2025

### Stakeholders

**Results will be shared with:**
- Marketing Director (campaign owner)
- Creative Team (ad development)
- Product Team (landing page implementation)
- CEO (final approval)

### Notes

**Special considerations:**
- Holiday timing matters - need urgency without being pushy
- Budget is significant for this campaign
- Previous campaign used "Play Now" with mediocre results

**Previous tests:**
- See results/2025-11-02_17-26-36/ for tagline testing methodology
- Q3 campaign CTA testing (not synthetic, real A/B test)

---

## How to Use This Template

1. **Copy this template** to a new file for each simulation
2. **Fill in all sections** with your specific details
3. **Share with Claude** along with the synthetic-simulation-execution skill
4. **Review results** in the generated results/ folder
5. **Archive completed template** with results for future reference

## Tips

- Be as specific as possible with materials to test
- Clearly define what success looks like
- Document your hypothesis (helps validate or challenge assumptions)
- Note any time constraints or special requirements
- Link to related previous tests for context
- Keep stakeholder list updated (who needs results?)
