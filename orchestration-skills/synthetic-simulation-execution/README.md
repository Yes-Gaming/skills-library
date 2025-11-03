# 🧪 Synthetic Simulation Execution Skill

**A comprehensive meta-skill for orchestrating isolated synthetic user testing with persona variations and complete documentation.**

## 📋 Overview

This skill enables you to run systematic user testing simulations by:
- Loading base personas from the skills library
- Generating 10 unique variations of each persona
- Running completely isolated tests (no context pollution)
- Testing any type of material (taglines, CTAs, visuals, UX flows, features)
- Creating professional HTML/Markdown documentation with interactive charts
- Providing actionable strategic recommendations

## 🎯 Use Cases

### What You Can Test:
- **Taglines** - Brand messaging and positioning
- **CTAs** - Call-to-action button copy
- **Visual Assets** - Images, designs, layouts
- **UX Flows** - User experience sequences
- **Product Features** - Functionality descriptions
- **Landing Pages** - Complete page concepts
- **Email Subject Lines** - Marketing copy
- **Ad Copy** - Advertisement variations
- **Onboarding Flows** - New user experiences
- **Any other user-facing materials**

## 🚀 Quick Start

### 1. Install the Skill

Download and add to Claude:
```bash
# Option A: Direct download
curl -O https://github.com/Yes-Gaming/skills-library/raw/main/synthetic-simulation-execution.skill

# Option B: Clone repository
git clone https://github.com/Yes-Gaming/skills-library.git
```

### 2. Use with Claude

```
I want to test [X] materials with [Y] personas using the synthetic simulation skill.

Testing materials:
1. [Your first option]
2. [Your second option]
3. [Your third option]
...

Please run the simulation.
```

### 3. Review Results

The skill will create a timestamped results folder with:
- Interactive HTML dashboard
- Executive summary with charts
- Individual persona analysis pages
- Complete markdown reports
- All raw data and insights

## 📊 Example Output

When you run a simulation, you'll get:

```
results/2025-11-03_14-30-22/
├── index.html              # Interactive dashboard with Chart.js
├── summary.html            # Executive summary
├── casual-entertainer-english.html
├── sports-enthusiast-english.html
├── assets/
│   ├── styles.css
│   └── script.js
└── markdown/
    ├── summary.md
    └── [persona]_results.md
```

### Interactive Features:
- 📊 Live charts showing preference vs trust gaps
- 📈 Vote distribution visualizations
- 🔍 Persona-specific deep dives
- 💡 Strategic recommendations
- 🎯 A/B test priorities
- 💰 Business impact projections

## 🎭 Available Personas

The skill can use any combination of these personas:

| Persona | Age | Focus | Use For |
|---------|-----|-------|---------|
| **Casual Entertainer** | 22-28 | Entertainment, fun | Mobile-first, casual users |
| **Casino Explorer** | 20-30 | Variety, visuals | Game variety testing |
| **Sports Enthusiast** | 25-35 | Betting, sports | Sports betting features |
| **Trust Seeker** | 40+ | Security, clarity | Older demographic, trust |
| **Cross-Entertainment Engager** | 18-40 | Integration | Unified experience |

Each persona generates **10 unique variations** to capture diversity within the segment.

## 🔬 Methodology

### Context Isolation
Each test round runs in a completely separate agent instance:
- ✅ No memory between tests
- ✅ No context pollution
- ✅ Fresh perspective every time
- ✅ True independent responses

### Persona Variation
Each base persona is expanded into 10 unique individuals:
- Different ages (within range)
- Different backgrounds
- Different motivations
- Different contexts
- Same core characteristics

### Question Framework
Adapts to your testing subject:
- **Q1:** Preference (what attracts)
- **Q2:** Reasoning (why it works)
- **Q3:** Rejection (what repels)
- **Q4:** Trust/Value/Urgency (what converts)

### Randomization
Presentation order randomized each round to prevent position bias.

## 📈 Sample Results

### From Tagline Testing:
```
✓ 100 isolated tests completed

Key Findings:
- Preference Winner: "Watch & Play" (46%)
- Trust Winner: "Casino and Sports Made Easy" (94%)
- Gap: 48 percentage points!

Recommendation: Use different taglines for acquisition vs conversion
```

### Variation Diversity:
```
Casual Entertainer Variations:
- 7/10 agreed on top choice (70% consensus)
- 3/10 preferred alternative (shows some diversity)
- Implication: Strong general preference but some variation
```

## 🎨 Customization

The skill adapts to your specific needs:

### Custom Questions
Modify the 4-question framework for your use case

### Custom Personas
Add new personas to the library

### Custom Metrics
Define what success looks like for your test

### Custom Documentation
Adjust output format and level of detail

## 📊 Results Documentation

Every simulation creates:

### 1. Interactive Dashboard
- Overview section with key metrics
- Methodology explanation
- Results by language/type
- Persona breakdowns
- Strategic recommendations
- Use cases and application guidance

### 2. Executive Summary
- Complete performance tables
- Interactive charts (Chart.js)
- Critical insights
- Preference-trust gap analysis
- Strategic recommendations
- A/B testing priorities
- Business impact projections

### 3. Persona Pages
- Individual persona analysis
- Variation diversity tracking
- Detailed results with charts
- Quotes from synthetic individuals
- Specific recommendations
- Related persona comparisons

### 4. Markdown Reports
- All HTML reports in markdown format
- Easy to version control
- Readable in any text editor
- Shareable with teams

## 💡 Best Practices

### Sample Size
- **Minimum:** 10 rounds per persona variation (100 tests for 1 persona)
- **Recommended:** 10 rounds × 10 variations × multiple personas
- **Large scale:** 500-1000+ tests for critical decisions

### Material Selection
- Test 3-6 options (enough variety, not overwhelming)
- Ensure options are truly different
- Label clearly and consistently
- Provide in same format

### Persona Selection
- Choose personas relevant to your target audience
- Include diverse age ranges
- Cover different motivations
- Consider 3-5 personas for comprehensive insights

### Interpretation
- Look for consensus AND diversity within personas
- Note preference-trust gaps (common and important!)
- Consider context (acquisition vs conversion)
- Test real-world before full rollout

## 🚨 Common Pitfalls

### Avoid:
- ❌ Testing too many options at once (max 6-8)
- ❌ Using same context for all tests (breaks isolation)
- ❌ Ignoring qualitative insights (quotes matter!)
- ❌ Treating synthetic data as gospel (validate with real users)
- ❌ Not considering preference-trust gaps
- ❌ Over-generalizing from one persona

### Do:
- ✅ Maintain context isolation
- ✅ Generate diverse persona variations
- ✅ Randomize presentation order
- ✅ Capture rich qualitative data
- ✅ Document everything systematically
- ✅ Use results to inform (not replace) real testing

## 🔄 Integration

This skill works with:
- Existing persona skills in the library
- Previous tagline testing methodology
- Your custom personas (add to library)
- Any testing framework you prefer

## 📚 Learn More

### Related Skills:
- `casual-entertainer` - Mobile-first entertainment user
- `casino-explorer` - Variety-seeking casino player
- `sports-enthusiast` - Serious sports bettor
- `trust-seeker` - Security-conscious older user
- `cross-entertainment-engager` - Integrated experience user

### Previous Results:
- See `results/2025-11-02_17-26-36/` for tagline testing example
- Full documentation with charts and insights
- Complete methodology and findings

## 🤝 Contributing

To improve this skill:
1. Run simulations and note improvements
2. Suggest new question frameworks
3. Add new personas to library
4. Enhance documentation templates
5. Share insights and patterns

## 📄 License

**Proprietary - Yes.com Exclusive Use**

This skill is created specifically for Yes.com gambling platform testing and research. Not for public distribution or commercial use outside Yes.com.

## 📞 Support

For questions or issues:
- Review the skill.md file for detailed instructions
- Check example results in results/ folder
- Refer to persona skill files for profiles

## 🎯 Success Metrics

A successful simulation provides:
- ✅ Clear winner identification
- ✅ Understanding of audience segments
- ✅ Preference-trust gap insights
- ✅ Actionable recommendations
- ✅ A/B test priorities
- ✅ Risk flags (what to avoid)
- ✅ Business impact projections

---

**Version:** 1.0.0
**Created:** November 2025
**Updated:** November 2025
**For:** Yes.com gambling platform
