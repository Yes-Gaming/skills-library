#!/usr/bin/env python3
"""
GOLDEN App Icon Testing - Parallel Interview Orchestrator
Launches 25 isolated persona interviews simultaneously
"""

import json
import subprocess
import concurrent.futures
import os
from pathlib import Path

# Define the 25 personas from PERSONA_VARIATIONS.md
PERSONAS = [
    # CASUAL ENTERTAINER (5 personas)
    {
        "name": "Emma",
        "age": 24,
        "location": "Copenhagen, Nørrebro",
        "occupation": "Retail supervisor at H&M",
        "income": "28,000 DKK/month",
        "device": "iPhone 14, mobile-only user",
        "gambling_pattern": "Friday evenings after work, 50-150 DKK on slots",
        "motivation": "Just want to zone out and have fun after a long week",
        "key_concern": "Don't want anything complicated or time-consuming",
        "discovery": "Friend showed her a casino app during girls' night",
        "communication_style": "Brief, direct, no-nonsense",
        "response_pattern": "Short answers, gets to the point quickly",
        "survey_voice": "Like it / Don't like it / It's fine",
        "persona_type": "Casual Entertainer",
        "persona_id": "casual_1"
    },
    {
        "name": "Lucas",
        "age": 27,
        "location": "Aarhus, Midtbyen",
        "occupation": "Junior UX designer at tech startup",
        "income": "35,000 DKK/month",
        "device": "iPhone 13 Pro, appreciates good design",
        "gambling_pattern": "Sunday afternoons, 100-300 DKK mixed games",
        "motivation": "I like the visual experience and seeing creative game design",
        "key_concern": "Poor UX and cluttered interfaces annoy me",
        "discovery": "Saw sleek app design while browsing App Store",
        "communication_style": "Detailed, explains reasoning thoroughly",
        "response_pattern": "Walks through decision process step-by-step",
        "survey_voice": "Well, I think the reason is... because when you look at...",
        "persona_type": "Casual Entertainer",
        "persona_id": "casual_2"
    },
    {
        "name": "Sofie",
        "age": 23,
        "location": "Copenhagen, Vesterbro",
        "occupation": "Marketing student at Copenhagen Business School",
        "income": "15,000 DKK/month (part-time + student aid)",
        "device": "iPhone 12, very aware of marketing tactics",
        "gambling_pattern": "Occasional, 50-100 DKK when bored",
        "motivation": "Entertainment, but I don't trust most gambling apps",
        "key_concern": "Too many apps try to manipulate you with flashy stuff",
        "discovery": "Skeptical of ads, only tried after friend's recommendation",
        "communication_style": "Critical, calls out what feels wrong",
        "response_pattern": "Points out flaws, questions intentions",
        "survey_voice": "This feels like... / I don't trust this because...",
        "persona_type": "Casual Entertainer",
        "persona_id": "casual_3"
    },
    {
        "name": "Mikkel",
        "age": 22,
        "location": "Odense, city center",
        "occupation": "Bartender at popular nightclub",
        "income": "24,000 DKK/month",
        "device": "Samsung Galaxy S23, loves gaming",
        "gambling_pattern": "Late nights after work, 100-200 DKK",
        "motivation": "Love the thrill! It's exciting and keeps me buzzing",
        "key_concern": "Boring games are a total buzzkill",
        "discovery": "Coworker was playing during break, looked fun",
        "communication_style": "Enthusiastic, uses exclamations, emotional",
        "response_pattern": "Passionate, expressive language",
        "survey_voice": "This is awesome! / Love it! / So cool!",
        "persona_type": "Casual Entertainer",
        "persona_id": "casual_4"
    },
    {
        "name": "Marie",
        "age": 26,
        "location": "Copenhagen, Østerbro",
        "occupation": "Data analyst at Danske Bank",
        "income": "38,000 DKK/month",
        "device": "iPhone 15, very analytical about choices",
        "gambling_pattern": "Strategic, 200-400 DKK monthly budget",
        "motivation": "Like analyzing odds and making informed decisions",
        "key_concern": "Need transparency in RTP and clear information",
        "discovery": "Researched multiple apps, compared features",
        "communication_style": "Analytical, compares options systematically",
        "response_pattern": "Compared to X... / The data shows...",
        "survey_voice": "If we compare this to... / Looking at the options...",
        "persona_type": "Casual Entertainer",
        "persona_id": "casual_5"
    },
    # SPORTS ENTHUSIAST (5 personas)
    {
        "name": "Thomas",
        "age": 29,
        "location": "Copenhagen, Valby",
        "occupation": "Personal trainer",
        "income": "30,000 DKK/month",
        "device": "Samsung Galaxy S24, watches matches on phone",
        "gambling_pattern": "Live betting during football matches, 300-600 DKK/week",
        "motivation": "Makes watching the game more exciting",
        "key_concern": "App needs to be fast during live matches - no lag",
        "discovery": "Friends at the gym all use betting apps for Superliga",
        "communication_style": "Brief, direct, sports-focused",
        "response_pattern": "Short, decisive answers",
        "survey_voice": "Good / Bad / Works for me",
        "persona_type": "Sports Enthusiast",
        "persona_id": "sports_1"
    },
    {
        "name": "Peter",
        "age": 32,
        "location": "Aarhus, Brabrand",
        "occupation": "Software developer, football fanatic",
        "income": "48,000 DKK/month",
        "device": "iPhone 14, desktop for pre-match research",
        "gambling_pattern": "Strategic betting, 500-1500 DKK/month budgeted",
        "motivation": "I study team stats and odds - it's strategic, not random",
        "key_concern": "Need comprehensive statistics and market depth",
        "discovery": "Researched betting sites after analyzing odds models",
        "communication_style": "Detailed, explains statistical reasoning",
        "response_pattern": "Walks through analysis process",
        "survey_voice": "The way I see it... because if you analyze...",
        "persona_type": "Sports Enthusiast",
        "persona_id": "sports_2"
    },
    {
        "name": "Kasper",
        "age": 27,
        "location": "Copenhagen, Nørrebro",
        "occupation": "Journalist at sports media outlet",
        "income": "34,000 DKK/month",
        "device": "iPhone 13, very aware of gambling industry tactics",
        "gambling_pattern": "Cautious betting, 200-400 DKK/month",
        "motivation": "Know the industry well - only bet when I see value",
        "key_concern": "Too many sites are predatory or have hidden terms",
        "discovery": "Professional research on gambling industry for article",
        "communication_style": "Skeptical, questions everything",
        "response_pattern": "Points out industry issues",
        "survey_voice": "Most betting apps... but this one... / I'm skeptical because...",
        "persona_type": "Sports Enthusiast",
        "persona_id": "sports_3"
    },
    {
        "name": "Morten",
        "age": 26,
        "location": "Aalborg, city center",
        "occupation": "Sports coach for youth football",
        "income": "27,000 DKK/month",
        "device": "iPhone 12, lives and breathes football",
        "gambling_pattern": "Live betting every match day, 200-400 DKK",
        "motivation": "LOVE the rush when my bet comes through during a match!",
        "key_concern": "Has to capture the emotion and energy of the game",
        "discovery": "Fellow coach introduced him during a Superliga match",
        "communication_style": "Passionate about sports, emotional",
        "response_pattern": "High energy, expressive",
        "survey_voice": "YES! This is it! / Absolutely love... / Amazing!",
        "persona_type": "Sports Enthusiast",
        "persona_id": "sports_4"
    },
    {
        "name": "Nikolaj",
        "age": 34,
        "location": "Copenhagen, Østerbro",
        "occupation": "Financial analyst, data-driven bettor",
        "income": "52,000 DKK/month",
        "device": "iPhone 15 Pro, uses desktop for analytics",
        "gambling_pattern": "Mathematical betting system, 1000-2000 DKK/month",
        "motivation": "Developed a statistical model - betting is calculated risk",
        "key_concern": "Need accurate odds, deep markets, and reliable data feeds",
        "discovery": "Evaluated 8 platforms, chose based on market depth",
        "communication_style": "Highly analytical, comparison-focused",
        "response_pattern": "Compares features systematically",
        "survey_voice": "Compared to Platform X... / The metrics show...",
        "persona_type": "Sports Enthusiast",
        "persona_id": "sports_5"
    },
    # CASINO EXPLORER (5 personas)
    {
        "name": "Anna",
        "age": 25,
        "location": "Copenhagen, Islands Brygge",
        "occupation": "Graphic designer",
        "income": "32,000 DKK/month",
        "device": "iPhone 13, visual aesthetics matter",
        "gambling_pattern": "Explores new slots, 200-400 DKK/week",
        "motivation": "Love discovering new games with cool visuals",
        "key_concern": "Boring games or poor graphics turn me off immediately",
        "discovery": "Browsed App Store for visually appealing casino games",
        "communication_style": "Brief, visual-focused",
        "response_pattern": "Quick visual assessments",
        "survey_voice": "Looks good / Don't like it / Too plain",
        "persona_type": "Casino Explorer",
        "persona_id": "casino_1"
    },
    {
        "name": "Viktor",
        "age": 28,
        "location": "Aarhus, Trøjborg",
        "occupation": "Game developer, appreciates design",
        "income": "42,000 DKK/month",
        "device": "iPhone 14 Pro, technical eye for quality",
        "gambling_pattern": "Tests different game mechanics, 300-600 DKK/week",
        "motivation": "Professional interest in game design plus entertainment",
        "key_concern": "Poor UX or lazy game design frustrates me",
        "discovery": "Researched casino game mechanics for work project",
        "communication_style": "Detailed, technical analysis",
        "response_pattern": "Explains design reasoning",
        "survey_voice": "The reason this works is... because technically...",
        "persona_type": "Casino Explorer",
        "persona_id": "casino_2"
    },
    {
        "name": "Katrine",
        "age": 24,
        "location": "Copenhagen, Nørrebro",
        "occupation": "Psychology student",
        "income": "18,000 DKK/month",
        "device": "iPhone 11, aware of psychological tactics",
        "gambling_pattern": "Occasional curiosity, 100-200 DKK/month",
        "motivation": "Curious about gambling psychology, but skeptical of manipulation",
        "key_concern": "Hate when apps use psychological tricks to keep you playing",
        "discovery": "Academic interest in gambling design and behavior",
        "communication_style": "Critical, psychologically aware",
        "response_pattern": "Questions design intentions",
        "survey_voice": "This seems designed to... / I'm suspicious of...",
        "persona_type": "Casino Explorer",
        "persona_id": "casino_3"
    },
    {
        "name": "Oliver",
        "age": 22,
        "location": "Odense, city center",
        "occupation": "Esports content creator",
        "income": "25,000 DKK/month",
        "device": "Gaming phone setup, loves flashy graphics",
        "gambling_pattern": "Frequent game exploration, 200-500 DKK/week",
        "motivation": "The visuals are INSANE! Love the themes and excitement",
        "key_concern": "Needs to be visually stunning and constantly new content",
        "discovery": "Streamer friend played casino games, looked amazing",
        "communication_style": "Enthusiastic, gaming language",
        "response_pattern": "High energy, gamer terminology",
        "survey_voice": "Epic! / Fire! / This slaps! / Love it!",
        "persona_type": "Casino Explorer",
        "persona_id": "casino_4"
    },
    {
        "name": "Caroline",
        "age": 29,
        "location": "Copenhagen, Østerbro",
        "occupation": "Mathematics teacher",
        "income": "38,000 DKK/month",
        "device": "iPhone 13, analyzes game mathematics",
        "gambling_pattern": "RTP-focused gaming, 300-500 DKK/month",
        "motivation": "Interested in probability - play games with best RTP",
        "key_concern": "Need transparent RTP information and fair games",
        "discovery": "Compared RTP percentages across platforms",
        "communication_style": "Analytical, math-focused",
        "response_pattern": "Compares statistics and probabilities",
        "survey_voice": "Statistically... / Compared to... / The numbers show...",
        "persona_type": "Casino Explorer",
        "persona_id": "casino_5"
    },
    # TRUST SEEKER (5 personas)
    {
        "name": "Jens",
        "age": 47,
        "location": "Aarhus, Højbjerg",
        "occupation": "Small business owner (plumbing)",
        "income": "45,000 DKK/month",
        "device": "Samsung Galaxy S22, prefers desktop when possible",
        "gambling_pattern": "Weekly routine, 300-500 DKK consistently",
        "motivation": "Been gambling responsibly for years - it's entertainment",
        "key_concern": "Must be licensed, secure, and trustworthy",
        "discovery": "Friend recommended after bad experience with shady site",
        "communication_style": "Brief, no-nonsense, values honesty",
        "response_pattern": "Direct assessments of trust",
        "survey_voice": "Trustworthy / Looks secure / Seems legitimate",
        "persona_type": "Trust Seeker",
        "persona_id": "trust_1"
    },
    {
        "name": "Hanne",
        "age": 52,
        "location": "Copenhagen, Gentofte",
        "occupation": "Senior accountant",
        "income": "55,000 DKK/month",
        "device": "iPad for browsing, desktop for betting",
        "gambling_pattern": "Systematic, 400-600 DKK/month budgeted",
        "motivation": "Controlled entertainment - I track every transaction",
        "key_concern": "Need transparent terms, visible licensing, clear responsible gambling tools",
        "discovery": "Extensively researched Spillemyndigheden-licensed sites",
        "communication_style": "Detailed, thorough, explains concerns",
        "response_pattern": "Walks through trust criteria systematically",
        "survey_voice": "The reason I trust/don't trust is... because when you consider...",
        "persona_type": "Trust Seeker",
        "persona_id": "trust_2"
    },
    {
        "name": "Lars",
        "age": 44,
        "location": "Odense, Seden",
        "occupation": "IT security consultant",
        "income": "58,000 DKK/month",
        "device": "Android, very security-conscious",
        "gambling_pattern": "Cautious, 200-400 DKK/month after vetting",
        "motivation": "Enjoy it, but only on platforms I've security-audited myself",
        "key_concern": "Most gambling sites have terrible security or hidden practices",
        "discovery": "Professional paranoia - vetted multiple platforms",
        "communication_style": "Highly skeptical, security-focused",
        "response_pattern": "Points out security/trust red flags",
        "survey_voice": "This concerns me because... / Security-wise... / I don't trust this because...",
        "persona_type": "Trust Seeker",
        "persona_id": "trust_3"
    },
    {
        "name": "Kirsten",
        "age": 49,
        "location": "Aalborg, Vejgaard",
        "occupation": "Kindergarten director",
        "income": "42,000 DKK/month",
        "device": "iPhone 12, uses both mobile and tablet",
        "gambling_pattern": "Weekend fun, 200-400 DKK weekly",
        "motivation": "Love the fun and excitement - but only on sites I trust!",
        "key_concern": "Must show responsible gambling messages and limits",
        "discovery": "Colleague recommended trustworthy site after license check",
        "communication_style": "Warm but trust-conscious",
        "response_pattern": "Enthusiastic about fun, serious about trust",
        "survey_voice": "Love it, but only if... / Looks fun AND safe / Trust is key!",
        "persona_type": "Trust Seeker",
        "persona_id": "trust_4"
    },
    {
        "name": "Søren",
        "age": 51,
        "location": "Copenhagen, Hellerup",
        "occupation": "Financial advisor",
        "income": "72,000 DKK/month",
        "device": "Desktop primary, iPhone secondary",
        "gambling_pattern": "Calculated, 600-1000 DKK/month",
        "motivation": "Analyzed odds and house edge - playing is calculated decision",
        "key_concern": "Need detailed payout information, RTP transparency, audit reports",
        "discovery": "Compared regulatory compliance across 12 platforms",
        "communication_style": "Highly analytical, data-driven",
        "response_pattern": "Compares trust metrics systematically",
        "survey_voice": "Compared to other platforms... / The data indicates... / Analysis shows...",
        "persona_type": "Trust Seeker",
        "persona_id": "trust_5"
    },
    # CROSS-ENTERTAINMENT (5 personas)
    {
        "name": "Marcus",
        "age": 25,
        "location": "Copenhagen, Vesterbro",
        "occupation": "Junior graphic designer at digital agency",
        "income": "35,000 DKK/month",
        "device": "iPhone 13, seamless multi-device user",
        "gambling_pattern": "Mixes sports, casino, esports, 300-500 DKK/week",
        "motivation": "Want everything in one app - sports, casino, esports",
        "key_concern": "Hate switching between apps - needs to be unified",
        "discovery": "Found platform offering all entertainment types",
        "communication_style": "Brief, integration-focused",
        "response_pattern": "Quick assessments of versatility",
        "survey_voice": "All-in-one / Unified / Integrated well",
        "persona_type": "Cross-Entertainment",
        "persona_id": "cross_1"
    },
    {
        "name": "Sebastian",
        "age": 32,
        "location": "Aarhus, Brabrand",
        "occupation": "Product manager at tech company",
        "income": "52,000 DKK/month",
        "device": "Full ecosystem (phone, tablet, laptop, TV app)",
        "gambling_pattern": "Cross-platform power user, 600-1000 DKK/week",
        "motivation": "Need seamless experience across sports betting, casino, and social features",
        "key_concern": "Platform integration and sync across devices is critical",
        "discovery": "Evaluated platforms based on ecosystem integration",
        "communication_style": "Detailed, product-thinking",
        "response_pattern": "Explains integration requirements thoroughly",
        "survey_voice": "The way it should work is... because users need...",
        "persona_type": "Cross-Entertainment",
        "persona_id": "cross_2"
    },
    {
        "name": "Nanna",
        "age": 28,
        "location": "Copenhagen, Nørrebro",
        "occupation": "UX researcher",
        "income": "42,000 DKK/month",
        "device": "iPhone 14, very critical of UX",
        "gambling_pattern": "Multi-entertainment user, 300-500 DKK/week",
        "motivation": "Interested in unified experience, but most platforms fail at it",
        "key_concern": "Platforms claim integration but deliver fragmented experience",
        "discovery": "Professional interest in multi-platform UX design",
        "communication_style": "Critically evaluates integration claims",
        "response_pattern": "Points out UX fragmentation issues",
        "survey_voice": "This claims to be unified but... / Skeptical of integration because...",
        "persona_type": "Cross-Entertainment",
        "persona_id": "cross_3"
    },
    {
        "name": "Alexander",
        "age": 24,
        "location": "Odense, city center",
        "occupation": "Twitch streamer / content creator",
        "income": "28,000 DKK/month (streaming + part-time)",
        "device": "Gaming setup (phone, streaming PC, multiple screens)",
        "gambling_pattern": "Streams gambling content, 400-700 DKK/week",
        "motivation": "LOVE platforms with everything! Casino, sports, esports - all there!",
        "key_concern": "Needs to be content-worthy and shareable across platforms",
        "discovery": "Streamer community recommended all-in-one platform",
        "communication_style": "Enthusiastic, streaming language",
        "response_pattern": "High energy about integration",
        "survey_voice": "Amazing how it has everything! / Love the all-in-one! / Epic!",
        "persona_type": "Cross-Entertainment",
        "persona_id": "cross_4"
    },
    {
        "name": "Ida",
        "age": 30,
        "location": "Copenhagen, Islands Brygge",
        "occupation": "Business analyst",
        "income": "48,000 DKK/month",
        "device": "Multi-device professional user",
        "gambling_pattern": "Analytical cross-product usage, 400-700 DKK/month",
        "motivation": "Analyzed value proposition - unified platform offers better value",
        "key_concern": "Need data consistency and unified account management",
        "discovery": "Compared feature matrices across platforms",
        "communication_style": "Analytical comparison of integration",
        "response_pattern": "Evaluates unified value systematically",
        "survey_voice": "Compared to separate apps... / Integration metrics show... / Value analysis indicates...",
        "persona_type": "Cross-Entertainment",
        "persona_id": "cross_5"
    }
]

def run_single_interview(persona):
    """Run interview for a single persona and save results"""
    persona_json = json.dumps(persona)
    persona_id = persona['persona_id']

    print(f"Starting interview with {persona['name']} ({persona_id})...")

    script_dir = Path(__file__).parent
    interview_script = script_dir / "golden_icon_interview.py"

    try:
        result = subprocess.run(
            ["python3", str(interview_script), persona_json, persona_id],
            capture_output=True,
            text=True,
            timeout=180  # 3 minutes per interview
        )

        if result.returncode == 0:
            interview_data = json.loads(result.stdout)

            # Save individual result
            output_file = script_dir / f"interview_{persona_id}.json"
            with open(output_file, 'w') as f:
                json.dump(interview_data, f, indent=2)

            print(f"Completed interview with {persona['name']}")
            return interview_data
        else:
            print(f"Error interviewing {persona['name']}: {result.stderr}")
            return None

    except subprocess.TimeoutExpired:
        print(f"Timeout interviewing {persona['name']}")
        return None
    except Exception as e:
        print(f"Exception interviewing {persona['name']}: {e}")
        return None

def main():
    print("=" * 80)
    print("GOLDEN APP ICON TESTING - 25 PARALLEL INTERVIEWS")
    print("=" * 80)
    print()

    # Run all 25 interviews in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
        futures = [executor.submit(run_single_interview, persona) for persona in PERSONAS]

        results = []
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    print()
    print("=" * 80)
    print(f"COMPLETED: {len(results)}/25 interviews successful")
    print("=" * 80)

    # Save consolidated results
    script_dir = Path(__file__).parent
    consolidated_file = script_dir / "all_interviews.json"
    with open(consolidated_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nConsolidated results saved to: {consolidated_file}")

if __name__ == "__main__":
    main()
