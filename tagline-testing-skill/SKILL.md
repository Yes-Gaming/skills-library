---
name: tagline-testing
description: Systematic methodology for testing taglines and brand messaging with synthetic gambling personas. Use when running comparative tagline tests, A/B preference studies, or brand positioning research with Recreational Spender or Mobile Gamer-Bettor personas.
---

# Tagline Testing Skill

## Overview

This skill provides a structured methodology for testing taglines, brand messaging, and positioning statements with synthetic user personas. It ensures consistent, methodical testing across multiple rounds to identify preference patterns and qualitative insights.

## When to Use This Skill

Activate this testing framework when:
- Running A/B or A/B/C tagline comparisons
- Testing brand lock-ups (brand name + tagline combinations)
- Evaluating messaging across different personas
- Gathering quantitative preference data with qualitative context
- Need to control for order bias and presentation effects

## Testing Methodology

### Standard Test Structure

**Default Configuration:**
- **Rounds per persona:** 10 (adjustable based on needs)
- **Order randomization:** Yes (prevents order bias)
- **Context variation:** Optional (can vary scenario/mood/channel)
- **Question consistency:** Same questions each round for comparability

### Round Format

Each round follows this structure:

1. **Context Setup** (optional but recommended)
   - Where the persona encounters the tagline
   - Their current mood/state
   - The channel (app store, Instagram ad, billboard, etc.)

2. **Stimulus Presentation**
   - Present 2-5 options in randomized order
   - Can be taglines alone or full brand lock-ups
   - Keep formatting consistent across options

3. **Response Collection**
   - Mix of forced-choice and open-ended questions
   - Forced-choice for quantitative analysis
   - Open-ended for understanding reasoning

4. **Record Keeping**
   - Log which option was presented first each round
   - Track all responses systematically
   - Note any contextual variables

## Question Templates

### Core Question Set (Recommended for most tests)

**Q1: Preference (Forced Choice)**
"Which [tagline/lock-up] would make you most likely to [click/download/try this]?"
- Provides: Clear preference data, countable across rounds

**Q2: Reasoning (Open-ended)**
"Why? What specifically appeals to you about it?"
- Provides: Understanding of what drives preference, themes to analyze

**Q3: Rejection Insight (Open-ended)**
"What's your immediate reaction to your least favorite option?"
- Provides: Red flags, friction points, negative associations

**Q4: Trust/Quality Signal (Forced Choice)**
"If you saw these [on the App Store/in an ad], which would feel most [trustworthy/premium/professional]?"
- Provides: Brand perception beyond just preference

### Optional Additional Questions

**Q5: Memorability**
"Which one would you remember after seeing it once?"

**Q6: Clarity**
"Which makes it clearest what the product offers?"

**Q7: Differentiation**
"Which feels most different from other gambling apps you've seen?"

**Q8: Emotional Response**
"Which makes you feel most [excited/curious/confident]?"

## Response Recording Format

For each round, record:

```
ROUND [N] - [PERSONA NAME]
Presentation Order: [List options in order shown]
Context: [If varied, describe context]

Q1 Choice: [Option selected]
Q2 Reasoning: "[Direct quote from persona]"
Q3 Rejection: "[Direct quote from persona]"
Q4 Trust: [Option selected]

---
```

## Analysis Framework

After completing all rounds, analyze:

### Quantitative Analysis
1. **Preference Frequency**
   - Count selections for Q1 across all rounds
   - Calculate percentages
   - Note if one option dominates or if it's split

2. **Position Bias Check**
   - Compare win rates when option shown first vs. second vs. third
   - Identify if order effects are present

3. **Trust vs. Preference Gap**
   - Compare Q1 (preference) to Q4 (trust) selections
   - Note when they diverge (e.g., prefer A but trust B more)

### Qualitative Analysis
4. **Thematic Coding of Q2 Responses**
   - What themes emerge in "why" responses?
   - Group similar reasoning together
   - Identify dominant appeals (e.g., "simplicity," "excitement," "clarity")

5. **Red Flag Identification from Q3**
   - What turns personas off?
   - Common complaints across rounds
   - Deal-breaker language or associations

6. **Persona Comparison**
   - How do different personas respond differently?
   - What appeals to one but not another?
   - Which option has broadest appeal vs. niche appeal?

## Output Format

### Summary Report Structure

```
# TAGLINE TEST RESULTS

## Test Configuration
- Personas tested: [List]
- Rounds per persona: [N]
- Options tested: [List all with full text]
- Date conducted: [Date]

## Quantitative Results

### Overall Preference (Q1)
[Persona 1 Name]:
- Option A: X/10 (X%)
- Option B: X/10 (X%)
- Option C: X/10 (X%)

[Persona 2 Name]:
- Option A: X/10 (X%)
- Option B: X/10 (X%)
- Option C: X/10 (X%)

### Trust/Quality Perception (Q4)
[Same structure as above]

### Order Bias Analysis
[Note if any option performed significantly better/worse based on position]

## Qualitative Insights

### Why Winners Won
[Key themes from Q2 responses for top performer]

### Why Losers Lost
[Key themes from Q3 responses about rejected options]

### Persona-Specific Patterns
[How responses differed between personas]

## Recommendations

### Primary Recommendation
[Clear statement of which option to use and why]

### Considerations
[Any caveats, trade-offs, or context-dependent factors]

### Follow-up Testing
[If needed, what to test next]
```

## Best Practices

### Do's
- **Randomize presentation order** every round
- **Use exact same questions** across rounds for comparability
- **Record verbatim responses** from personas
- **Test at least 10 rounds** per persona for pattern confidence
- **Vary context** if testing channel-specific effectiveness
- **Look for consensus** across different personas
- **Note surprising responses** that contradict expectations

### Don'ts
- **Don't lead the persona** with context that biases toward one option
- **Don't change question wording** mid-test
- **Don't skip rounds** if you see early patterns (complete full set)
- **Don't ignore qualitative data** in favor of just counting votes
- **Don't test too many options** at once (2-4 is ideal, max 5)
- **Don't expose personas to business strategy** or internal reasoning

## Common Test Scenarios

### Scenario 1: Simple A/B Tagline Test
- 2 options, 10 rounds each, 2 personas
- Focus on Q1 (preference) and Q2 (reasoning)
- Clear winner should emerge

### Scenario 2: Complex A/B/C with Lock-ups
- 3 full brand lock-ups, 10 rounds each, 2 personas
- All 4 core questions
- May reveal split preferences or contextual winners

### Scenario 3: Cross-Language Testing
- Same concept in multiple languages
- Test with culturally appropriate persona
- Check if translation maintains appeal

### Scenario 4: Context-Varied Testing
- Same options, but vary where persona encounters them
- Tests if tagline works across channels
- More complex analysis needed

## Integration with Persona Skills

This skill should be used in conjunction with:
- `recreational-spender` skill (Casual Kasper persona)
- `mobile-gamer-bettor` skill (when available)
- Any other synthetic user persona skills

**Protocol:**
1. Load this testing skill first
2. Load target persona skill(s)
3. Run test rounds as persona
4. Compile results using this skill's framework
5. Generate summary report

## Notes on Statistical Validity

With 10 rounds per persona:
- **7-3 split** suggests moderate preference (70% vs 30%)
- **8-2 or stronger** suggests strong preference
- **5-5 split** suggests no clear preference (test more or refine options)
- **Consistent reasoning** matters as much as vote counts

This is synthetic testing, not real user research. Use results to:
- Inform decisions and narrow options
- Identify potential issues before real testing
- Generate hypotheses for user research
- NOT as replacement for actual user testing with real people
