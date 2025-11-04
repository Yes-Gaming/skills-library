---
name: synthetic-simulation-execution
description: Orchestration meta-skill for running large-scale isolated synthetic user testing with persona variations and complete documentation. Use when executing comprehensive testing simulations with 100+ isolated tests across multiple personas and test subjects.
---

# Synthetic Simulation Execution Skill

## Purpose
Execute comprehensive synthetic user testing by generating multiple isolated persona variations and running systematic tests on provided materials (taglines, CTAs, visual assets, etc.) with complete documentation and results reporting.

## Key Innovation: Unique Persona Variations
Unlike traditional testing that produces identical responses, this skill generates **10 unique variations** for each base persona, where each variation:
- Is a fully-realized synthetic individual with unique background, communication style, and perspective
- Responds in their own voice using contextually relevant language and cultural references
- Brings authentic survey response diversity (brief/detailed/skeptical/enthusiastic/etc.)
- Provides realistic variation within the persona type (avoiding artificial consensus)

This approach delivers **realistic preference distribution** rather than homogeneous results, revealing:
- High consensus signals (8-10 variations agree) = Strong, actionable insights
- Moderate consensus (6-7 variations agree) = Directional with nuance
- Split opinions (4-6 variations per option) = Need for segmentation or further testing
- Communication style patterns = Opportunity for dynamic messaging

## Core Principles

### 1. Context Isolation
- Each test round must be completely independent
- No memory or context pollution between rounds
- Fresh perspective for every synthetic person
- Use separate agent instances for true isolation

### 2. Persona Variation Generation
- Load base persona from existing skills library
- Generate 10 unique variations of each base persona
- **Critical:** Each variation must be a fully-realized individual, not a template
- Each variation should have:
  - Same core characteristics and motivations (from base persona)
  - Different specific background details (unique life story)
  - Unique personal context (specific circumstances and experiences)
  - Distinct expression style (how they communicate in surveys)
  - Individual demographic nuances (within persona range)
  - Made-up contextually relevant information that makes them feel real
  - Survey response voice that reflects their personality and communication preferences

### 3. Systematic Testing
- Apply consistent question framework across all variations
- Randomize presentation order to prevent position bias
- Capture both quantitative (votes) and qualitative (reasoning) data
- Document rejected options and why

## Execution Protocol

### Phase 1: Setup and Planning

**When user requests a simulation, gather:**

1. **Testing Subject Type:**
   - Taglines (brand messaging)
   - CTAs (call-to-action buttons/copy)
   - Visual assets (images, designs, layouts)
   - UX flows (user experience sequences)
   - Product features (functionality descriptions)
   - Other (specify)

2. **Testing Materials:**
   - Collect all variants to be tested
   - Ensure materials are clearly labeled/numbered
   - Note any language requirements (English, Danish, etc.)

3. **Personas to Use:**
   - Identify which base personas from `persona-skills/` folder
   - Load any available persona skills from the library
   - User can provide their own custom personas
   - User can select subset or all available personas
   - Each persona should have clear demographic and behavioral characteristics

4. **Test Parameters:**
   - Number of rounds per persona variation (default: 10)
   - Total tests = (# personas) × (10 variations) × (# rounds)
   - Confirm total test count with user

### Phase 2: Persona Variation Generation

**For each selected base persona:**

Generate 10 unique synthetic individuals with DISTINCT personalities, expression styles, and contextual backgrounds. Each variation should feel like a real person responding to a customer preference survey, not a template response.

**Critical: Each variation must have:**

**1. Demographic Details:**
- Specific age within range (e.g., 24 vs 27)
- Geographic location (specific city/region)
- Occupation/profession (specific role, not generic)
- Income bracket (within persona's typical range)
- Education level
- Relationship status and household composition

**2. Behavioral Context:**
- Specific frequency patterns (e.g., "Friday nights after work" vs "Daily lunch breaks")
- Favorite games/sports with personal reasons why
- Typical bet sizes with context (e.g., "€10-20 when feeling lucky")
- Device preferences (specific phone model, OS version, screen habits)
- Time of day preferences with lifestyle context

**3. Psychographic Nuances:**
- Risk tolerance variations (with specific examples)
- Social vs solo play preferences (with social context)
- Motivation emphasis (fun vs profit vs social) with personal backstory
- Tech savviness level (with specific behaviors)
- Brand loyalty tendencies (with examples of brands they love/hate)

**4. Personal Background & Voice:**
- How they discovered gambling (specific story)
- Past positive/negative experiences (memorable moments)
- Current gambling goals (realistic and personal)
- Biggest concerns or priorities (emotionally grounded)
- Communication style (casual, formal, enthusiastic, cautious, etc.)
- Language quirks (vocabulary, sentence structure, emoji use)
- Cultural context (local references, idioms, expressions)

**5. Survey Response Style:**
Each variation should respond like a real person in a preference survey:
- **Variation 1**: Brief, direct answers ("I like it because it's clear")
- **Variation 2**: Detailed, explanatory ("Well, I think the reason I prefer this one is...")
- **Variation 3**: Skeptical, critical ("Honestly, none of these really grab me, but if I had to choose...")
- **Variation 4**: Enthusiastic, emotional ("This one just FEELS right! It speaks to me...")
- **Variation 5**: Comparative, analytical ("Compared to option 2, this one...")
- **Variation 6**: Storytelling ("This reminds me of when I...")
- **Variation 7**: Practical, focused ("From a usability standpoint...")
- **Variation 8**: Social/influenced ("My friends would probably...")
- **Variation 9**: Uncertain, hedging ("I guess maybe this one, though I'm not sure...")
- **Variation 10**: Confident, decisive ("Definitely this one. No question.")

**Example Variation Template:**
```
Base Persona: [Any persona from persona-skills/ folder]
Variation #3:
- Name: "Marcus, 26"
- Location: Copenhagen, Vesterbro neighborhood
- Occupation: Junior graphic designer at a digital agency
- Income: 35,000 DKK/month
- Device: iPhone 13, prefers mobile over desktop
- Gambling Pattern: Plays slots on Friday evenings after work drinks, 100-300 DKK sessions
- Motivation: "I just want to unwind and have a bit of fun. If I win, great, but it's really about the entertainment."
- Key Concern: "I don't want to feel like I'm being manipulated or tricked. Transparency matters to me."
- Discovery: "A colleague showed me an app during a team outing. We were all trying different games."
- Communication Style: Casual but thoughtful, uses design terminology, prefers clarity
- Response Pattern: Tends to give measured, considered answers with visual/design references
- Cultural Context: Uses Danish expressions occasionally, references Copenhagen nightlife
- Survey Voice: "I think what appeals to me is... [explains reasoning]... but I can see how others might feel differently."
```

### Phase 3: Question Framework Design

**Adapt questions based on testing subject type:**

**Note:** Specific testing methodologies are available in the `testing-skills/` folder. Reference these for detailed question frameworks and context scenarios:
- `testing-skills/tagline-testing-skill/` - For brand messaging
- `testing-skills/cta-testing-skill/` - For call-to-action copy with context frameworks
- `testing-skills/logo-testing-skill/` - For visual identity and logo testing
- Custom testing frameworks can be created following the same pattern

**Generic 4-Question Framework (adaptable to any test type):**

1. **Q1 (Preference):** "Which [option] would you most likely [choose/click/use]?"
   - Captures initial appeal and preference
   - Forced choice to prevent "all are good" responses

2. **Q2 (Reasoning):** "Why did you choose that one? / What appeals to you about it?"
   - Open-ended to capture qualitative insights
   - Reveals motivational drivers and decision factors

3. **Q3 (Rejection):** "Which [option] would you [avoid/ignore/distrust] and why?"
   - Identifies friction points and turn-offs
   - Reveals what repels or creates barriers

4. **Q4 (Secondary Metric):** "Which [option] [builds trust/creates urgency/suggests quality/etc.]?"
   - Adapt based on what matters most for the test subject
   - Often reveals preference vs. conversion gaps

**For specific test types, consult the relevant testing skill in `testing-skills/` for optimized question frameworks and context scenarios.**

### Phase 4: Test Execution

**CRITICAL: Context Isolation and Variation Uniqueness**

Each of the 10 variations must be executed in a completely separate, isolated agent instance to prevent context pollution. The sub-agent should receive ONLY the variation profile and test materials - no information about other variations or previous results.

**For each persona variation (1-10):**

1. **Launch Isolated Agent:**
   - Use Task tool to create completely separate agent instance
   - Provide the COMPLETE variation profile with all personal details, background, communication style, and survey voice
   - Include explicit instruction: "You are responding as this specific person in a customer preference survey. Answer naturally in your voice, using your language style and perspective. Do not reference other options or variations."
   - Provide testing materials in randomized order (different for each agent to prevent bias)
   - Present the 4 questions appropriate to the test type
   - Collect responses that reflect this person's unique voice and style

2. **Variation Profile Format for Sub-Agent:**
   ```
   You are participating in a customer preference survey. Please respond naturally as yourself.

   Your Profile:
   - Name & Age: [Specific details]
   - Location & Context: [Where you live, neighborhood vibe]
   - Work & Lifestyle: [Your job, daily routine, free time]
   - Your Habits: [Specific behavioral patterns with timing and context]
   - Your Personality: [How you approach decisions, what matters to you]
   - Your Voice: [Communication style, language patterns, typical expressions]
   - Background Story: [Your relevant personal history and experiences]

   Survey Instructions:
   - Review the options presented below in the order shown
   - Answer each question from your perspective
   - Use your natural language and communication style
   - There are no right or wrong answers - we want YOUR authentic opinion
   - Be specific about what appeals or doesn't appeal to you personally

   [Present testing materials in randomized order]
   [Ask 4 questions from framework]
   ```

3. **Document Response:**
   - Record exact variation number and profile summary
   - Capture all 4 answers verbatim, preserving language quirks and style
   - Note specific expressions, phrases, or cultural references used
   - Tag response style (brief/detailed/skeptical/enthusiastic/etc.)
   - Track vote counts
   - Identify unique insights that differ from other variations

4. **Maintain Running Results:**
   - Keep cumulative tally in memory during execution
   - Update vote counts after each variation completes
   - Track patterns emerging across variations
   - Note which response styles are more common in each persona type
   - Flag when variations show high consensus vs. split opinions

5. **Progress Tracking:**
   - Show progress: "Completed Variation 7/10 for Persona X..."
   - Report diversity: "5/7 variations chose Option 2, 2/7 chose Option 3"
   - Estimate remaining time
   - Report any anomalies (e.g., "Variation 8 showed unusually strong preference")
   - Highlight interesting response style variations

**Example Sub-Agent Prompts:**

**Variation 1 (Brief/Direct style):**
```
You are participating in a customer preference survey.

You are: Sarah, 28, from Aarhus. You work in retail management and play casino games on your commute (20 min each way). You like quick sessions, clear information, and no-nonsense communication. You're practical and don't have patience for marketing fluff.

Your communication style: Brief, direct, to-the-point. You say what you mean without elaboration.

[Test materials + questions]
```

**Variation 2 (Detailed/Explanatory style):**
```
You are participating in a customer preference survey.

You are: Lars, 32, from Odense. You're a software developer who enjoys analyzing odds and strategies. You play poker weekly with friends and occasionally try sports betting. You like understanding the "why" behind things and tend to overthink decisions.

Your communication style: Detailed and explanatory. You like to walk through your reasoning step-by-step and provide context for your choices.

[Test materials + questions]
```

**Variation 3 (Skeptical/Critical style):**
```
You are participating in a customer preference survey.

You are: Mette, 24, from Copenhagen. You're a marketing student who's skeptical of advertising and promotional language. You use betting apps casually but distrust anything that feels manipulative. You've had bad experiences with misleading offers.

Your communication style: Skeptical and critical. You call out what doesn't work and explain what makes you distrust certain approaches.

[Test materials + questions]
```

### Phase 5: Results Documentation

**Create timestamped results folder:**

```
results/YYYY-MM-DD_HH-MM-SS/
├── index.html                          # Interactive dashboard
├── summary.html                        # Executive summary
├── assets/
│   ├── styles.css                      # Styling
│   └── script.js                       # Interactive features
├── markdown/
│   ├── summary.md                      # Markdown summary
│   └── [persona]_[language/type].md   # Individual reports
├── [persona]-[variant].html            # Persona pages
└── README.md                           # Navigation guide
```

**Required Documentation Components:**

#### 1. Running Results Tracker (During Execution)
Maintain in-memory tally showing:
- Current test number (e.g., "Round 47/100")
- Vote distribution so far
- Leading options
- Emerging patterns

#### 2. Individual Test Logs
For each completed test, document the unique voice and perspective:
```markdown
## Test #47: [Base Persona] - Variation 7
**Profile:** Marcus, 26, Copenhagen (Vesterbro) - Junior graphic designer
**Response Style:** Thoughtful/Visual - Uses design terminology
**Timestamp:** 2025-11-03 14:23:15
**Materials Presented (Order):** [3, 1, 5, 2, 4, 6]

### Responses (captured verbatim):
**Q1 - Preference:** Choice: #3 ("[Option text]")
**Q2 - Reasoning:** "I think what really appeals to me here is the visual hierarchy - it's clear and doesn't feel cluttered. As someone who works with design daily, I appreciate when things are straightforward. It feels honest, you know? Not trying too hard."

**Q3 - Rejection:** Choice: #6 ("[Option text]")
**Reasoning:** "This one feels a bit desperate? Like it's screaming at me. The language is too pushy and makes me think they're trying to hide something. I'd scroll past this immediately."

**Q4 - Trust:** Choice: #1 ("[Option text]")
**Reasoning:** "Even though I didn't pick this as my favorite, I think this builds the most trust. It's professional and transparent about what you're getting."

### Voice Characteristics Observed:
- Uses design/visual terminology ("hierarchy", "cluttered")
- Casual but thoughtful language ("you know?")
- Values authenticity and transparency
- Skeptical of overly promotional language ("desperate", "screaming")
- Analytical approach with emotional grounding

### Insights:
- Preference ≠ Trust: Chose #3 for appeal but #1 for trust (gap pattern)
- Values clarity and visual design in messaging
- Rejects aggressive/pushy marketing tactics
- Decision influenced by professional design background
```

#### 3. Aggregate Results Tables
**By Testing Material:**
| Material | Total Votes (Q1) | % | Trust Votes (Q4) | % | Gap |
|----------|------------------|---|------------------|---|-----|
| Option 1 | 23/100 | 23% | 67/100 | 67% | +44% |
| Option 2 | 45/100 | 45% | 12/100 | 12% | -33% |

**By Persona (Base):**
| Persona | Top Preference | % | Top Secondary Metric | % |
|---------|---------------|---|-----------|---|
| [Persona 1] | Option 2 | 60% | Option 1 | 80% |
| [Persona 2] | Option 3 | 45% | Option 3 | 50% |

**By Variation (showing diversity within persona):**
| Persona | Variation Range | Notes |
|---------|----------------|-------|
| [Persona 1] | 7/10 picked same top choice | High consistency - strong signal |
| [Persona 2] | 5/10 split between two | More variation - nuanced preferences |

#### 4. Variation Diversity Analysis
Track how the 10 variations within each persona responded:

**Response Style Distribution:**
| Style | Count | Example Variation |
|-------|-------|------------------|
| Brief/Direct | 2/10 | Variation 1, 5 |
| Detailed/Explanatory | 3/10 | Variation 2, 7, 9 |
| Skeptical/Critical | 2/10 | Variation 3, 8 |
| Enthusiastic/Emotional | 1/10 | Variation 4 |
| Analytical/Comparative | 2/10 | Variation 6, 10 |

**Consensus vs. Diversity:**
```markdown
**High Consensus (8+ variations agree):**
- Indicates strong signal - this preference is robust across the persona
- Example: "8/10 variations of Casual Entertainer chose Option 3"
- Implication: High confidence in this finding

**Moderate Consensus (6-7 variations agree):**
- Clear preference but with notable exceptions
- Example: "6/10 chose Option 2, but skeptical communicators (Var 3, 8) chose Option 1"
- Implication: Preference depends on communication style within persona

**Split Opinion (4-6 variations per option):**
- Persona shows internal diversity on this dimension
- Example: "5/10 chose Option 1, 5/10 chose Option 4"
- Implication: May need to segment further or test both approaches

**High Diversity (no option gets >4 variations):**
- Weak signal - persona is not aligned on this test
- May indicate poor options or persona not well-defined for this test
- Requires deeper investigation
```

**Language & Cultural Patterns:**
Track unique expressions and communication styles:
- Danish expressions used: [List examples]
- Local references: [Copenhagen nightlife, Aarhus habits, etc.]
- Communication style variations: [Formal vs casual, emoji use, etc.]
- Technical vocabulary: [Industry-specific terms used]

#### 5. Qualitative Insights
Extract patterns from Q2 responses, preserving the diversity of voices:

**What Appeals (by response style):**
- **Direct communicators say:** "Clear", "Simple", "Gets to the point"
- **Detailed communicators say:** "I appreciate that this explains... and provides context for..."
- **Skeptical communicators say:** "At least this one doesn't try to manipulate me"
- **Enthusiastic communicators say:** "This just feels right! It's exciting and fun!"

**What Repels (common themes across styles):**
- Aggressive/pushy language (mentioned by 7/10 variations)
- Unclear or confusing messaging (mentioned by 5/10 variations)
- Perceived manipulation or hidden terms (mentioned by skeptical variations)
- Generic or boring copy (mentioned by enthusiastic variations)

**Trust Signals (across persona types):**
- Transparency and clarity (strong across all personas)
- Professional presentation (valued by analytical types)
- Authenticity and honesty (critical for skeptical types)
- Alignment with personal values (important for mission-driven personas)

**Persona-Specific Patterns:**
- [Persona 1]: Strong preference for [specific attribute], consistent across 8/10 variations
- [Persona 2]: Split between [attribute A] (detail-oriented variations) and [attribute B] (emotion-driven variations)
- [Persona 3]: Unique emphasis on [specific concern] regardless of communication style

#### 6. Strategic Recommendations
Based on results, provide actionable guidance using variation insights:

**Winner by Context:**
- **For Acquisition/Appeal:** [Option X] won preference (Q1) with 45% overall
  - Strongest with [Persona Type]: 8/10 variations chose this
  - Weakest with [Persona Type]: Only 3/10 variations chose this
  - Works best for: [Specific audience characteristics]

- **For Trust/Credibility:** [Option Y] won trust (Q4) with 67% overall
  - Universal appeal: Strong across all response styles
  - Note: Creates preference-trust gap (-22%) - may sacrifice appeal for credibility

**Persona-Specific Targeting:**
- **[Persona 1]**: Use [Option X] - High consensus (8/10) indicates robust preference
  - Resonates with: [Specific values/motivations from variations]
  - Avoid: [Option Z] - Rejected by skeptical variations who called it "pushy"

- **[Persona 2]**: Split strategy needed - Test both [Option A] and [Option B]
  - Detail-oriented variations (40%) prefer [Option A] for clarity
  - Emotion-driven variations (40%) prefer [Option B] for excitement
  - Consider: Dynamic messaging based on behavior signals

**Communication Style Insights:**
- **Brief/Direct communicators** (20% of audience): Prefer concise, clear messaging
  - Recommendation: Use [Option X] in mobile contexts where scan-reading is common

- **Detailed/Explanatory communicators** (30% of audience): Want context and reasoning
  - Recommendation: Use [Option Y] in long-form content or onboarding flows

- **Skeptical/Critical communicators** (20% of audience): Distrust promotional language
  - Recommendation: Use [Option Z] with transparent terms, avoid hype words

**A/B Test Priorities:**
1. **High Priority:** Test [Option X] vs [Option Y] for [Persona 1] - Clear preference signal
2. **Medium Priority:** Test [Option A] vs [Option B] for [Persona 2] - Split requires validation
3. **Low Priority:** [Option Z] - Weak signal across all variations, likely underperformer

**Risk Flags:**
- **[Option N]**: Rejected by 7/10 variations - "too pushy", "feels desperate"
- **[Option M]**: No strong preference (3/10 max) - too generic/forgettable
- **Gap Concerns**: [Option K] has 40% preference but only 15% trust - conversion risk

**Expected Impact (based on variation consensus):**
- **High Confidence (8+ variations agree):** These findings likely to replicate in real testing
- **Medium Confidence (6-7 variations agree):** Directionally correct, needs validation
- **Low Confidence (4-5 variations agree):** Requires real-world testing before decisions

**Recommended Next Steps:**
1. Implement [Option X] for [high consensus persona]
2. A/B test [Option A] vs [Option B] for [split persona]
3. Revise and retest [low-performing options]
4. Consider audience segmentation by communication style for dynamic messaging

### Phase 6: Output Generation

**Create Complete Documentation Package:**

#### HTML Dashboard (index.html)
- Interactive Chart.js visualizations
- Tabbed navigation (Overview, Methodology, Results by Persona, Recommendations)
- Summary statistics cards
- Links to detailed persona pages

#### Executive Summary (summary.html)
- Key findings with charts
- Strategic recommendations
- Business impact projections
- Navigation to detailed reports

#### Persona Pages ([persona]-[type].html)
- Individual persona analysis
- Variation diversity analysis
- Detailed results tables
- Charts showing preference vs trust gap
- Quotes from synthetic individuals
- Specific recommendations for that segment

#### Markdown Reports
- Complete markdown versions of all HTML reports
- Raw data tables
- Individual test logs
- Easy to read and version control

#### Navigation README
- Overview of all files
- Quick links to key findings
- How to interpret results
- Methodology explanation

## Usage Instructions

### Starting a New Simulation

**User provides:**
```
I want to test [6 taglines / 4 CTAs / 3 visual designs] with [all personas / specific personas].

Testing materials:
1. [Material 1]
2. [Material 2]
3. [Material 3]
...
```

**Agent responds with:**
```
I'll execute a synthetic simulation testing [X materials] across [Y personas].

This will involve:
- Generating 10 unique variations per persona
- Running [Z] total isolated tests
- Testing with 4-question framework
- Creating complete documentation package

Estimated time: [X] minutes
Proceed? (yes/no)
```

### During Execution

**Show progress updates with variation details:**
```
✓ Generated 10 unique variations for Casual Entertainer
  Sample profiles:
  - Variation 1: Sarah, 28 (brief/direct style) - Retail manager, Aarhus
  - Variation 2: Lars, 32 (detailed/explanatory) - Software developer, Odense
  - Variation 3: Mette, 24 (skeptical/critical) - Marketing student, Copenhagen
  [... 7 more unique individuals]

✓ Generated 10 unique variations for Sports Enthusiast
  [Similar profile samples]

⏳ Running isolated tests (each variation in separate agent)...

Progress: Casual Entertainer 6/10 variations completed
Emerging pattern:
- Brief/direct variations (3/3): All chose Option 3
- Detailed/explanatory variations (2/2): Split between Option 2 and 3
- Skeptical variation (1/1): Chose Option 1 - "only one that doesn't feel manipulative"

Current leaders:
- Preference: Option 3 (50% so far)
- Trust: Option 1 (67% so far)

⏳ Continuing...
```

### After Completion

**Provide summary with variation insights:**
```
✓ Simulation complete! 20 unique synthetic individuals tested across 2 personas.

📊 Results summary:
- Preference winner: [Option X] (45%)
  - High consensus in [Persona 1]: 8/10 variations chose this
  - Split in [Persona 2]: 5/10 chose Option X, 4/10 chose Option Y

- Trust winner: [Option Y] (82%)
  - Universal across all communication styles

- Variation diversity insights:
  - [Persona 1]: High consensus (80%) - strong signal
  - [Persona 2]: Moderate split - communication style matters

- Language patterns observed:
  - Direct communicators: "Clear", "Simple", "Gets to the point"
  - Skeptical communicators: "Not manipulative", "Honest", "Transparent"
  - Enthusiastic communicators: "Exciting!", "Feels right", "Love it"

📁 Documentation created:
results/2025-11-03_14-30-22/

🔗 Access results:
- Interactive Dashboard: [link with variation analysis]
- Executive Summary: [link]
- Individual Variation Reports: [links showing unique voices]

💡 Key insight: [Most important finding, including variation diversity implications]
Example: "Brief/direct communicators within Casual Entertainer persona strongly
prefer Option X (90%), while skeptical communicators prefer Option Y (70%).
Consider dynamic messaging based on user behavior signals."
```

## Advanced Features

### Variation Diversity Analysis
Track and report:
- Consensus within persona (all 10 variations agree)
- Split opinions (variations disagree)
- Outlier variations (1-2 variations differ from group)
- Implications for targeting precision

### Longitudinal Tracking
When running multiple simulations over time:
- Compare results across test runs
- Track how messaging evolution performs
- Identify consistent winners vs temporal trends
- Build performance history database

### Multi-Language Support
For international testing:
- Run same test materials in multiple languages
- Compare cultural response differences
- Identify translation issues
- Optimize per-market messaging

### Visual Asset Testing Extensions
For image/design testing:
- Describe visual elements in detail
- Test multiple variations (A/B/C/D)
- Capture specific element feedback (color, layout, imagery)
- Identify design patterns that work

## Quality Assurance

### Validation Checks
Before finalizing results:
- ✓ All test rounds completed
- ✓ No duplicate test IDs
- ✓ Vote counts sum correctly
- ✓ All personas represented equally
- ✓ Randomization confirmed (no position bias)
- ✓ Qualitative data captured for all rounds
- ✓ Charts render correctly
- ✓ All links functional

### Red Flags to Report
- Unanimous agreement (might indicate context pollution)
- Extreme outliers (1 variation radically different)
- Missing data (incomplete responses)
- Technical errors (chart rendering issues)

## Example Execution Flow

```
User: "I want to test 5 new CTA button texts with casual entertainers and sports enthusiasts"

Agent: "I'll run a synthetic simulation with:
- 2 personas (Casual Entertainer, Sports Enthusiast)
- 10 unique variations each = 20 unique synthetic individuals
  - Each variation will have distinct communication styles, backgrounds, and survey voices
  - Variations include: brief/direct, detailed/explanatory, skeptical/critical, enthusiastic, analytical styles
- 1 round per variation (isolated agents) = 20 total isolated tests
- 5 CTA options to evaluate

What are your 5 CTA texts to test?"

User: [Provides 5 CTAs]

Agent:
"Starting simulation...

Phase 1: Generating persona variations...
✓ Generated 10 unique variations for Casual Entertainer
  - Variation 1: Sarah (brief/direct) - Retail manager, Aarhus
  - Variation 2: Lars (detailed/explanatory) - Software dev, Odense
  - Variation 3: Mette (skeptical/critical) - Marketing student, Copenhagen
  - [...7 more unique individuals with distinct backgrounds...]

✓ Generated 10 unique variations for Sports Enthusiast
  - Variation 1: Thomas (enthusiastic) - Personal trainer, Copenhagen
  - Variation 2: Emma (analytical) - Data analyst, Aalborg
  - [...8 more unique individuals with distinct backgrounds...]

Phase 2: Running isolated tests (each in separate agent)...
⏳ Testing Casual Entertainer variations: 3/10 completed
  - Variation 1 (Sarah): Chose CTA #2 - "Clear and to the point"
  - Variation 2 (Lars): Chose CTA #3 - "I appreciate that it explains what happens next..."
  - Variation 3 (Mette): Chose CTA #1 - "Honestly, this is the only one that doesn't feel manipulative"

⏳ Current leader: CTA #2 (40% so far)

⏳ Testing Casual Entertainer: 10/10 complete
  Results: CTA #2 (6/10), CTA #1 (3/10), CTA #3 (1/10)
  Consensus: Moderate (60%) - Brief/direct and enthusiastic variations prefer CTA #2
  Skeptical variations prefer CTA #1

⏳ Testing Sports Enthusiast variations: 10/10 complete
  Results: CTA #4 (8/10), CTA #2 (2/10)
  Consensus: High (80%) - Strong preference across all communication styles

✓ All tests complete! 20/20 isolated agents finished.

Phase 3: Analyzing results...

📊 Overall Results:
- Preference Leader: CTA #4 "Join the Action" (40% overall, 80% Sports Enthusiasts)
- Trust Leader: CTA #1 "Secure Sign Up" (55% overall)
- Biggest Gap: Casual Entertainers - 30% prefer CTA #2, but 60% trust CTA #1

📁 Results saved to: results/2025-11-03_14-30-22/

🎯 Key Finding:
Casual Entertainers show variation diversity:
- Brief/direct communicators (40%) prefer CTA #2 "Start Playing Free" - simple and clear
- Skeptical communicators (30%) prefer CTA #1 "Secure Sign Up" - builds trust
- Detailed communicators split between options

Sports Enthusiasts show high consensus:
- 8/10 variations chose CTA #4 "Join the Action" - excitement and belonging
- Works across all communication styles for this persona

💡 Recommendation:
1. Use CTA #4 "Join the Action" for Sports Enthusiasts (high confidence)
2. A/B test CTA #1 vs CTA #2 for Casual Entertainers based on context:
   - Use CTA #2 for acquisition (quick engagement)
   - Use CTA #1 for high-value conversions (trust matters)
3. Consider dynamic CTAs based on user behavior signals (risk tolerance, engagement style)

📄 View detailed analysis with verbatim quotes and voice patterns in the full report."
```

## Continuous Improvement

After each simulation:
- Review for methodology improvements
- Note any persona variations that need refinement
- Update question frameworks based on learnings
- Enhance documentation templates
- Optimize visualization approaches

## Integration with Existing Skills

### Persona Skills (Required)
This skill orchestrates and uses persona skills from:
- **`persona-skills/` folder** - Contains all available persona profiles
- Load any personas from this folder
- Custom personas can be added by user
- Each persona should define clear demographic, behavioral, and psychographic characteristics

### Testing Methodology Skills (Optional but Recommended)
Can be used in conjunction with testing skills from:
- **`testing-skills/` folder** - Contains specialized testing methodologies
  - `tagline-testing-skill/` - For brand messaging
  - `cta-testing-skill/` - For call-to-action copy with context frameworks
  - `logo-testing-skill/` - For visual identity testing
  - Custom testing methodologies can be added following the same pattern

### How Integration Works:
1. **Load this orchestration skill** for simulation automation
2. **Reference specific testing skill** from `testing-skills/` for methodology details (optional)
3. **Load persona skills** from `persona-skills/` for variation generation
4. **Execute simulation** with appropriate question frameworks
5. **Generate documentation** using established patterns

**Example:**
```
Use orchestration-skills/synthetic-simulation-execution with
testing-skills/cta-testing-skill methodology to test 4 CTAs
across 3 personas from persona-skills/ folder.

CTAs:
1. "Start Playing Free"
2. "Join Now"
3. "Claim Bonus"
4. "Get Started"

Personas: [Any 3 personas from persona-skills/ folder]
Context: [Specify test context from testing skill]
```

## Success Criteria

A successful simulation delivers:
1. ✅ Complete isolation (no context pollution)
2. ✅ Sufficient sample size (minimum 10 per variation)
3. ✅ Rich qualitative insights (quotes, reasoning)
4. ✅ Clear quantitative results (vote counts, percentages)
5. ✅ Actionable recommendations (what to do next)
6. ✅ Professional documentation (ready to share with stakeholders)
7. ✅ Reproducible methodology (can be repeated)
8. ✅ Variation diversity tracked (understand consensus vs disagreement)

---

**Skill Version:** 3.0.0
**Created:** November 2025
**Updated:** November 2025 - Enhanced variation generation with unique survey voices and communication styles
**Key Changes in v3.0:**
- Each of 10 variations now has distinct communication style and survey response voice
- Variations respond as unique individuals with made-up contextually relevant information
- Added 10 response style archetypes (brief/direct, detailed/explanatory, skeptical/critical, etc.)
- Enhanced isolation protocol with complete variation profiles passed to sub-agents
- Results now include variation diversity analysis and communication style insights
- Consensus tracking (high/moderate/split) for confidence scoring
- Language and cultural pattern analysis in documentation

**For:** General purpose synthetic user testing (optimized for Yes.com)
**License:** Proprietary - Yes.com exclusive use
