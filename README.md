# Skills Library

A collection of AI skills for synthetic user testing and evaluation of gambling platform content, features, and user experiences.

## Overview

This repository contains modular skills that enable Claude to adopt specific personas and testing methodologies for evaluating gambling platform materials. Each skill provides structured prompts, context filtering guidelines, and response principles to ensure consistent, authentic synthetic testing.

## Available Skills

### User Persona Skills

#### 1. Recreational Spender (`recreational-spender`)
**Persona:** "Casual Kasper" - A 28-year-old recreational bettor representing the core casual gambling demographic.

**Download:** [recreational-spender.zip](https://github.com/Yes-Gaming/skills-library/raw/main/recreational-spender/recreational-spender.zip)

**Use Cases:**
- Testing copy, content, and messaging for gambling platforms
- Evaluating feature designs and user journeys
- Getting feedback on mobile experiences
- Assessing social and gamification features
- Validating "fun-first" positioning

**Key Characteristics:**
- Values mobile-first experiences and quick entertainment
- Motivated by social sharing and casual fun over serious gambling
- Abandons easily when faced with friction or complexity
- Prefers entertainment focus over "too serious" messaging

#### 2. Mobile Gamer-Turned Bettor (`mobile-gamer-bettor`)
**Persona:** "Mobile Mette" - A 22-year-old Gen-Z mobile gamer who transitioned into betting.

**Download:** [mobile-gamer-bettor.zip](https://github.com/Yes-Gaming/skills-library/raw/main/mobile-gamer-bettor/mobile-gamer-bettor.zip)

**Use Cases:**
- Testing mobile-first features and UI/UX
- Evaluating gamification elements (badges, levels, leaderboards)
- Assessing social features and sharing functionality
- Getting feedback on push notifications and engagement mechanics
- Testing video-first or short-form content
- Validating experiences for Gen-Z audiences

**Key Characteristics:**
- Expects mobile gaming standards in betting apps
- Values speed, social features, and constant novelty
- Quick to flag boredom or lack of interactivity
- Compares experiences to mobile gaming benchmarks
- Abandons fast if content isn't snackable or experiences are slow

### Testing Methodology Skills

#### 3. Tagline Testing (`tagline-testing-skill`)
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

## Notes on Synthetic Testing

These skills provide synthetic user testing capabilities that are valuable for:
- Informing decisions and narrowing options
- Identifying potential issues before real testing
- Generating hypotheses for user research
- Rapid iteration and exploration

**Important:** This is not a replacement for actual user testing with real people. Use these skills to supplement and inform your research, not replace it.

## Contributing

To add new skills to this library:

1. Create a new directory with a descriptive name
2. Include a `SKILL.md` file with the skill definition
3. Add any supporting materials in a `references/` subdirectory
4. Follow the established format for consistency
5. Update this README with the new skill details

## License

[Add license information as appropriate]
