---
name: logo-testing
description: Systematic methodology for testing logos, brand marks, and visual identity assets with synthetic gambling personas. Use when evaluating logo designs, brand identity options, or visual rebranding decisions with multimodal analysis.
---

# Logo Testing Skill

## Overview

This skill provides a structured methodology for testing logos, brand marks, icons, and visual identity assets with synthetic user personas. It leverages multimodal AI capabilities to analyze visual design elements and gather both quantitative preference data and rich qualitative insights about brand perception.

## When to Use This Skill

Activate this testing framework when:
- Evaluating multiple logo design concepts
- Testing logo redesigns or rebrands
- Comparing logo variations (color, layout, typography)
- Assessing brand mark recognition and memorability
- Testing logo effectiveness across different contexts (app icon, website header, merchandise)
- Evaluating visual identity consistency
- Understanding brand perception through visual elements
- Testing logo accessibility and clarity at different sizes

## Logo Testing is Different

Unlike text-based testing (taglines, CTAs), logo testing involves:
- **Visual analysis** - Requires viewing actual image files
- **Emotional response** - Immediate gut reactions to design
- **Brand association** - What the design communicates about the brand
- **Context dependency** - How logo works at different sizes and placements
- **Cultural sensitivity** - Visual symbols have cultural meanings
- **Memorability** - Can users recall and recognize it?
- **Differentiation** - Does it stand out in competitive landscape?

## Example Output

See `references/example_test_output.md` for a complete sample test report showing:
- Quantitative results across Preference-Trust-Memory Triangle
- Qualitative insights on visual elements and brand perception
- Context testing results (app icon, favicon, website header)
- Trust analysis (critical for gambling platforms)
- Why certain design approaches fail or succeed
- Visual identity system recommendations

## Testing Methodology

### Standard Test Structure

**Default Configuration:**
- **Rounds per persona:** 10 (adjustable based on needs)
- **Order randomization:** Yes (prevents order bias)
- **Context variation:** Highly recommended (logos appear in many contexts)
- **Asset format:** PNG, JPG, SVG (provided by user)
- **Display modes:** Full size, mobile icon size, favicon size

### Round Format

Each round follows this structure:

1. **Visual Presentation** (CRITICAL - actual image viewing)
   - Display logo image(s) to persona
   - Show in relevant context (app icon, website header, etc.)
   - Can show multiple sizes simultaneously
   - Present in randomized order

2. **Context Setup**
   - Where the logo appears (app store icon, website header, business card)
   - Viewing device (mobile, desktop, print)
   - Surrounding elements (competitor logos, brand colors)
   - User's current state (first impression, comparison shopping)

3. **Response Collection**
   - Mix of immediate reactions and considered responses
   - Visual element identification
   - Emotional and brand perception
   - Practical usability assessment

4. **Record Keeping**
   - Log which logo was presented first
   - Capture verbatim visual descriptions
   - Note specific design elements mentioned
   - Track emotional responses

## Question Templates

### Core Question Set (Recommended for logo testing)

**Q1: First Impression (Forced Choice)**
"Which logo makes the strongest positive first impression?"
- Provides: Initial visual appeal, gut reaction
- Focus: Immediate emotional response
- Timing: Ask within 3-5 seconds of viewing

**Q2: Visual Elements (Open-ended)**
"What do you notice first? Describe what you see."
- Provides: Attention hierarchy, focal points
- Focus: Which design elements stand out
- Look for: Colors, shapes, typography, symbols mentioned

**Q3: Brand Perception (Open-ended)**
"What does this logo tell you about the brand? What kind of company does this look like?"
- Provides: Brand associations, positioning perception
- Focus: What the design communicates
- Look for: Adjectives (modern, trustworthy, fun, premium, cheap, etc.)

**Q4: Trust & Quality (Forced Choice)**
"Which logo suggests the most trustworthy, professional gambling platform?"
- Provides: Credibility assessment
- Focus: Trust signals in visual design
- Critical for: Gambling platforms (trust is paramount)

**Q5: Recognition (Forced Choice)**
"Which logo would you most easily recognize again if you saw it tomorrow?"
- Provides: Memorability assessment
- Focus: Distinctive, memorable elements
- Critical for: Brand recall and recognition

**Q6: Context Fit (Open-ended)**
"Imagine this as an app icon on your phone. Does it work? Why or why not?"
- Provides: Practical usability insights
- Focus: Real-world application
- Varies by context tested

### Optional Additional Questions for Logo Testing

**Q7: Differentiation**
"Which logo feels most different from other gambling apps you've seen?"
- Tests: Uniqueness vs category conventions
- Reveals: Standing out vs fitting in

**Q8: Clarity at Scale**
"Can you still tell what this is when it's very small (like a favicon)?"
- Tests: Scalability and simplification
- Critical for: Multi-platform usage

**Q9: Color Impact**
"What emotions or feelings do the colors evoke?"
- Tests: Color psychology effectiveness
- Reveals: Emotional design drivers

**Q10: Symbol Interpretation**
"What does [specific symbol/icon] represent to you?"
- Tests: Icon clarity and meaning
- Critical for: Avoiding misinterpretation

**Q11: Competitive Comparison**
"If you saw this next to [competitor logos], which would you choose?"
- Tests: Competitive differentiation
- Reveals: Relative positioning

**Q12: Negative Associations**
"Does anything about this logo turn you off or concern you?"
- Tests: Red flags and negative reactions
- Critical for: Avoiding mistakes

## Demographic Testing Methodologies

### Single Logo, Multiple Visuals - Demographic Validation

**Use Case:** You have a logo design and want to test its appeal across different demographic segments (gender, age, etc.) in various visual contexts.

**Test Configuration:**
- **Logo:** Single design (with variations in context/application)
- **Demographics:** Males only / Females only / 50:50 split / As per audience demographics
- **Visual Contexts:** Multiple contexts (app icon, website header, social media, merchandise, etc.)
- **Rounds per demographic segment:** 10-15
- **Focus:** Does the logo work equally well across demographic segments and contexts?

**Question Set for Single Logo Demographic Testing:**

**Q1: First Impression by Context (Forced Choice)**
"Which version/context makes the strongest positive first impression?"
- Provides: Context preference by demographic
- Focus: Where does this logo shine for different audiences?
- Show: Logo as app icon, website header, social profile, merchandise

**Q2: Visual Appeal Assessment (Scale 1-10)**
"Rate the visual appeal of this logo. What draws you to it or turns you off?"
- Provides: Appeal intensity and specific attractive/unattractive elements
- Focus: What works for males vs females vs mixed audience
- Look for: Gender-specific color/shape/style preferences

**Q3: Brand Fit & Identity (Open-ended)**
"Does this logo feel like it's designed for someone like you? Why or why not?"
- Provides: Demographic targeting perception
- Focus: Inclusion, exclusion, who it speaks to
- Critical for: Understanding if logo alienates any demographic

**Q4: Context-Specific Trust (Rating by Context)**
"Rate your trust in this brand based on seeing the logo in each context:"
- App icon on your phone: [1-10]
- Website header: [1-10]
- Social media profile: [1-10]
- Physical merchandise: [1-10]
- Provides: Trust variance by context and demographic
- Focus: Where does credibility come from for each group?

**Q5: Gender/Age Perception (Open-ended)**
"Who do you think this logo is designed for? What age group? What gender? Why?"
- Provides: Target audience perception
- Focus: Does the design communicate intended demographic?
- Critical for: Avoiding unintended demographic skew

**Q6: Visual Element Preferences by Demographics (Open-ended)**
"What specific visual elements appeal to you? Colors? Shapes? Style? What would you change?"
- Provides: Demographic-specific design preferences
- Focus: Refinement opportunities for target segments
- Look for: Gender patterns (e.g., females prefer certain colors, males prefer geometric shapes)

**Q7: Cultural & Demographic Resonance (Open-ended)**
"Does anything about this logo feel particularly relevant or irrelevant to your lifestyle/interests?"
- Provides: Cultural and demographic fit assessment
- Focus: Personal connection by demographic segment
- Critical for: Understanding emotional resonance

**Q8: Application Context Ranking (Ranking Exercise)**
"Rank these contexts from where the logo works BEST to where it works WORST:"
- App icon
- Website header
- Social media profile picture
- Email signature
- Physical merchandise (t-shirt, hat, etc.)
- Loading screen
- Business card
- Provides: Context effectiveness hierarchy by demographic
- Focus: Optimal usage by audience segment

**Q9: Competitive Standing by Demographics (Forced Choice)**
"Compared to other gambling brand logos you've seen, this logo feels:"
- More premium/professional
- More casual/fun
- More trustworthy
- More modern
- More generic
- Provides: Competitive positioning by demographic
- Focus: How different segments position the brand

**Q10: Likelihood to Engage (Scale 1-10 with Reasoning)**
"How likely are you to download/use an app with this logo? Why?"
- Provides: Conversion intent by demographic
- Focus: Real-world impact of logo on user acquisition
- Critical for: ROI measurement

**Demographic Comparison Framework:**

After collecting responses, analyze:

1. **Gender Differences:**
   - Visual element preferences (colors, shapes, styles)
   - Trust levels by context
   - Brand perception alignment
   - Engagement likelihood gaps

2. **Age/Generational Patterns:**
   - Modern vs. traditional preference splits
   - Trust signal variations
   - Context effectiveness differences

3. **Cross-Demographic Consensus:**
   - Which aspects work universally?
   - Which elements polarize by demographic?
   - Optimization opportunities without alienating segments

4. **Context-Demographic Matrix:**
   - Which contexts work best for which demographics?
   - Where do all demographics align on context effectiveness?
   - Demographic-specific application strategies

---

### Multiple Logo Options - Demographic Comparison Testing

**Use Case:** You have 2-5 logo design options and need to determine which performs best across different demographic segments.

**Test Configuration:**
- **Logos:** 2-5 design options
- **Demographics:** Males only / Females only / 50:50 split / As per audience demographics
- **Visual Contexts:** Comparable settings (all shown in same contexts for fair comparison)
- **Rounds per demographic segment:** 10-15 per logo option
- **Order randomization:** Critical - rotate which logo shown first
- **Focus:** Which logo wins overall and within each demographic segment?

**Question Set for Multiple Logo Demographic Testing:**

**Q1: Immediate Preference by Demographics (Forced Choice)**
"Which logo makes the strongest positive first impression on you?"
- Provides: Initial preference by demographic segment
- Focus: Gut reaction differences between males/females/age groups
- Timing: Ask within 5 seconds of viewing all options

**Q2: Demographic Targeting Perception (Multiple Choice)**
"Which logo feels most designed for:"
- Males primarily
- Females primarily
- Everyone equally
- Younger adults (18-30)
- Mature adults (35-50)
- Older adults (50+)
- Provides: Perceived demographic targeting
- Focus: Intended vs. perceived audience

**Q3: Trust & Credibility by Demographics (Forced Choice)**
"Which logo makes you feel the brand is most trustworthy and professional?"
- Provides: Trust winner by demographic segment
- Focus: Trust signals vary by gender/age
- Critical for: Gambling platforms where trust = money deposits

**Q4: Visual Appeal Elements (Open-ended by Logo)**
For each logo, ask: "What do you like or dislike about this logo's visual design?"
- Provides: Specific element feedback by logo and demographic
- Focus: Why preferences differ between segments
- Look for: Gender/age patterns in color, shape, typography preferences

**Q5: Brand Perception Alignment (Open-ended by Logo)**
"What does [Logo A/B/C] tell you about the brand? What kind of company does this seem like?"
- Provides: Brand association mapping by logo and demographic
- Focus: Positioning perception differences
- Look for: Males see "professional," females see "aggressive," etc.

**Q6: Context Performance Comparison (Forced Choice by Context)**
"Which logo works best as:"
- A mobile app icon?
- A website header logo?
- A social media profile picture?
- Physical merchandise?
- Provides: Context winner by demographic
- Focus: Different demos may prioritize different contexts
- Critical for: Multi-context brand systems

**Q7: Memorability Test (Forced Choice)**
"Which logo would you most easily recognize and remember tomorrow?"
- Provides: Recognition winner by demographic
- Focus: Memory patterns differ by age/gender
- Look for: Younger demos prefer bold, older prefer familiar

**Q8: Emotional Response by Demographics (Rating Scale 1-10)**
For each logo: "Rate how this logo makes you feel:"
- Excited
- Trustful
- Confident
- Welcome
- Sophisticated
- Fun
- Provides: Emotional profile by logo and demographic
- Focus: Emotional resonance differences
- Critical for: Understanding why preferences diverge

**Q9: Demographic Inclusion Assessment (Scale 1-10 per Logo)**
"How much does this logo feel like it's designed for someone like you?"
- Provides: Inclusion/exclusion perception
- Focus: Which logos alienate which demographics?
- Critical for: Avoiding unintended demographic barriers

**Q10: Likelihood to Download/Engage (Scale 1-10 per Logo)**
"How likely would you be to download an app with this logo?"
- Provides: Conversion intent by logo and demographic
- Focus: Real-world business impact prediction
- Critical for: ROI and acquisition cost estimates

**Q11: Competitive Differentiation (Forced Choice)**
"Which logo stands out most from other gambling brands you know?"
- Provides: Differentiation winner by demographic
- Focus: Uniqueness perception varies by familiarity with category
- Look for: Males may know more gambling brands, prefer different differentiation

**Q12: Negative Associations by Demographics (Open-ended per Logo)**
"Does anything about [Logo X] turn you off, concern you, or feel inappropriate?"
- Provides: Red flags and demographic-specific concerns
- Focus: Gender/age-specific sensitivities
- Critical for: Avoiding designs that alienate key segments

**Q13: Age/Gender Appropriateness (Multiple Choice per Logo)**
"This logo feels most appropriate for:"
- Males
- Females
- All genders equally
- Ages 18-25
- Ages 26-35
- Ages 36-50
- Ages 50+
- All ages equally
- Provides: Perceived demographic appropriateness
- Focus: Matching intent with perception
- Critical for: Ensuring broad appeal if desired

**Q14: Final Selection by Demographics (Forced Choice with Ranking)**
"Rank all logos from your most to least favorite. Explain your #1 choice."
- Provides: Final preference hierarchy by demographic
- Focus: Clear winner identification per segment
- Critical for: Decision making with demographic strategy

**Q15: Trade-off Identification (Open-ended)**
"Are there any logos you found visually appealing but wouldn't trust? Or trustworthy but visually boring?"
- Provides: Preference-trust gaps by demographic
- Focus: Understanding trade-offs by segment
- Critical for: Preference-Trust-Memory Triangle analysis

**Demographic Analysis Framework:**

After collecting all responses across demographics:

1. **Overall Winner Identification:**
   - Which logo wins most questions across all demographics?
   - Clear consensus vs. demographic splits

2. **Demographic Segment Winners:**
   - Best logo for males only
   - Best logo for females only
   - Best logo for primary age demographic
   - Best logo for secondary age demographic

3. **Demographic Divergence Analysis:**
   - Questions where demographics agree (universal appeal)
   - Questions where demographics diverge (polarizing elements)
   - Magnitude of differences (slight preference vs. strong opposition)

4. **Gender Preference Patterns:**
   - Visual elements males prefer (colors, shapes, styles)
   - Visual elements females prefer
   - Trust signal variations by gender
   - Context effectiveness differences

5. **Age/Generational Patterns:**
   - Modern vs. traditional design preferences
   - Trust vs. appeal trade-offs by age
   - Symbol/icon interpretation by generation
   - Technology/digital familiarity effects

6. **Context-Logo-Demographic Matrix:**
   - Logo A: Best for [context] with [demographic]
   - Logo B: Best for [context] with [demographic]
   - Universal context winners vs. demographic-specific

7. **Preference-Trust-Memory Triangle by Demographics:**
   - Males: Logo X alignment analysis
   - Females: Logo Y alignment analysis
   - Age segment: Logo Z alignment analysis
   - Overall: Best triangle alignment across all demos

8. **Business Strategy Implications:**
   - **Single Logo Strategy:** Which logo maximizes total audience?
   - **Segmented Strategy:** Different logos for different demographics?
   - **Context Strategy:** Different logos for different applications?
   - **Acquisition vs. Retention:** Logo for new user appeal vs. loyal user trust?

9. **Demographic-Specific Red Flags:**
   - Elements that alienate males
   - Elements that alienate females
   - Age-inappropriate design choices
   - Cultural sensitivities by segment

10. **Optimization Opportunities:**
    - Can winning logo be refined for demographic segments?
    - Color variations for gender preferences?
    - Symbol adjustments for age appropriateness?
    - Context-specific optimizations?

**Sample Demographic Comparison Output:**

```
## Logo Preference by Demographics

### Males (n=50)
1. Logo B (Playing Card + Dice): 35/50 (70%)
2. Logo A (Minimalist "Y"): 10/50 (20%)
3. Logo C (Wordmark): 5/50 (10%)

**Why Logo B wins with males:**
- "Classic gambling symbols I recognize"
- "Professional and serious about betting"
- "Reminds me of poker nights - trustworthy"

### Females (n=50)
1. Logo B (Playing Card + Dice): 30/50 (60%)
2. Logo A (Minimalist "Y"): 15/50 (30%)
3. Logo C (Wordmark): 5/50 (10%)

**Why Logo B wins with females:**
- "Clear about what it is - honest"
- "Not overly aggressive like some gambling logos"
- "Professional without being masculine"

**Gender Insights:**
- Logo B wins both demographics (universal appeal)
- Males prefer Logo B more strongly (70% vs 60%)
- Females show more interest in Logo A (30% vs 20%)
  - Logo A's modern aesthetic appeals more to female segment
  - But trust concerns override preference for both genders
- Logo C fails equally with both demographics

### 18-30 Age Group (n=40)
1. Logo A (Minimalist "Y"): 18/40 (45%)
2. Logo B (Playing Card + Dice): 16/40 (40%)
3. Logo C (Wordmark): 6/40 (15%)

**Why younger demographic splits:**
- Logo A: "Modern, clean, matches my other apps"
- Logo B: "Bit old-school but definitely trustworthy"
- Trust vs. aesthetic trade-off more balanced

### 35-50 Age Group (n=40)
1. Logo B (Playing Card + Dice): 34/40 (85%)
2. Logo A (Minimalist "Y"): 4/40 (10%)
3. Logo C (Wordmark): 2/40 (5%)

**Why older demographic strongly prefers Logo B:**
- "Need to see gambling symbols to trust it"
- "Too many scam apps with generic modern logos"
- "Established look = established company"

### 50+ Age Group (n=20)
1. Logo B (Playing Card + Dice): 19/20 (95%)
2. Logo A (Minimalist "Y"): 0/20 (0%)
3. Logo C (Wordmark): 1/20 (5%)

**Overwhelming Logo B dominance:**
- "Only one that looks like a real gambling brand"
- "Modern logos feel like scams"
- Trust is absolutely paramount - aesthetic is secondary
```

**Strategic Decision Framework:**

Based on demographic analysis:

**If targeting broad market (all demographics):**
→ Choose logo with strongest cross-demographic appeal
→ Example: Logo B wins 70% males, 60% females, 85% high-value 35+ segment

**If targeting specific demographic:**
→ Choose logo that maximizes that segment even if overall performance is lower
→ Example: Logo A for 18-30 acquisition, Logo B for 35+ retention

**If running demographic-specific campaigns:**
→ Use different logos for different marketing channels
→ Example: Logo A in Instagram ads (younger), Logo B in Facebook/TV (older)

**Critical Principle:**
Never sacrifice trust (especially for gambling) to chase preference in a demographic segment. A logo that attracts but doesn't build trust creates expensive acquisition with zero retention.

## Logo Testing Contexts

Logos must be tested in multiple contexts as they appear differently:

### 1. App Store Icon (Mobile)
**Context:** 1024x1024 displayed at ~60-120px on phone screen
**Viewing:** User scrolling through app store
**Critical Factors:** Recognizable at small size, stands out in grid
**Test Questions:** Q1, Q4, Q5, Q6 (app icon variant)

### 2. Website Header/Logo
**Context:** Header logo, typically 200-400px width on desktop
**Viewing:** User on website homepage
**Critical Factors:** Professional, readable, fits header design
**Test Questions:** Q1, Q3, Q4, Q6 (header variant)

### 3. Favicon
**Context:** 16x16 or 32x32 pixels in browser tab
**Viewing:** User with multiple tabs open
**Critical Factors:** Recognizable at tiny size, distinctive shape/color
**Test Questions:** Q5, Q8

### 4. Social Media Profile
**Context:** Circular crop at ~200-400px
**Viewing:** User on Instagram, Facebook, Twitter
**Critical Factors:** Works in circular frame, readable in feed
**Test Questions:** Q1, Q5, Q7

### 5. Loading Screen / Splash Screen
**Context:** Large format, center of mobile screen
**Viewing:** User waiting for app to load
**Critical Factors:** Engaging, quality feel, brand presence
**Test Questions:** Q1, Q3, Q4

### 6. Merchandise / Physical Assets
**Context:** Printed on merchandise, business cards, signage
**Viewing:** User in physical environment
**Critical Factors:** Print quality, works in one color, various sizes
**Test Questions:** Q3, Q4, Q8

### 7. Competitive Landscape
**Context:** Shown alongside 3-5 competitor logos
**Viewing:** User comparison shopping
**Critical Factors:** Differentiation, standing out, category fit
**Test Questions:** Q7, Q11

## Visual Asset Preparation

### Required Formats

**For comprehensive testing, provide:**

1. **Full Color Primary Logo**
   - Format: PNG with transparency
   - Size: 1024x1024 or larger
   - Use: Main logo evaluation

2. **App Icon Version**
   - Format: PNG, 1024x1024
   - Use: Mobile app icon context
   - May be simplified from full logo

3. **Horizontal Lockup** (if applicable)
   - Format: PNG with transparency
   - Aspect: Rectangular (logo + wordmark)
   - Use: Website header, email signatures

4. **Monochrome Version**
   - Format: PNG with transparency
   - Colors: Black on transparent, white on transparent
   - Use: Print, merchandise, accessibility

5. **Small Size Preview**
   - Format: PNG at actual display sizes (32x32, 64x64, 128x128)
   - Use: Favicon, small icon testing

### Optional but Recommended

6. **Variations** (if testing alternatives)
   - Different color schemes
   - Layout variations
   - Typography alternatives
   - Symbol/icon variations

7. **Context Mockups**
   - Logo on app store screenshot
   - Logo in website header mockup
   - Logo on phone screen mockup
   - Logo alongside competitors

## Response Recording Format

For each round, record:

```
ROUND [N] - [PERSONA NAME]
Context: [e.g., "App icon on iPhone, scrolling app store"]
Logo(s) Shown: [File names in order presented]
Display Size: [e.g., "Mobile app icon size (~120px)"]

Q1 First Impression: [Logo selected]
Q2 Visual Elements: "[Direct quote - what they notice first]"
Q3 Brand Perception: "[Direct quote - brand associations]"
   - Adjectives mentioned: [modern, fun, trustworthy, etc.]
   - Brand type: [premium, casual, professional, etc.]
Q4 Trust/Quality: [Logo selected]
Q5 Recognition: [Logo selected]
Q6 Context Fit: "[Direct quote - does it work in context?]"

Visual Details Mentioned:
- Colors: [Which colors mentioned, reactions]
- Shapes: [Which shapes noticed, interpretations]
- Typography: [Font reactions if applicable]
- Symbols: [Icon/symbol interpretations]

Emotional Response: [positive, negative, neutral, specific emotions]
Red Flags: [Any concerns or negative reactions]

---
```

## Analysis Framework

After completing all rounds, analyze:

### Quantitative Analysis

1. **First Impression Preference (Q1)**
   - Count selections across all rounds
   - Calculate percentages
   - Identify clear winner or splits

2. **Trust/Quality Assessment (Q4)**
   - Count selections across all rounds
   - Compare to Q1 (preference vs trust gap)
   - Critical metric for gambling platforms

3. **Memorability (Q5)**
   - Count most recognizable logos
   - May differ from preference
   - Critical for brand building

4. **Position Bias Check**
   - Compare performance when shown first vs. second vs. third
   - Identify if order effects are present

5. **Preference-Trust-Memory Triangle**
   - Logos where all three align (ideal)
   - Logos strong in one but weak in others
   - Trade-offs to consider

### Qualitative Analysis

6. **Visual Element Attention (Q2)**
   - What do people notice first? (colors, shapes, symbols)
   - Consensus vs. varied perception
   - Intended focal point vs. actual focal point
   - Design hierarchy effectiveness

7. **Brand Association Themes (Q3)**
   - Cluster brand descriptors (modern, trustworthy, fun, premium, etc.)
   - Intended brand positioning vs. perceived positioning
   - Consensus across personas or divergence
   - Positive vs. negative associations

8. **Context Performance (Q6)**
   - Which logos work best in which contexts?
   - Versatility across contexts vs. context-specific strength
   - Scalability issues (works large but not small)
   - Practical usability concerns

9. **Color Psychology**
   - Which colors mentioned most
   - Emotional responses to color choices
   - Cultural color associations
   - Color distinctiveness vs competitors

10. **Symbol/Icon Interpretation**
    - What symbols are recognized/noticed
    - Intended meaning vs. perceived meaning
    - Cultural interpretation variations
    - Potential misinterpretation risks

11. **Red Flags & Concerns (Q12)**
    - Negative reactions and why
    - Design elements that create distrust
    - Unintended associations
    - Accessibility or clarity issues

12. **Persona-Specific Patterns**
    - Age-related preferences (Gen Z vs 40+)
    - Risk tolerance correlation (Trust Seeker vs Casual Entertainer)
    - Visual sophistication differences
    - Context preference variations

13. **Competitive Differentiation (Q7, Q11)**
    - Uniqueness vs. category conventions
    - Standing out vs. fitting in
    - Competitive advantage through design
    - Category leadership vs. challenger positioning

## Output Format

### Summary Report Structure

```
# LOGO TEST RESULTS

## Test Configuration
- Personas tested: [List with age/type]
- Rounds per persona: [N]
- Contexts tested: [List all scenarios]
- Logo variants tested: [List with file names/descriptions]
- Date conducted: [Date]

## Visual Assets Tested

### Logo A: [Name/Description]
[Display image or link to file]
**Description:** [Brief description of design elements]
**Intended Brand Positioning:** [What designer intended]

### Logo B: [Name/Description]
[Display image or link to file]
**Description:** [Brief description of design elements]
**Intended Brand Positioning:** [What designer intended]

[Additional logos...]

## Quantitative Results

### First Impression Preference (Q1) - Across All Personas
- Logo A: X/50 (X%)
- Logo B: X/50 (X%)
- Logo C: X/50 (X%)

**By Persona:**
[Persona 1 Name]:
- Logo A: X/10 (X%)
- Logo B: X/10 (X%)
- Logo C: X/10 (X%)

[Repeat for each persona]

### Trust/Quality Perception (Q4)
- Logo A: X/50 (X%)
- Logo B: X/50 (X%)
- Logo C: X/50 (X%)

**By Persona:**
[Same structure as Q1]

### Memorability (Q5)
- Logo A: X/50 (X%)
- Logo B: X/50 (X%)
- Logo C: X/50 (X%)

**By Persona:**
[Same structure as Q1]

### Preference-Trust-Memory Triangle

| Logo | Preference (Q1) | Trust (Q4) | Memory (Q5) | Alignment |
|------|----------------|------------|-------------|-----------|
| Logo A | X% | X% | X% | [High/Medium/Low] |
| Logo B | X% | X% | X% | [High/Medium/Low] |
| Logo C | X% | X% | X% | [High/Medium/Low] |

**Analysis:**
- Aligned logos: [Logos where all three metrics are similar]
- Trust-preference gap: [Logos where trust differs significantly from preference]
- Memorability outliers: [Logos remembered differently than preferred]

### Context-Specific Performance

[Context 1 - e.g., App Icon]:
- Logo A: X votes
- Logo B: X votes
- Logo C: X votes

[Context 2 - e.g., Website Header]:
- Logo A: X votes
- Logo B: X votes
- Logo C: X votes

### Order Bias Analysis
[Note if any logo performed significantly better/worse based on position]

## Qualitative Insights

### Visual Element Analysis (Q2)

**Logo A:**
- **Most noticed elements:** [Colors, shapes, symbols in order of mention frequency]
- **First impressions:** [Common immediate reactions]
- **Visual hierarchy:** [What draws attention in what order]

Representative quotes:
- "[Quote about what stands out]"
- "[Quote about visual elements]"

**Logo B:**
[Same structure]

**Logo C:**
[Same structure]

### Brand Perception Analysis (Q3)

**Logo A - Brand Associations:**
- **Positive descriptors:** [modern, trustworthy, premium, fun, etc. - frequency counts]
- **Negative descriptors:** [cheap, boring, confusing, etc. - frequency counts]
- **Brand type perceived:** [Premium/Casual/Professional/Entertainment/etc.]
- **Target audience perceived:** [Who this logo seems designed for]

Representative quotes:
- "[Quote about brand perception]"
- "[Quote about what company seems like]"

**Intended vs. Perceived Positioning:**
- Intended: [Designer's goal]
- Perceived: [What users actually see]
- Alignment: [High/Medium/Low]
- Gap analysis: [What's missing or misinterpreted]

**Logo B:**
[Same structure]

**Logo C:**
[Same structure]

### Context Fit Analysis (Q6)

**App Icon Context:**
- **Works well:** [Logos that excel as app icons]
  - Why: [Clarity at small size, distinctive, etc.]
- **Struggles:** [Logos that don't work as app icons]
  - Why: [Too detailed, unclear when small, etc.]

**Website Header Context:**
[Same structure]

**Favicon Context:**
[Same structure]

[Additional contexts...]

### Color Psychology Insights

**Logo A Colors:**
- **Primary colors used:** [List]
- **Emotional responses:** [Excitement, trust, energy, calm, etc.]
- **Cultural associations:** [Relevant cultural meanings]
- **Distinctiveness:** [Unique vs. category-typical]

**Logo B Colors:**
[Same structure]

### Symbol/Icon Interpretation

**Logo A Symbol:**
- **Symbol description:** [What the symbol is]
- **Intended meaning:** [What designer meant]
- **Perceived meaning:** [What users interpreted]
- **Clarity score:** [X/10 recognized correctly]
- **Misinterpretations:** [Unintended meanings, if any]

**Logo B Symbol:**
[Same structure]

### Red Flags & Concerns (Q12)

**Logo A:**
- **Negative reactions:** [Count and themes]
- **Concerns raised:** [Trust issues, clarity, professionalism, etc.]
- **Deal-breakers:** [Issues that would prevent usage]
- **Severity:** [Minor/Moderate/Critical]

Representative quotes:
- "[Negative reaction quote]"

**Logo B:**
[Same structure]

### Persona-Specific Patterns

**Casual Entertainer (22-28):**
- Preferred: [Which logo and why]
- Key factors: [What drove their preference]
- Unique insights: [Observations specific to this persona]

**Casino Explorer (20-30):**
[Same structure]

**Sports Enthusiast (25-35):**
[Same structure]

**Trust Seeker (40+):**
[Same structure - often very different from younger personas]

**Cross-Entertainment Engager (18-40):**
[Same structure]

**Generational Splits:**
- Under 30 vs. Over 40 preferences
- Visual sophistication differences
- Trust signal variations

### Competitive Differentiation Analysis (Q7, Q11)

**Uniqueness Scores:**
- Logo A: [High/Medium/Low differentiation from competitors]
- Logo B: [High/Medium/Low differentiation from competitors]
- Logo C: [High/Medium/Low differentiation from competitors]

**Competitive Context Performance:**
When shown alongside [competitor logos]:
- Stood out most: [Logo X]
- Blended in: [Logo Y]
- Confused with competitor: [Logo Z confused with which competitor]

## Recommendations

### Primary Logo Recommendation

**Recommended Logo:** [Logo X]

**Why This Logo Wins:**
1. [Reason 1 - e.g., "Strongest trust perception (75%)"]
2. [Reason 2 - e.g., "High memorability across all personas"]
3. [Reason 3 - e.g., "Works effectively across all contexts"]
4. [Reason 4 - e.g., "Clear brand positioning alignment"]

**Supporting Data:**
- Preference: X%
- Trust: X%
- Memorability: X%
- Context versatility: [High/Medium/Low]

**Strengths:**
- [Specific strong points from qualitative data]
- [Visual elements that work well]
- [Brand associations that align with goals]

**Considerations/Weaknesses:**
- [Any minor issues to be aware of]
- [Trade-offs being made]
- [Potential improvement areas]

### Context-Specific Recommendations

**For App Icon:**
Use: [Logo X or variant Y]
Why: [Clarity at small size, recognition, etc.]

**For Website Header:**
Use: [Logo X or variant Y]
Why: [Professional presentation, header fit, etc.]

**For Merchandise:**
Use: [Logo X or variant Y]
Why: [Print quality, one-color viability, etc.]

### Persona Segmentation Strategy

**If targeting primarily [Persona Type]:**
Recommendation: [Logo and reasoning]

**If broad market appeal needed:**
Recommendation: [Logo that works across personas]

**If willing to segment:**
Strategy: [Different logos for different audiences/contexts]

### Avoid These Options

**Logo [X] - Not Recommended:**
- **Why:** [Key problems from data]
- **Issues:** [Specific concerns raised]
- **Risk:** [Business impact of using this logo]

**Logo [Y] - Not Recommended:**
[Same structure]

### Design Refinement Opportunities

**For Selected Logo [X]:**

**Quick Wins:**
1. [Minor adjustment that could improve perception]
2. [Color tweak based on feedback]
3. [Scale optimization for specific context]

**Considerations for Future:**
1. [Longer-term evolution possibilities]
2. [Accessibility improvements]
3. [Cultural adaptation for new markets]

### Testing & Validation Roadmap

**Before Full Rollout:**

**High Priority:**
1. **Real User Testing:** Validate with actual users (n=100+)
   - A/B test in app store
   - Measure actual download rates
   - Track brand recall

2. **Accessibility Audit:**
   - Color contrast ratios
   - Clarity for color-blind users
   - Screen reader compatibility (alt text)

3. **Technical Testing:**
   - Render quality across devices
   - File size optimization
   - Print quality verification

**Medium Priority:**
4. **Cultural Sensitivity Review:**
   - Test in all target markets
   - Verify symbol meanings
   - Check color associations

5. **Competitor Monitoring:**
   - Ensure no similarity to existing marks
   - Trademark availability
   - Differentiation maintenance

6. **Scalability Testing:**
   - Minimum readable size
   - Maximum size (billboard, etc.)
   - Animation potential (if relevant)

## Visual Design Principles Validated

Based on results, these design principles were effective:

✅ **[Principle 1 - e.g., "Simplicity"]**
- Evidence: [Quotes/data showing simple logos performed better]

✅ **[Principle 2 - e.g., "Bold Colors"]**
- Evidence: [Color impact data]

✅ **[Principle 3 - e.g., "Meaningful Symbols"]**
- Evidence: [Symbol interpretation success]

❌ **[Principle that didn't work]**
- Evidence: [What failed and why]

## Appendix: Individual Round Data

[Include full round-by-round responses for reference]

ROUND 1 - Casual Entertainer
[Full response data]

ROUND 2 - Casual Entertainer
[Full response data]

[Continue for all rounds...]
```

## Best Practices

### Do's
- ✅ **Always provide actual image files** - logos must be viewed, not described
- ✅ **Test at multiple sizes** - logo should work at 16px and 1000px
- ✅ **Test in context** - show how logo appears in real usage
- ✅ **Capture immediate reactions** - first 3-5 seconds matter most
- ✅ **Ask about specific elements** - colors, shapes, symbols
- ✅ **Test across personas** - age groups see design very differently
- ✅ **Check for negative associations** - what turns people off
- ✅ **Compare to competitors** - differentiation is critical
- ✅ **Test context versatility** - app icon, website, print, etc.
- ✅ **Record emotional responses** - gut reactions predict brand connection

### Don'ts
- ❌ **Don't describe logos in text** - must show actual visual
- ❌ **Don't skip small size testing** - app icons need to work tiny
- ❌ **Don't ignore trust metrics (Q4)** - especially critical for gambling
- ❌ **Don't test too many variations** - max 4-5 logo options
- ❌ **Don't skip negative reaction questions** - need to find red flags
- ❌ **Don't ignore cultural context** - symbols mean different things
- ❌ **Don't assume designer intent = perception** - test what users actually see
- ❌ **Don't test without competitive context** - need to stand out
- ❌ **Don't forget accessibility** - color blindness, contrast, clarity
- ❌ **Don't skip context variation** - one context isn't enough

## Common Test Scenarios

### Scenario 1: Logo Redesign Decision
- Current logo vs. 2-3 redesign concepts
- All personas, 10 rounds each
- Multiple contexts (app icon, website, competitive)
- Focus on preference, trust, and recognition
- Decision: Rebrand or iterate current logo

### Scenario 2: New Brand Logo Selection
- 3-4 finalist concepts
- All personas, 10 rounds each
- All contexts (comprehensive testing)
- Focus on all questions
- Decision: Select winning logo

### Scenario 3: Logo Variation Testing
- Same logo in different color schemes or layouts
- Target personas only, 10 rounds each
- Specific contexts where variations would be used
- Focus on context fit and brand perception
- Decision: Primary logo + approved variations

### Scenario 4: Competitive Positioning Test
- Your logo(s) vs. 3-5 competitor logos
- All personas, 5-10 rounds each
- Competitive landscape context
- Focus on differentiation and standing out
- Decision: Positioning strategy

### Scenario 5: App Icon Optimization
- Logo variations optimized for app icon specifically
- Mobile-focused personas, 10 rounds each
- App icon context exclusively
- Focus on clarity, recognition, standing out in app store
- Decision: App icon variant selection

## Integration with Persona Skills

This skill should be used in conjunction with:
- `casual-entertainer` - Visual preferences of younger, entertainment-focused users
- `casino-explorer` - Emphasis on visual quality and premium feel
- `sports-enthusiast` - Professional, serious brand perception
- `trust-seeker` - Trust signals and credibility in visual design (CRITICAL)
- `cross-entertainment-engager` - Modern, integrated brand feel

**Protocol:**
1. Prepare logo asset files (PNG, various sizes)
2. Load this logo testing skill
3. Load target persona skill(s)
4. Present visual assets to persona
5. Run test rounds with question framework
6. Compile visual and perception data
7. Generate report with design recommendations

## Multimodal AI Capabilities

This skill leverages Claude's vision capabilities:
- **Image analysis** - Can view and analyze actual logo files
- **Visual element identification** - Colors, shapes, typography
- **Design critique** - Professional design assessment
- **Context simulation** - Can imagine logo in different contexts
- **Comparative analysis** - Side-by-side logo comparison
- **Cultural awareness** - Symbol and color meanings across cultures

**How to provide logos:**
- Upload image files directly to conversation
- Provide URLs to logo images
- Share screenshots of logos in context
- Use design tool exports (Figma, Adobe, etc.)

## Notes on Statistical Validity

With 10 rounds per persona:
- **7-3 split** suggests moderate preference
- **8-2 or stronger** suggests strong preference
- **5-5 split** suggests no clear winner (test more rounds or refine designs)
- **Visual consensus** - When people notice same elements, design hierarchy is clear
- **Perception alignment** - When brand perception matches intent, design is successful

**Remember:**
- Logo testing is subjective but patterns emerge
- Younger personas may prefer modern/bold, older prefer traditional/trustworthy
- First impressions matter most (3-5 seconds)
- Trust is most critical metric for gambling platforms
- Validate synthetic results with real user testing

**Always A/B test winning logo in production before full rebrand.**

---

**Skill Version:** 1.0.0
**Created:** November 2025
**For:** Yes.com gambling platform visual identity
**License:** Proprietary - Yes.com exclusive use
