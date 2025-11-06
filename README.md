# Skills Library

A collection of AI skills for synthetic user testing and evaluation of gambling platform content, features, and user experiences, specifically designed for the Danish market.

## Folder Structure

```
skills-library/
├── persona-skills/          # User persona profiles
├── testing-skills/          # Testing methodologies (taglines, CTAs, logos)
├── orchestration-skills/    # Meta-skills for running simulations
└── results/                 # Test results and documentation
```

## Table of Contents

- [Overview](#overview)
- [Target Audience](#target-audience)
- [Available Skills](#available-skills)
  - [User Persona Skills](#user-persona-skills)
    - [1. The Casual Entertainer](#1-the-casual-entertainer-casual-entertainer)
    - [2. The Sports Enthusiast](#2-the-sports-enthusiast-sports-enthusiast)
    - [3. The Casino Explorer](#3-the-casino-explorer-casino-explorer)
    - [4. The Trust Seeker](#4-the-trust-seeker-trust-seeker)
    - [5. The Cross-Entertainment Engager](#5-the-cross-entertainment-engager-cross-entertainment-engager)
  - [Orchestration Skills](#orchestration-skills)
    - [6. Synthetic Simulation Execution](#6-synthetic-simulation-execution-synthetic-simulation-execution)
  - [Testing Methodology Skills](#testing-methodology-skills)
    - [7. CTA Testing](#7-cta-testing-cta-testing-skill)
    - [8. Tagline Testing](#8-tagline-testing-tagline-testing-skill)
    - [9. Logo Testing](#9-logo-testing-logo-testing-skill)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Integration](#integration)
- [Notes on Synthetic Testing](#notes-on-synthetic-testing)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains modular skills that enable Claude to adopt specific personas and testing methodologies for evaluating gambling platform materials. Each skill provides structured prompts, context filtering guidelines, and response principles to ensure consistent, authentic synthetic testing.

All personas are grounded in real Danish gambling market data (2024-2025), regulatory environment, and user behavior patterns to provide realistic, actionable insights for testing and validation.

## Target Audience

- **Primary**: Young adults (18–35) in Denmark
- **Secondary**: Adults 35–50 seeking safe, trusted brands
- **Behavior**: Mobile-first, social-media native, blends betting with gaming/streaming; trust-oriented segments still value desktop/tablet use
- **Needs**: Fast, transparent, gamified entertainment with social features; safe deposits/withdrawals; clear T&Cs; Danish-language support; visible responsible gambling

## Available Skills

### User Persona Skills

#### 1. The Casual Entertainer (`casual-entertainer`)
**Profile:** Age 22-28, occasional bettor treating gambling as lighthearted mobile entertainment alongside TikTok and mobile games.

**Download:** [casual-entertainer.zip](https://github.com/Yes-Gaming/skills-library/raw/main/persona-skills/casual-entertainer/casual-entertainer.zip)

**Use Cases:**
- Testing quick-play features, instant-win formats, or casual gaming experiences
- Evaluating gamified reward systems, loyalty programs, or achievement mechanics
- Assessing mobile-first interfaces and fast-flow user experiences
- Getting feedback on slot games, lottery features, or simple sports betting
- Testing registration flows, deposit processes, or onboarding experiences
- Validating experiences for 18-28 demographic focused on entertainment

**Key Characteristics:**
- Values instant gratification, quick thrills, and zero friction
- Mobile-only mindset with near-zero tolerance for complexity
- Motivated by small wins, gamification, and social sharing moments
- Abandons immediately if experience feels slow, complex, or boring
- Competes with TikTok, streaming, and mobile games for attention
- Typical spend: DKK 50-200/month sporadically

#### 2. The Sports Enthusiast (`sports-enthusiast`)
**Profile:** Age 25-35, regular sports bettor with deep football knowledge who lives for live betting during matches.

**Download:** [sports-enthusiast.zip](https://github.com/Yes-Gaming/skills-library/raw/main/persona-skills/sports-enthusiast/sports-enthusiast.zip)

**Use Cases:**
- Testing sports betting features, live betting interfaces, or in-play functionality
- Evaluating market depth, odds displays, or betting slip complexity
- Assessing real-time statistics, live scores, or match tracking features
- Getting feedback on mobile betting UX during live matches
- Testing pre-match vs. live betting experiences
- Validating sports content, match previews, or statistical tools

**Key Characteristics:**
- Demands professional-grade speed and reliability (especially live betting)
- Frustrated by limited markets or shallow betting depth
- Motivated by proving sports knowledge through betting success
- Expects comprehensive statistics and real-time data
- Mobile-focused during matches but uses desktop for research
- Zero tolerance for technical issues during live matches
- Typical spend: DKK 500-1,500/month strategically

#### 3. The Casino Explorer (`casino-explorer`)
**Profile:** Age 20-30, variety-seeking casino player driven by visual quality, game discovery, and the thrill of exploring new slots and live dealer games.

**Download:** [casino-explorer.zip](https://github.com/Yes-Gaming/skills-library/raw/main/persona-skills/casino-explorer/casino-explorer.zip)

**Use Cases:**
- Testing slot games, game libraries, or game discovery features
- Evaluating game categorization, search, filtering, or recommendation systems
- Assessing visual quality, animations, themes, and game presentation
- Getting feedback on jackpot displays, progressive slots, or big win celebrations
- Testing live dealer games, game shows, or interactive casino experiences
- Validating personalized offers, promotions, or loyalty programs
- Evaluating payout processes, withdrawal speeds, or RTP transparency

**Key Characteristics:**
- Motivated by discovery, novelty, and visual excellence
- Needs excellent game discovery to navigate large libraries
- Responds strongly to beautiful, well-designed, themed games
- Frustrated by technical issues, slow loads, or poor performance
- Values transparency in RTPs and fair play
- Variety-seeker who gets bored easily without fresh content
- Typical spend: DKK 200-600/month across varied sessions

#### 4. The Trust Seeker (`trust-seeker`)
**Profile:** Age 40+, experienced but cautious gambler who values security, transparency, simplicity, and reliable customer service over innovation or flashy features.

**Download:** [trust-seeker.zip](https://github.com/Yes-Gaming/skills-library/raw/main/persona-skills/trust-seeker/trust-seeker.zip)

**Use Cases:**
- Testing trust signals, security features, or licensing information displays
- Evaluating terms and conditions clarity, bonus term transparency
- Assessing customer support experiences (live chat, email, phone)
- Getting feedback on desktop or tablet interfaces
- Testing simplified UX, traditional betting formats, or classic games
- Validating responsible gambling tools and messaging
- Evaluating loyalty programs for steady, long-term players

**Key Characteristics:**
- Security and protection above all else
- Skeptical of "too good to be true" offers or flashy gimmicks
- Appreciates clear, straightforward, transparent communication
- Values human customer support (phone, email) over chatbots
- Prefers desktop/tablet (40-50% of usage) but uses mobile too
- Loyal once trust is earned but impossible to win back if betrayed
- Typical spend: DKK 300-800/month consistently

#### 5. The Cross-Entertainment Engager (`cross-entertainment-engager`)
**Profile:** Age 18-40, digitally-native multitasker who blends sports watching, esports, casino gaming, and social interaction simultaneously, demanding unified platform experiences.

**Download:** [cross-entertainment-engager.zip](https://github.com/Yes-Gaming/skills-library/raw/main/persona-skills/cross-entertainment-engager/cross-entertainment-engager.zip)

**Use Cases:**
- Testing unified platform experiences that blend multiple entertainment types
- Evaluating social features (chat, sharing, community feeds, friend activity)
- Assessing in-app streaming, multi-view experiences, or integrated video content
- Getting feedback on prediction contests, free-to-play pools, or community challenges
- Testing multi-device synchronization and cross-platform consistency
- Validating shareable bet-slips, social proof features, or collaborative betting
- Evaluating experiences for highly engaged, daily active users

**Key Characteristics:**
- Needs integrated, unified experiences above everything else
- Motivated by social features, community, and shared experiences
- Frustrated by fragmentation, silos, and app-switching requirements
- Expects flawless multi-device synchronization
- Values variety across entertainment types (sports, casino, esports, novelty)
- Wants personalization and to feel recognized by the platform
- Power user who drives organic growth through social amplification
- Typical spend: DKK 300-600/month with high engagement depth

### Orchestration Skills

#### 6. Synthetic Simulation Execution (`synthetic-simulation-execution`)
**Methodology:** Comprehensive orchestration skill for running isolated synthetic user testing with unique persona variations and complete documentation. Works with any personas and test types.

**Download:** [synthetic-simulation-execution.zip](https://github.com/Yes-Gaming/skills-library/raw/main/orchestration-skills/synthetic-simulation-execution/synthetic-simulation-execution.zip)

**Version:** 3.0.0 - Enhanced with unique survey voices and communication styles

**Use Cases:**
- Running large-scale synthetic simulations (100+ isolated tests)
- Testing any user-facing material (taglines, CTAs, visuals, UX flows, features)
- Generating 10 unique variations per persona with distinct communication styles
- Creating professional HTML/Markdown documentation with interactive charts
- Multi-persona comparative analysis with strategic recommendations
- A/B testing prioritization and business impact projections
- Variation diversity analysis to understand consensus vs. split opinions

**Key Innovation - Unique Persona Variations:**

Unlike traditional testing that produces identical responses, v3.0 generates **10 unique variations** for each base persona:
- Each variation is a fully-realized synthetic individual with unique background, communication style, and perspective
- Responds in their own voice using contextually relevant language and cultural references
- Brings authentic survey response diversity (brief/direct, detailed/explanatory, skeptical/critical, enthusiastic, analytical, etc.)
- Provides realistic preference distribution rather than artificial consensus

**What This Delivers:**
- **High consensus (8-10 variations agree)** = Strong, actionable insights with high confidence
- **Moderate consensus (6-7 variations agree)** = Directional insights requiring validation
- **Split opinions (4-6 variations per option)** = Need for audience segmentation or further testing
- **Communication style patterns** = Opportunities for dynamic messaging based on user behavior

**Key Features:**
- **Complete Context Isolation:** Each test runs in separate agent instance (no pollution)
- **Unique Variation Generation:** 10 distinct survey response styles per persona (not template responses)
- **Persona Agnostic:** Works with any personas from `persona-skills/` folder or custom personas
- **Test Type Agnostic:** Adapts to any testing subject (taglines, CTAs, visuals, UX flows, features, etc.)
- **Flexible Integration:** References specialized methodologies from `testing-skills/` folder when needed
- **Variation Diversity Analysis:** Tracks consensus levels and communication style patterns
- **Running Documentation:** Tracks results incrementally during execution with voice characteristics
- **Professional Output:** Interactive HTML dashboards with Chart.js visualizations
- **Strategic Recommendations:** Actionable insights by persona, communication style, and confidence level
- **Timestamped Results:** Each simulation saves to dated subfolder
- **Markdown + HTML:** Complete documentation in both formats

**What Gets Generated:**
```
results/YYYY-MM-DD_HH-MM-SS/
├── index.html              # Interactive dashboard
├── summary.html            # Executive summary
├── [persona]-[type].html   # Individual persona pages
├── assets/
│   ├── styles.css
│   └── script.js
└── markdown/
    ├── summary.md
    └── [persona]_results.md
```

**Testing Capabilities:**
- **Taglines** - Brand messaging and positioning
- **CTAs** - Call-to-action button copy
- **Visual Assets** - Images, designs, layouts
- **UX Flows** - User experience sequences
- **Product Features** - Functionality descriptions
- **Landing Pages** - Complete page concepts
- **Any user-facing materials**

**Example Results:**
- `results/2025-11-02_17-26-36/` - Complete tagline testing with 100 isolated tests
- `results/2025-11-04_20-46-08/` - Complete logo testing (Phase 1 + Phase 2) with 150 tests
  - Phase 1: 50 personas tested 7 logos individually
  - Phase 2A: 50 personas compared all 7 logos side-by-side
  - Phase 2B: 50 personas tested top 3 finalists head-to-head
  - Final winner: Logo 2 (72% final vote, 9/10 confidence)
  - Trust Seeker anomaly identified and mitigation strategy provided
  - Interactive HTML reports and comprehensive markdown analysis
- `results/2025-11-06_COLOR_COMPARISON_STAKEHOLDER_REPORT.html` - **Complete 9-color app icon comparison (225 interviews)**
  - **Winner: PURPLE (4.24/5)** - Universal appeal with zero trade-offs
  - Comprehensive testing: Yellow, Red, Blue, Green, Black, Orange, Purple, Pink, Golden
  - Rankings: Purple (4.24/5), Black (4.00/5), Golden (4.00/5), Orange (3.6/5), Green (3.5/5), Yellow (3.4/5), Blue (3.2/5)
  - **Rejected: Pink (2.9/5), Red (2.6/5)** - catastrophic trust failures
  - Critical insight: Only 5 colors achieve acceptable ratings with Trust Seekers (40+, highest LTV)
  - Trust vs Excitement matrix reveals Purple as only "sweet spot" color
  - Complete strategic decision framework with alternatives for different business strategies
  - Professional HTML report with visualizations and demographic analysis
- `results/2025-11-06_yellow-icon-testing/` - Yellow app icon background testing with 25 personas
  - Isolated interviews across all 5 persona types (5 each)
  - Overall rating: 3.4/5 with significant demographic variation
  - Critical finding: Trust Seekers (40+) rated yellow only 2.5/5
  - Excellent visibility (10/10) vs poor trust perception (3/10) trade-off
  - Strategic recommendations for young vs high-value demographics
  - Complete HTML stakeholder report with visualizations

### Testing Methodology Skills

#### 7. CTA Testing (`cta-testing-skill`)
**Methodology:** Systematic framework for testing call-to-action (CTA) copy and button text with synthetic personas, focusing on conversion optimization.

**Download:** [cta-testing-skill.zip](https://github.com/Yes-Gaming/skills-library/raw/main/testing-skills/cta-testing-skill/cta-testing-skill.zip)

**Use Cases:**
- Running A/B or A/B/C CTA button text comparisons
- Optimizing landing page CTAs, registration flows, deposit prompts
- Testing primary vs secondary action copy
- Evaluating conversion messaging across personas
- Testing urgency-driven vs value-driven CTAs
- Multi-context CTA optimization (landing page, email, in-app)

**Key Features:**
- **Context-Specific Testing:** CTAs tested in realistic usage scenarios
- **4-Question Framework:** Action intent, motivation, friction, value perception
- **Intent-to-Value Analysis:** Identifies clicks vs conversion gaps
- **Friction Detection:** Surfaces conversion barriers and hesitation factors
- **Context Versatility Scoring:** Universal vs specialized CTA recommendations
- **Device-Specific Testing:** Mobile vs desktop optimization
- **A/B Testing Roadmap:** Prioritized tests with hypotheses and metrics

**Key Metrics:**
- Action Intent (who would click)
- Motivation Drivers (why they'd click)
- Friction Coefficient (what stops them)
- Value Perception (what converts)

**Contexts Covered:**
- Landing page hero CTAs
- Registration flow CTAs
- First deposit prompts
- Promotional email CTAs
- Re-engagement messaging
- Mobile in-app CTAs

**Note:** Works seamlessly with `synthetic-simulation-execution` for automated large-scale CTA testing.

#### 8. Tagline Testing (`tagline-testing-skill`)
**Methodology:** Systematic framework for testing taglines and brand messaging with synthetic personas.

**Download:** [tagline-testing-skill.zip](https://github.com/Yes-Gaming/skills-library/raw/main/testing-skills/tagline-testing-skill/tagline-testing-skill.zip)

**Use Cases:**
- Running A/B or A/B/C tagline comparisons
- Testing brand lock-ups (brand name + tagline combinations)
- Evaluating messaging across different personas
- Gathering quantitative preference data with qualitative context
- Controlling for order bias and presentation effects

**Key Features:**
- Structured 10-round testing protocol (adjustable)
- Order randomization to prevent bias
- Mix of forced-choice and open-ended questions
- Quantitative and qualitative analysis framework
- Statistical validity guidelines for synthetic testing

**Note:** The `synthetic-simulation-execution` skill supersedes this for large-scale testing with automated documentation.

#### 9. Logo Testing (`logo-testing-skill`)
**Methodology:** Systematic methodology for testing logos, brand marks, and visual identity assets with synthetic personas using multimodal AI analysis.

**Download:** [logo-testing-skill.zip](https://github.com/Yes-Gaming/skills-library/raw/main/testing-skills/logo-testing-skill/logo-testing-skill.zip)

**Use Cases:**
- Evaluating multiple logo design concepts
- Making rebrand vs. iteration decisions
- Testing logo variations (colors, layouts, sizes)
- Assessing app icon effectiveness
- Understanding brand perception through visual analysis
- Comparing competitive differentiation
- Testing logo scalability (favicon to billboard)
- Validating visual identity before launch
- **NEW:** Testing logos across demographic segments (males/females, age groups, 50:50 splits)
- **NEW:** Comparing multiple logo options across different demographics in comparable settings

**Key Features:**
- **Multimodal AI Analysis:** Leverages Claude's vision capabilities to analyze actual image files
- **Preference-Trust-Memory Triangle:** Three key metrics for comprehensive logo evaluation
- **6-Question Framework:** First impression, visual elements, brand perception, trust/quality, recognition, context fit
- **Context-Specific Testing:** App icon, website header, favicon, social media, competitive landscape
- **Visual Element Analysis:** Colors, shapes, symbols, typography, attention hierarchy
- **Brand Perception Assessment:** Intended vs. actual positioning insights
- **Critical Trust Focus:** Especially important for gambling platforms (Q4 is most critical)
- **NEW: Demographic Testing Methodologies:**
  - Single logo across demographics (10-question framework)
  - Multiple logos demographic comparison (15-question framework)
  - Gender preference patterns and trust signal variations
  - Age/generational design language differences
  - Context-demographic performance matrices

**Key Metrics:**
- **Preference (Q1):** First impression appeal (3-5 second reaction)
- **Trust (Q4):** Professional, trustworthy perception ⭐ MOST CRITICAL
- **Memory (Q5):** Recognition and recall strength
- **NEW: Demographic Alignment:** Logo performance across gender, age, and audience segments

**Multimodal Capabilities:**
- ✅ View actual image files (PNG, JPG)
- ✅ Analyze visual elements (colors, shapes, typography)
- ✅ Professional design critique
- ✅ Simulate contexts (app store, website, competitive)
- ✅ Comparative side-by-side evaluation
- ✅ Cultural awareness (symbol meanings, color associations)

**Testing Contexts:**
- App store icon ⭐ CRITICAL (must work at 60-120px)
- Website header (desktop/mobile)
- Favicon (16x16 or 32x32 pixels)
- Social media profile (circular crop)
- Competitive landscape (side-by-side with competitors)

**Demographic Testing Configurations:**
- **Males only:** Identify male-specific visual preferences and trust signals
- **Females only:** Understand female-targeted design effectiveness
- **50:50 gender split:** Balanced demographic validation
- **As per audience demographics:** Custom demographic distributions
- **Age segmentation:** 18-30, 31-45, 46-55+ generational testing
- **Cross-demographic analysis:** Identify universal appeal vs. polarizing elements

**What Demographic Testing Reveals:**
- Gender preference patterns (colors, shapes, symbols)
- Age-based trust signal variations (modern vs. traditional)
- Perceived demographic targeting vs. actual appeal
- Context effectiveness differences by segment
- Preference-trust gaps by demographic
- High-value segment performance (critical for ROI)
- Strategic segmentation opportunities

**Example Outputs:**
- `example_test_output.md` - Complete single-persona logo test
- `example_demographic_single_logo.md` - Single logo tested across demographics (27 pages)
- `example_demographic_multiple_logos.md` - Multiple logos compared across demographics (40 pages)
- `results/2025-11-04_20-46-08/` - Real-world complete logo testing project:
  - 150 synthetic user tests across 3 testing phases
  - 7 logo variations evaluated (winnowed to top 3, then final winner)
  - Complete demographic analysis with Trust Seeker (40+) anomaly discovery
  - Professional HTML reports and comprehensive strategic recommendations
  - Final decision: Logo 2 selected with 72% preference and 9/10 confidence

**Critical for Gambling:** Trust (Q4) is the most important metric because users deposit real money and credibility drives conversion. Older demographics (40+) prioritize trust over "cool" visual appeal and represent highest lifetime value users.

**Note:** Works seamlessly with `synthetic-simulation-execution` for automated large-scale logo testing with complete visual analysis documentation.

## Installation

To add a skill to Claude:

1. Click the download link for the skill you want to use
2. Save the `.zip` file to your computer
3. In Claude, go to Settings > Skills
4. Click "Add Skill" and upload the `.zip` file
5. The skill will now be available in your Claude interface

## How to Use

Each skill includes:

1. **SKILL.md** - Main skill definition with activation criteria and response principles
2. **references/** - Supporting materials like detailed persona profiles or methodology guides

### Basic Usage Pattern

1. **Load the appropriate skill** based on your testing needs
2. **Provide context** about what you're testing (copy, features, journeys)
3. **Ask targeted questions** to the persona or apply the testing methodology
4. **Receive authentic responses** from the persona's perspective
5. **Iterate and refine** based on feedback

### Context Filtering

All persona skills include guidelines for filtering what information to provide:

**Include:**
- Direct questions or materials being tested
- User-facing content and experiences
- Information the persona would naturally know

**Exclude:**
- Internal business strategy or rationale
- Technical implementation details
- Leading information that biases responses
- Testing methodology exposure

## Integration

Skills are organized into three categories and can be used individually or in combination:

**Persona Skills** (`persona-skills/` folder)
- Use for qualitative feedback and authentic user perspectives
- Can be combined to test how different user segments respond to the same materials
- Works with any testing methodology

**Testing Skills** (`testing-skills/` folder)
- Specialized methodologies for specific test types
- Provides question frameworks, contexts, and best practices
- Can be used standalone or with orchestration skill

**Orchestration Skills** (`orchestration-skills/` folder)
- Meta-skills that coordinate personas and testing methodologies
- `synthetic-simulation-execution` automates large-scale isolated testing
- Generates professional documentation and visualizations

**Integration Pattern:**
```
orchestration-skills/synthetic-simulation-execution
  └─ Uses personas from: persona-skills/
  └─ Uses methodologies from: testing-skills/ (optional)
  └─ Generates results in: results/
```

## Notes on Synthetic Testing

These skills provide synthetic user testing capabilities that are valuable for:
- Informing decisions and narrowing options
- Identifying potential issues before real testing
- Generating hypotheses for user research
- Rapid iteration and exploration
- Understanding different segment perspectives simultaneously

**Important:** This is not a replacement for actual user testing with real people. Use these skills to supplement and inform your research, not replace it.

### Danish Market Grounding (2024-2025 Data)

All personas are based on:
- Real Danish gambling market data and trends
- Spillemyndigheden regulatory requirements
- Actual user behavior patterns (mobile usage, session patterns, demographics)
- Danish consumer preferences and expectations
- Market growth patterns and segment characteristics

## Contributing

To add new skills to this library:

1. Create a new directory with a descriptive name
2. Include a `SKILL.md` file with the skill definition
3. Add any supporting materials in a `references/` subdirectory
4. Follow the established format for consistency
5. Ground personas in real market data and research
6. Update this README with the new skill details

## Archived Personas

Previous versions of personas have been moved to the `/archived` folder for reference. The current skills represent a complete redesign grounded in 2024-2025 Danish market data and free from platform-specific bias.

## License

These skills are proprietary and licensed exclusively for use by Yes.com and related business purposes. Unauthorized use, reproduction, or distribution is prohibited.

Copyright © Yes.com. All rights reserved.
