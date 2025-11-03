# Skills Library

A collection of AI skills for synthetic user testing and evaluation of gambling platform content, features, and user experiences, specifically designed for the Danish market.

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
  - [Testing Methodology Skills](#testing-methodology-skills)
    - [6. Tagline Testing](#6-tagline-testing-tagline-testing-skill)
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

**Download:** [casual-entertainer.zip](https://github.com/Yes-Gaming/skills-library/raw/main/casual-entertainer/casual-entertainer.zip)

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

**Download:** [sports-enthusiast.zip](https://github.com/Yes-Gaming/skills-library/raw/main/sports-enthusiast/sports-enthusiast.zip)

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

**Download:** [casino-explorer.zip](https://github.com/Yes-Gaming/skills-library/raw/main/casino-explorer/casino-explorer.zip)

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

**Download:** [trust-seeker.zip](https://github.com/Yes-Gaming/skills-library/raw/main/trust-seeker/trust-seeker.zip)

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

**Download:** [cross-entertainment-engager.zip](https://github.com/Yes-Gaming/skills-library/raw/main/cross-entertainment-engager/cross-entertainment-engager.zip)

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

### Testing Methodology Skills

#### 6. Synthetic Simulation Execution (`synthetic-simulation-execution`)
**Methodology:** Comprehensive meta-skill for orchestrating isolated synthetic user testing with persona variations and complete documentation.

**Download:** [synthetic-simulation-execution.zip](https://github.com/Yes-Gaming/skills-library/raw/main/synthetic-simulation-execution/synthetic-simulation-execution.zip)

**Use Cases:**
- Running large-scale synthetic simulations (100+ isolated tests)
- Testing any user-facing material (taglines, CTAs, visuals, UX flows, features)
- Generating 10 unique variations per persona for diversity analysis
- Creating professional HTML/Markdown documentation with interactive charts
- Multi-persona comparative analysis with strategic recommendations
- A/B testing prioritization and business impact projections

**Key Features:**
- **Complete Context Isolation:** Each test runs in separate agent instance (no pollution)
- **Persona Variation Generation:** Creates 10 unique individuals per base persona
- **Flexible Testing Framework:** Adapts to taglines, CTAs, visuals, UX flows, features, etc.
- **Running Documentation:** Tracks results incrementally during execution
- **Professional Output:** Interactive HTML dashboards with Chart.js visualizations
- **Strategic Recommendations:** Actionable insights by channel, demographic, and persona
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
See `results/2025-11-02_17-26-36/` for complete tagline testing example with:
- 100 isolated tests across 5 personas
- Interactive charts showing preference vs trust gaps
- Strategic recommendations by use case
- Individual persona deep-dives with charts

#### 7. Tagline Testing (`tagline-testing-skill`)
**Methodology:** Systematic framework for testing taglines and brand messaging with synthetic personas.

**Download:** [tagline-testing-skill.zip](https://github.com/Yes-Gaming/skills-library/raw/main/tagline-testing-skill/tagline-testing-skill.zip)

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

Skills can be used individually or in combination:

- Use **persona skills** for qualitative feedback and authentic user perspectives
- Use **tagline testing** methodology with any persona skill for structured preference testing
- Combine multiple persona skills to test how different user segments respond to the same materials
- Layer personas to understand cross-segment appeal and optimization opportunities

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
