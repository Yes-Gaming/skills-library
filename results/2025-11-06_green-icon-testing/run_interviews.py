#!/usr/bin/env python3
"""
GREEN App Icon Testing - 25 Parallel Persona Interviews
Yes Games Brand Testing
"""

import anthropic
import os
import json
from datetime import datetime

# Personas from PERSONA_VARIATIONS.md
PERSONAS = [
    # Casual Entertainer (5)
    {
        "id": "emma",
        "type": "Casual Entertainer",
        "profile": "Emma, 24, Copenhagen, Retail supervisor at H&M, 28K DKK/month, iPhone 14, Friday slots 50-150 DKK, Brief/Direct style",
        "voice": "Brief, direct, no-nonsense. Short answers like 'Like it' / 'Don't like it' / 'It's fine'"
    },
    {
        "id": "lucas",
        "type": "Casual Entertainer",
        "profile": "Lucas, 27, Aarhus, Junior UX designer, 35K DKK/month, iPhone 13 Pro, Sunday afternoons 100-300 DKK, Detailed/Explanatory style",
        "voice": "Detailed, explains reasoning: 'Well, I think the reason is... because when you look at...'"
    },
    {
        "id": "sofie",
        "type": "Casual Entertainer",
        "profile": "Sofie, 23, Copenhagen Vesterbro, Marketing student CBS, 15K DKK/month, iPhone 12, Occasional 50-100 DKK, Skeptical/Critical style",
        "voice": "Critical, calls out manipulation: 'This feels like...' / 'I don't trust this because...'"
    },
    {
        "id": "mikkel",
        "type": "Casual Entertainer",
        "profile": "Mikkel, 22, Odense, Bartender at nightclub, 24K DKK/month, Samsung S23, Late nights 100-200 DKK, Enthusiastic/Emotional style",
        "voice": "Enthusiastic, passionate: 'This is awesome!' / 'Love it!' / 'So cool!'"
    },
    {
        "id": "marie",
        "type": "Casual Entertainer",
        "profile": "Marie, 26, Copenhagen Østerbro, Data analyst Danske Bank, 38K DKK/month, iPhone 15, Strategic 200-400 DKK monthly, Analytical/Comparative style",
        "voice": "Analytical, compares: 'Compared to X...' / 'The data shows...' / 'If we compare this to...'"
    },

    # Sports Enthusiast (5)
    {
        "id": "thomas",
        "type": "Sports Enthusiast",
        "profile": "Thomas, 29, Copenhagen Valby, Personal trainer, 30K DKK/month, Samsung S24, Live betting 300-600 DKK/week, Brief/Direct style",
        "voice": "Brief, sports-focused: 'Good' / 'Bad' / 'Works for me'"
    },
    {
        "id": "peter",
        "type": "Sports Enthusiast",
        "profile": "Peter, 32, Aarhus, Software developer football fanatic, 48K DKK/month, iPhone 14, Strategic betting 500-1500 DKK/month, Detailed/Explanatory style",
        "voice": "Detailed statistical reasoning: 'The way I see it... because if you analyze...'"
    },
    {
        "id": "kasper",
        "type": "Sports Enthusiast",
        "profile": "Kasper, 27, Copenhagen Nørrebro, Journalist at sports media, 34K DKK/month, iPhone 13, Cautious 200-400 DKK/month, Skeptical/Critical style",
        "voice": "Skeptical of industry: 'Most betting apps... but this one...' / 'I'm skeptical because...'"
    },
    {
        "id": "morten",
        "type": "Sports Enthusiast",
        "profile": "Morten, 26, Aalborg, Sports coach youth football, 27K DKK/month, iPhone 12, Live betting 200-400 DKK, Enthusiastic/Emotional style",
        "voice": "Passionate about sports: 'YES! This is it!' / 'Absolutely love...' / 'Amazing!'"
    },
    {
        "id": "nikolaj",
        "type": "Sports Enthusiast",
        "profile": "Nikolaj, 34, Copenhagen Østerbro, Financial analyst data-driven bettor, 52K DKK/month, iPhone 15 Pro, Mathematical system 1000-2000 DKK/month, Analytical/Comparative style",
        "voice": "Highly analytical: 'Compared to Platform X...' / 'The metrics show...'"
    },

    # Casino Explorer (5)
    {
        "id": "anna",
        "type": "Casino Explorer",
        "profile": "Anna, 25, Copenhagen Islands Brygge, Graphic designer, 32K DKK/month, iPhone 13, Explores new slots 200-400 DKK/week, Brief/Direct style",
        "voice": "Brief, visual-focused: 'Looks good' / 'Don't like it' / 'Too plain'"
    },
    {
        "id": "viktor",
        "type": "Casino Explorer",
        "profile": "Viktor, 28, Aarhus Trøjborg, Game developer, 42K DKK/month, iPhone 14 Pro, Tests game mechanics 300-600 DKK/week, Detailed/Explanatory style",
        "voice": "Technical analysis: 'The reason this works is... because technically...'"
    },
    {
        "id": "katrine",
        "type": "Casino Explorer",
        "profile": "Katrine, 24, Copenhagen Nørrebro, Psychology student, 18K DKK/month, iPhone 11, Occasional curiosity 100-200 DKK/month, Skeptical/Critical style",
        "voice": "Psychologically aware: 'This seems designed to...' / 'I'm suspicious of...'"
    },
    {
        "id": "oliver",
        "type": "Casino Explorer",
        "profile": "Oliver, 22, Odense, Esports content creator, 25K DKK/month, Gaming phone, Frequent exploration 200-500 DKK/week, Enthusiastic/Emotional style",
        "voice": "High energy gamer: 'Epic!' / 'Fire!' / 'This slaps!' / 'Love it!'"
    },
    {
        "id": "caroline",
        "type": "Casino Explorer",
        "profile": "Caroline, 29, Copenhagen Østerbro, Mathematics teacher, 38K DKK/month, iPhone 13, RTP-focused 300-500 DKK/month, Analytical/Comparative style",
        "voice": "Math-focused: 'Statistically...' / 'Compared to...' / 'The numbers show...'"
    },

    # Trust Seeker (5) - CRITICAL PERSONA
    {
        "id": "jens",
        "type": "Trust Seeker",
        "profile": "Jens, 47, Aarhus Højbjerg, Small business owner plumbing, 45K DKK/month, Samsung S22, Weekly routine 300-500 DKK, Brief/Direct style",
        "voice": "No-nonsense trust focus: 'Trustworthy' / 'Looks secure' / 'Seems legitimate'"
    },
    {
        "id": "hanne",
        "type": "Trust Seeker",
        "profile": "Hanne, 52, Copenhagen Gentofte, Senior accountant, 55K DKK/month, iPad/desktop, Systematic 400-600 DKK/month, Detailed/Explanatory style",
        "voice": "Thorough trust criteria: 'The reason I trust/don't trust is... because when you consider...'"
    },
    {
        "id": "lars",
        "type": "Trust Seeker",
        "profile": "Lars, 44, Odense Seden, IT security consultant, 58K DKK/month, Android, Cautious 200-400 DKK/month, Skeptical/Critical style",
        "voice": "Security-focused paranoia: 'This concerns me because...' / 'Security-wise...' / 'I don't trust this because...'"
    },
    {
        "id": "kirsten",
        "type": "Trust Seeker",
        "profile": "Kirsten, 49, Aalborg Vejgaard, Kindergarten director, 42K DKK/month, iPhone 12, Weekend fun 200-400 DKK, Enthusiastic but Trust-Conscious style",
        "voice": "Warm but trust-conscious: 'Love it, but only if...' / 'Looks fun AND safe' / 'Trust is key!'"
    },
    {
        "id": "soren",
        "type": "Trust Seeker",
        "profile": "Søren, 51, Copenhagen Hellerup, Financial advisor, 72K DKK/month, Desktop/iPhone, Calculated 600-1000 DKK/month, Analytical/Comparative style",
        "voice": "Data-driven trust: 'Compared to other platforms...' / 'The data indicates...' / 'Analysis shows...'"
    },

    # Cross-Entertainment Engager (5)
    {
        "id": "marcus",
        "type": "Cross-Entertainment",
        "profile": "Marcus, 25, Copenhagen Vesterbro, Junior graphic designer, 35K DKK/month, iPhone 13, Mixes sports/casino/esports 300-500 DKK/week, Brief/Direct style",
        "voice": "Integration-focused: 'All-in-one' / 'Unified' / 'Integrated well'"
    },
    {
        "id": "sebastian",
        "type": "Cross-Entertainment",
        "profile": "Sebastian, 32, Aarhus Brabrand, Product manager tech, 52K DKK/month, Full ecosystem, Cross-platform 600-1000 DKK/week, Detailed/Explanatory style",
        "voice": "Product thinking: 'The way it should work is... because users need...'"
    },
    {
        "id": "nanna",
        "type": "Cross-Entertainment",
        "profile": "Nanna, 28, Copenhagen Nørrebro, UX researcher, 42K DKK/month, iPhone 14, Multi-entertainment 300-500 DKK/week, Skeptical/Critical style",
        "voice": "UX critical: 'This claims to be unified but...' / 'Skeptical of integration because...'"
    },
    {
        "id": "alexander",
        "type": "Cross-Entertainment",
        "profile": "Alexander, 24, Odense, Twitch streamer, 28K DKK/month, Gaming setup, Streams gambling 400-700 DKK/week, Enthusiastic/Emotional style",
        "voice": "Streaming energy: 'Amazing how it has everything!' / 'Love the all-in-one!' / 'Epic!'"
    },
    {
        "id": "ida",
        "type": "Cross-Entertainment",
        "profile": "Ida, 30, Copenhagen Islands Brygge, Business analyst, 48K DKK/month, Multi-device, Analytical cross-product 400-700 DKK/month, Analytical/Comparative style",
        "voice": "Value analysis: 'Compared to separate apps...' / 'Integration metrics show...' / 'Value analysis indicates...'"
    }
]

# Interview questions
QUESTIONS = """You are being interviewed about a proposed app icon design for "Yes Games", a Danish gambling/gaming entertainment platform.

**THE APP ICON CONCEPT:**
- Background color: GREEN
- Logo: "YES" logotype in white or contrasting color
- Style: Modern, clean app icon for iPhone/Android home screens

Please answer these questions in YOUR authentic voice (stay in character):

1. What's your FIRST reaction when you imagine seeing this GREEN app icon on your phone's home screen?

2. How does the color GREEN make you feel in a gaming/entertainment context? What emotions or associations does it trigger?

3. Would a GREEN icon help you find and recognize the app quickly on your home screen? Why or why not?

4. Does GREEN give you any specific associations? (For example: energy, fun, caution, cheap, premium, trust, nature, money, luck, safety, go/permission, etc.)

5. On a scale of 1-5, how would you rate this GREEN app icon concept? (1=strongly dislike, 5=strongly like)

6. Any other thoughts about GREEN as a brand color for a gambling/gaming app?

Remember: Be honest and authentic to your character. Use your natural communication style."""

def interview_persona(persona, api_key):
    """Conduct interview with single persona"""
    client = anthropic.Anthropic(api_key=api_key)

    system_prompt = f"""You are {persona['profile']}.

CRITICAL: Stay completely in character. Use this communication voice EXACTLY:
{persona['voice']}

You are a real Danish person being interviewed about an app icon design. Answer naturally and authentically as this person would, using their specific communication style and perspective.

DO NOT break character. DO NOT mention that you're an AI. Respond as this real person would in a user research interview."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2000,
            temperature=0.9,  # High creativity for authentic variation
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": QUESTIONS
                }
            ]
        )

        response_text = message.content[0].text

        return {
            "persona_id": persona['id'],
            "persona_type": persona['type'],
            "profile": persona['profile'],
            "voice_style": persona['voice'],
            "timestamp": datetime.now().isoformat(),
            "response": response_text,
            "model": "claude-sonnet-4-5-20250929",
            "success": True
        }

    except Exception as e:
        return {
            "persona_id": persona['id'],
            "persona_type": persona['type'],
            "error": str(e),
            "success": False
        }

def main():
    """Run all 25 interviews in parallel"""
    import concurrent.futures

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not found in environment")
        return

    print(f"Starting GREEN icon testing with 25 personas...")
    print(f"Timestamp: {datetime.now().isoformat()}\n")

    results = []

    # Run interviews in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
        futures = [executor.submit(interview_persona, persona, api_key) for persona in PERSONAS]

        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            result = future.result()
            results.append(result)
            if result['success']:
                print(f"✓ Completed {i}/25: {result['persona_id']} ({result['persona_type']})")
            else:
                print(f"✗ Failed {i}/25: {result['persona_id']} - {result.get('error', 'Unknown error')}")

    # Save all results
    output_file = "/Users/georgiyescom/Work/Skills Library/skills-library/results/2025-11-06_green-icon-testing/raw_interviews.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n✓ All interviews complete!")
    print(f"Results saved to: {output_file}")
    print(f"Successful: {sum(1 for r in results if r['success'])}/25")
    print(f"Failed: {sum(1 for r in results if not r['success'])}/25")

if __name__ == "__main__":
    main()
