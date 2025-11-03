# Synthetic Simulation Execution Skill

## Purpose
Execute comprehensive synthetic user testing by generating multiple isolated persona variations and running systematic tests on provided materials (taglines, CTAs, visual assets, etc.) with complete documentation and results reporting.

## Core Principles

### 1. Context Isolation
- Each test round must be completely independent
- No memory or context pollution between rounds
- Fresh perspective for every synthetic person
- Use separate agent instances for true isolation

### 2. Persona Variation Generation
- Load base persona from existing skills library
- Generate 10 unique variations of each base persona
- Each variation should have:
  - Same core characteristics and motivations
  - Different specific background details
  - Unique personal context
  - Distinct expression style
  - Individual demographic nuances (within persona range)

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
   - Identify which base personas from skills library
   - Available personas:
     - `casual-entertainer` (22-28, entertainment-focused)
     - `casino-explorer` (20-30, variety-seeking)
     - `sports-enthusiast` (25-35, betting-focused)
     - `trust-seeker` (40+, security-conscious)
     - `cross-entertainment-engager` (18-40, integrated experience)
   - User can select subset or all personas

4. **Test Parameters:**
   - Number of rounds per persona variation (default: 10)
   - Total tests = (# personas) × (10 variations) × (# rounds)
   - Confirm total test count with user

### Phase 2: Persona Variation Generation

**For each selected base persona:**

Generate 10 unique synthetic individuals by varying:

**Demographic Details:**
- Specific age within range (e.g., 24 vs 27)
- Geographic location
- Occupation/profession
- Income bracket (within persona's typical range)
- Education level
- Relationship status

**Behavioral Context:**
- Gambling frequency (within persona's pattern)
- Favorite games/sports
- Typical bet sizes
- Device preferences (phone model, OS)
- Time of day preferences

**Psychographic Nuances:**
- Risk tolerance variations
- Social vs solo play preferences
- Motivation emphasis (fun vs profit vs social)
- Tech savviness level
- Brand loyalty tendencies

**Personal Background:**
- How they discovered gambling
- Past positive/negative experiences
- Current gambling goals
- Biggest concerns or priorities

**Example Variation Template:**
```
Base Persona: Casual Entertainer
Variation #3:
- Name: "Emma, 24"
- Location: Copenhagen
- Occupation: Marketing coordinator
- Income: 35,000 DKK/month
- Device: iPhone 13
- Gambling: 2-3 times/month, slots and live casino
- Motivation: "I play when I'm bored on weekends, not about winning big"
- Concern: "Don't want to spend more than 200 DKK per session"
- Discovery: "Saw ads on Instagram, tried it during COVID lockdown"
```

### Phase 3: Question Framework Design

**Adapt questions based on testing subject type:**

#### For Taglines/Messaging:
1. **Q1 (Preference):** "Which [tagline/message] would you most likely click on?"
2. **Q2 (Reasoning):** "Why did you choose that one?"
3. **Q3 (Rejection):** "Which would you least likely click on and why?"
4. **Q4 (Trust):** "Which suggests a trustworthy, premium [platform/product]?"

#### For CTAs:
1. **Q1 (Preference):** "Which call-to-action would you most likely tap/click?"
2. **Q2 (Reasoning):** "What about it makes you want to take action?"
3. **Q3 (Rejection):** "Which CTA would you ignore or distrust?"
4. **Q4 (Urgency):** "Which creates the strongest sense of urgency or value?"

#### For Visual Assets:
1. **Q1 (Preference):** "Which design/visual appeals to you most?"
2. **Q2 (Reasoning):** "What specific elements attract you?"
3. **Q3 (Rejection):** "Which design turns you off or feels wrong?"
4. **Q4 (Trust):** "Which looks most professional and trustworthy?"

#### For UX Flows:
1. **Q1 (Preference):** "Which flow feels most intuitive to you?"
2. **Q2 (Reasoning):** "What makes it easy or natural?"
3. **Q3 (Friction):** "Where do you feel confused or frustrated?"
4. **Q4 (Completion):** "Which flow would you most likely complete?"

#### For Product Features:
1. **Q1 (Value):** "Which feature would you use most often?"
2. **Q2 (Reasoning):** "Why does this feature matter to you?"
3. **Q3 (Rejection):** "Which feature seems unnecessary or annoying?"
4. **Q4 (Premium):** "Which feature would make you consider a premium subscription?"

### Phase 4: Test Execution

**For each test round:**

1. **Launch Isolated Agent:**
   - Use Task tool to create completely separate agent instance
   - Load ONE persona variation profile
   - Provide testing materials in randomized order
   - Ask all 4 questions
   - Collect responses

2. **Document Response:**
   - Record exact variation number
   - Capture all 4 answers verbatim
   - Note any interesting quotes or insights
   - Track vote counts

3. **Maintain Running Results:**
   - Keep cumulative tally in memory during execution
   - Update vote counts after each round
   - Track patterns emerging

4. **Progress Tracking:**
   - Show progress: "Completed 23/100 tests..."
   - Estimate remaining time
   - Report any anomalies or interesting patterns

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
For each completed test, document:
```markdown
## Test #47
**Persona:** Casual Entertainer - Variation 7 (Emma, 24, Copenhagen)
**Timestamp:** 2025-11-03 14:23:15
**Materials Presented (Order):** [3, 1, 5, 2, 4, 6]

### Responses:
**Q1:** Choice: #3 ("Watch & Play")
**Q2:** "I like that it's short and tells me I can do both things at once"
**Q3:** Choice: #6 ("Play Made Easy") - "Sounds boring and like it's for old people"
**Q4:** Choice: #1 ("Casino and Sports Made Easy") - "This one sounds legit and professional"

### Insights:
- Strong preference for brevity
- Rejects patronizing language
- Trust diverges from initial appeal
```

#### 3. Aggregate Results Tables
**By Testing Material:**
| Material | Total Votes (Q1) | % | Trust Votes (Q4) | % | Gap |
|----------|------------------|---|------------------|---|-----|
| Option 1 | 23/100 | 23% | 67/100 | 67% | +44% |
| Option 2 | 45/100 | 45% | 12/100 | 12% | -33% |

**By Persona (Base):**
| Persona | Top Preference | % | Top Trust | % |
|---------|---------------|---|-----------|---|
| Casual Entertainer | Option 2 | 60% | Option 1 | 80% |

**By Variation (showing diversity within persona):**
| Persona | Variation Range | Notes |
|---------|----------------|-------|
| Casual Entertainer | 7/10 picked same top choice | High consistency |
| Sports Enthusiast | 5/10 split between two | More variation |

#### 4. Qualitative Insights
Extract patterns from Q2 responses:
- **What Appeals:** Common themes from preference reasoning
- **What Repels:** Patterns in rejection reasoning
- **Trust Signals:** What builds credibility
- **Persona-Specific:** Unique patterns per persona type

#### 5. Strategic Recommendations
Based on results, provide:
- **Winner by Context:** Different choices for acquisition vs trust
- **Persona Targeting:** Best options per audience segment
- **A/B Test Priorities:** What to test in real world
- **Risk Flags:** What to avoid
- **Expected Impact:** Business metrics projections

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

**Show progress updates:**
```
✓ Generated 10 variations for Casual Entertainer
✓ Generated 10 variations for Sports Enthusiast
⏳ Running tests...

Progress: 34/100 tests completed
Current leaders:
- Preference: Option 3 (38%)
- Trust: Option 1 (76%)

⏳ Continuing...
```

### After Completion

**Provide summary:**
```
✓ Simulation complete! 100/100 tests finished.

📊 Results summary:
- Preference winner: [Option X] (45%)
- Trust winner: [Option Y] (82%)
- Largest gap: Casual Entertainer (60% preference vs 10% trust)

📁 Documentation created:
results/2025-11-03_14-30-22/

🔗 Access results:
- Interactive Dashboard: [link]
- Executive Summary: [link]
- Individual Persona Reports: [links]

💡 Key insight: [Most important finding]
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
- 10 variations each = 20 unique synthetic individuals
- 10 rounds per variation = 200 total isolated tests
- 5 CTA options to evaluate

What are your 5 CTA texts to test?"

User: [Provides 5 CTAs]

Agent:
"Starting simulation...

✓ Generated variations for Casual Entertainer (10)
✓ Generated variations for Sports Enthusiast (10)

Running isolated tests: 47/200 completed...
Leading CTA: 'Join Now & Play' (34%)

[Continues until 200/200]

✓ Complete! Results in results/2025-11-03_14-30-22/

Key Finding: Casual Entertainers prefer 'Start Playing Free' (62%)
but trust 'Secure Sign Up' most (81%). Sports Enthusiasts show
no gap - 'Join the Action' wins both preference (73%) and trust (70%).

Recommendation: Use different CTAs for different audience segments."
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
This skill orchestrates and uses:
- `casual-entertainer` skill for persona profiles
- `casino-explorer` skill for persona profiles
- `sports-enthusiast` skill for persona profiles
- `trust-seeker` skill for persona profiles
- `cross-entertainment-engager` skill for persona profiles

### Testing Methodology Skills (Optional but Recommended)
Can be used in conjunction with:
- `tagline-testing-skill` - For detailed tagline testing methodology
- `cta-testing-skill` - For detailed CTA testing methodology with context frameworks
- Results documentation patterns from previous research

### How Integration Works:
1. **Load this meta-skill** for orchestration and automation
2. **Reference specific testing skill** (tagline-testing or cta-testing) for methodology details
3. **Load persona skills** as needed for variation generation
4. **Execute simulation** with appropriate question frameworks
5. **Generate documentation** using established patterns

**Example:**
```
Use synthetic-simulation-execution skill with cta-testing methodology
to test 4 CTAs across 3 personas in landing page context.

CTAs:
1. "Start Playing Free"
2. "Join Now"
3. "Claim Bonus"
4. "Get Started"

Personas: Casual Entertainer, Sports Enthusiast, Trust Seeker
Context: Landing page hero, mobile, new visitor
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

**Skill Version:** 1.0.0
**Created:** November 2025
**For:** Yes.com gambling platform testing
**License:** Proprietary - Yes.com exclusive use
