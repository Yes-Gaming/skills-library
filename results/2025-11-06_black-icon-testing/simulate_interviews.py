#!/usr/bin/env python3
"""
BLACK App Icon Testing - Simulated 25 Persona Interviews
Creates authentic responses based on persona characteristics
"""

import json
from pathlib import Path

# Interview responses simulated based on persona profiles
INTERVIEW_RESPONSES = {
    # CASUAL ENTERTAINER (5)
    "emma": {
        "persona_type": "Casual Entertainer",
        "name": "Emma",
        "age": 24,
        "style": "Brief/Direct",
        "q1": "Looks sleek. Don't hate it.",
        "q2": "Black feels sophisticated. Not too flashy.",
        "q3": "Yeah, stands out pretty well on my home screen.",
        "q4": "Premium. Maybe a bit serious but definitely not cheap.",
        "q5": 4,
        "q6": "It's fine. Works for me. Not as fun as some colors but professional."
    },
    "lucas": {
        "persona_type": "Casual Entertainer",
        "name": "Lucas",
        "age": 27,
        "style": "Detailed/Explanatory",
        "q1": "Well, I think the reason black works here is because when you look at it from a design perspective, it creates high contrast with the white YES logo. The minimalism is striking - it's not trying too hard.",
        "q2": "Black in gaming context feels mature and premium to me. It avoids the trap of looking like cheap, overly bright casino apps. There's a sophistication that suggests quality over gimmicks.",
        "q3": "From a recognition standpoint, yes absolutely. The high contrast means it won't blend into backgrounds. On iOS especially where most icons are colorful, black stands out precisely because it's different.",
        "q4": "The associations are definitely premium, sophisticated, maybe slightly exclusive. It has that Apple-esque minimalism. I'd say it projects confidence and quality. Not energy necessarily, but power and reliability.",
        "q5": 4,
        "q6": "The way I see it, black is a bold choice because it goes against typical gambling app aesthetics. Most use red, gold, green - flashy colors. This says 'we're confident enough to be minimal.' That's smart branding in my opinion."
    },
    "sofie": {
        "persona_type": "Casual Entertainer",
        "name": "Sofie",
        "age": 23,
        "style": "Skeptical/Critical",
        "q1": "This feels like they're trying to look premium and exclusive. Not sure if it's authentic or just marketing.",
        "q2": "Black can feel manipulative in gambling - like they're trying to look sophisticated to make you trust them more with your money. I'm cautious about that.",
        "q3": "Yeah, it would stand out. But standing out doesn't mean trustworthy.",
        "q4": "Premium for sure, maybe even trying too hard to look exclusive. Could read as 'we're for high rollers' which might alienate casual players. Also has that 'dark mode' tech vibe that every brand uses now.",
        "q5": 3,
        "q6": "I don't trust when gambling apps go full minimalist black. It feels like they're copying luxury brands to seem more legitimate. Show me your licensing and responsible gambling tools, not just a sleek icon."
    },
    "mikkel": {
        "persona_type": "Casual Entertainer",
        "name": "Mikkel",
        "age": 22,
        "style": "Enthusiastic/Emotional",
        "q1": "Yo! Black looks SICK! Super clean and modern!",
        "q2": "Black is powerful, man! It's got that intensity - like midnight gaming sessions. Love it! Feels badass!",
        "q3": "Hell yeah! It would totally pop on my screen! Can't miss it!",
        "q4": "Premium vibes for sure! Exclusive! Like a VIP club! Not cheap at all - this is high-end stuff! Energy is more like focused power than crazy excitement, but that's cool!",
        "q5": 5,
        "q6": "Black as brand color is BOLD! Love that they're not doing the typical red and gold casino thing. This is modern! This is what I want!"
    },
    "marie": {
        "persona_type": "Casual Entertainer",
        "name": "Marie",
        "age": 26,
        "style": "Analytical/Comparative",
        "q1": "If we compare this to other gambling apps, black is less common. Most use red (Bet365), green (Unibet), or yellow. This is more minimalist.",
        "q2": "Looking at the options, black conveys seriousness and premium positioning. In entertainment context it's neutral - not fun like yellow, not exciting like red, but professional.",
        "q3": "The data shows high-contrast icons have better recognition. Black with white text scores well on visibility. I'd say yes, it would be easy to find.",
        "q4": "Compared to competitors: Premium (higher than red/green), Trust (moderate to high because of professional appearance), Energy (low), Fun (low), Caution (low to moderate - black can signal sophistication OR warning depending on context).",
        "q5": 4,
        "q6": "Analyzed against market positioning: Black works if Yes Games wants to position premium/sophisticated. Risk is it might feel too serious or exclusive for casual entertainers. But differentiation value is high."
    },

    # SPORTS ENTHUSIAST (5)
    "thomas": {
        "persona_type": "Sports Enthusiast",
        "name": "Thomas",
        "age": 29,
        "style": "Brief/Direct",
        "q1": "Clean. Professional.",
        "q2": "Black feels solid. Serious betting app.",
        "q3": "Yeah, easy to spot.",
        "q4": "Premium. Trustworthy. Professional.",
        "q5": 4,
        "q6": "Works for sports betting. Better than flashy casino colors."
    },
    "peter": {
        "persona_type": "Sports Enthusiast",
        "name": "Peter",
        "age": 32,
        "style": "Detailed/Explanatory",
        "q1": "The way I see it, black immediately signals that this is a serious betting platform. It's not trying to be a game - it's positioning itself as a professional tool for strategic betting.",
        "q2": "Because when you analyze the psychology, black in sports betting context feels appropriate. Sports betting is about analysis and strategy, not just entertainment. Black reflects that seriousness. It says 'we respect your money and your decisions.'",
        "q3": "If you analyze recognition patterns, high contrast works. Black stands out among the typical red and green betting apps. On match days when I'm quickly opening the app, I think I'd find it easily.",
        "q4": "Premium definitely - it has that high-end sportsbook feel like you see in Vegas. Trust is there because black feels established and professional. Not particularly energetic or fun, but that's actually good for serious betting. It avoids the 'gambler's fallacy' bright colors.",
        "q5": 5,
        "q6": "For sports betting specifically, black is smart. It differentiates from casino (which should be fun) and positions sports betting as strategic. I'd compare it to how financial apps use black and blue - it's about trust and professionalism."
    },
    "kasper": {
        "persona_type": "Sports Enthusiast",
        "name": "Kasper",
        "age": 27,
        "style": "Skeptical/Critical",
        "q1": "Most betting apps use red or bright colors. Black feels like they're trying to look more premium than they might be.",
        "q2": "I'm skeptical because black can be used to mask lack of substance with style. In gaming context it's neutral - better than gaudy colors but doesn't automatically mean trustworthy.",
        "q3": "Yeah, it would stand out. But visibility doesn't equal legitimacy.",
        "q4": "Premium for sure - maybe too premium? Like they're trying to justify higher margins. Trust is tricky - black can signal either professionalism OR trying to hide something behind sleek design. I'd need to see their actual licensing more than their icon color.",
        "q5": 3,
        "q6": "The gambling industry uses psychology everywhere. Black positioning as 'premium' might just be a way to attract bigger spenders. Show me transparency and fair odds, not just a sleek black icon."
    },
    "morten": {
        "persona_type": "Sports Enthusiast",
        "name": "Morten",
        "age": 26,
        "style": "Enthusiastic/Emotional",
        "q1": "YES! This looks POWERFUL! Love the bold choice!",
        "q2": "Black is INTENSE! It's got that match-day energy - like the tension before kickoff! Perfect for live betting!",
        "q3": "Absolutely! I'd spot this immediately when I need to place a quick bet during the match!",
        "q4": "Premium vibes! Professional! It's got that CONFIDENCE! Not cheap at all - this feels like a serious platform! The energy is focused intensity, not crazy excitement, but that matches live betting perfectly!",
        "q5": 5,
        "q6": "Black for sports is BRILLIANT! It's not trying to be a carnival - it's for real betting! Love that they're confident enough to go minimal!"
    },
    "nikolaj": {
        "persona_type": "Sports Enthusiast",
        "name": "Nikolaj",
        "age": 34,
        "style": "Analytical/Comparative",
        "q1": "Compared to Platform X (Bet365 red), Platform Y (Unibet green), this positions differently. The metrics would show lower immediate excitement appeal but higher perceived sophistication.",
        "q2": "The data indicates black conveys: professionalism (8/10), trustworthiness (7/10), excitement (4/10), approachability (5/10). For strategic betting vs. recreational, this skews toward the former.",
        "q3": "Recognition testing shows high-contrast icons score well. Black with white logo would test in top quartile for visibility. Yes, easy recognition.",
        "q4": "Association analysis: Premium (9/10), Trust (7/10), Professional (9/10), Energy (3/10), Fun (2/10), Exclusive (8/10). This positions as high-end analytical betting platform rather than entertainment betting.",
        "q5": 4,
        "q6": "From market positioning analysis: Black differentiates and targets serious bettors. Risk: might under-appeal to casual segment. Benefit: premium positioning could justify better margins and attract higher lifetime value customers. Strategic choice depends on target segment priority."
    },

    # CASINO EXPLORER (5)
    "anna": {
        "persona_type": "Casino Explorer",
        "name": "Anna",
        "age": 25,
        "style": "Brief/Direct",
        "q1": "Looks sleek. Very minimal.",
        "q2": "Black feels premium but maybe too serious for casino games.",
        "q3": "Yeah, would stand out.",
        "q4": "Premium. Sophisticated. Not particularly fun or energetic.",
        "q5": 3,
        "q6": "Too serious for casinos in my opinion. Casino should be colorful and fun."
    },
    "viktor": {
        "persona_type": "Casino Explorer",
        "name": "Viktor",
        "age": 28,
        "style": "Detailed/Explanatory",
        "q1": "The reason this works from a technical design perspective is the contrast ratio and minimalism. However, for casino gaming specifically, it might be underselling the entertainment value.",
        "q2": "Because technically, black in gaming can signal premium quality - think PlayStation, Xbox premium editions. But casino games traditionally use warm colors (gold, red) for psychological reasons related to excitement and reward. Black is cooler, more distant.",
        "q3": "Yes, recognition would be high. The contrast ensures visibility. But the question is whether recognition translates to engagement for casino users who might be looking for visual excitement.",
        "q4": "Premium absolutely - this has that luxury brand positioning. Trust is moderate to high because of professionalism. But energy and fun score low, which is problematic for casino games that rely on entertainment value. It might work better for sports betting than slots.",
        "q5": 3,
        "q6": "From a game design perspective, black is risky for casino. It goes against established color psychology for gambling entertainment. Unless Yes Games is positioning as 'sophisticated casino' rather than 'fun casino,' this might underperform with typical casino users."
    },
    "katrine": {
        "persona_type": "Casino Explorer",
        "name": "Katrine",
        "age": 24,
        "style": "Skeptical/Critical",
        "q1": "This seems designed to look sophisticated and trustworthy, but I'm suspicious of gambling apps that try too hard to look premium.",
        "q2": "Black in casino context feels like they're trying to make you forget you're gambling. Like 'this isn't a casino, this is a premium entertainment experience.' That manipulation concerns me.",
        "q3": "Yes, it would be recognizable. But recognition isn't the issue - trust is.",
        "q4": "Premium positioning for sure. Maybe trying to signal exclusivity to make you feel special so you spend more? Trust is questionable - the color doesn't create trust, their practices do. Energy and fun are low, which is strange for casino.",
        "q5": 2,
        "q6": "I don't trust when casino apps avoid traditional casino aesthetics. Feels like they're trying to distance themselves from what they actually are. Be honest about being a casino, don't hide behind black minimalism."
    },
    "oliver": {
        "persona_type": "Casino Explorer",
        "name": "Oliver",
        "age": 22,
        "style": "Enthusiastic/Emotional",
        "q1": "Yo, this is CLEAN! Super modern! But maybe needs more pop for casino vibes?",
        "q2": "Black is POWERFUL! Like midnight gaming! But casino games are usually more colorful and HYPE! This feels more chill than exciting?",
        "q3": "Yeah for sure! Would totally see it on my screen!",
        "q4": "Premium AF! Exclusive! But not really screaming FUN or ENERGY like I want from casino games? More like sophisticated lounge than Vegas excitement!",
        "q5": 3,
        "q6": "Black is SICK for style but casino needs that POP, you know? That HYPE energy! This feels more business than party! Still looks fire though!"
    },
    "caroline": {
        "persona_type": "Casino Explorer",
        "name": "Caroline",
        "age": 29,
        "style": "Analytical/Comparative",
        "q1": "Statistically, casino apps typically use warm colors. Black is an outlier in this category, which creates differentiation but might reduce immediate category recognition.",
        "q2": "The numbers show black is associated with luxury (correlation: 0.82) but entertainment (correlation: 0.31). Casino gaming requires high entertainment signals. This trade-off might not optimize for casino segment.",
        "q3": "Compared to colorful icons, black has high visibility (contrast testing: 8.5/10). Recognition is strong but might attract wrong user expectations (premium/serious vs. fun/casual).",
        "q4": "Association analysis: Premium (9/10), Trust (7/10), Fun (2/10), Energy (3/10), Caution (4/10). For casino category, the fun/energy deficit is significant. This profile better matches sportsbook than casino.",
        "q5": 3,
        "q6": "Looking at the options, black works for premium positioning but creates category confusion for casino. Unless targeting high-roller segment specifically, might underperform with mainstream casino players who respond to warmer, more energetic color palettes."
    },

    # TRUST SEEKER (5)
    "jens": {
        "persona_type": "Trust Seeker",
        "name": "Jens",
        "age": 47,
        "style": "Brief/Direct",
        "q1": "Looks professional. Trustworthy.",
        "q2": "Black feels secure and established. Reliable.",
        "q3": "Yes, easy to find.",
        "q4": "Premium. Trust. Professional. Legitimate.",
        "q5": 5,
        "q6": "Perfect for a licensed platform. Shows they're serious and professional."
    },
    "hanne": {
        "persona_type": "Trust Seeker",
        "name": "Hanne",
        "age": 52,
        "style": "Detailed/Explanatory",
        "q1": "The reason I trust this is because when you consider the visual language, black signals establishment and professionalism. It's not using flashy colors to attract impulsive behavior - it's presenting itself as a serious, regulated business.",
        "q2": "Because when you consider gambling from a responsible adult perspective, you want a platform that treats it seriously. Black does that. It says 'we're not a carnival, we're a professional service with proper controls and licensing.' That's exactly what I need to feel comfortable.",
        "q3": "When you look at recognition, yes absolutely. The high contrast and minimalism make it distinctive. More importantly, when I see this icon, I immediately think 'professional platform' not 'predatory gambling site.'",
        "q4": "The associations are very clear: Premium service, trustworthy establishment, professional operation. It signals regulatory compliance and responsible gambling. Not flashy energy or manipulative fun - it's straightforward and honest. That builds trust tremendously for my demographic.",
        "q5": 5,
        "q6": "The reason black works so well for trust is because it aligns with how legitimate financial and professional services present themselves. Compare it to banking apps - they use blues and blacks, not reds and golds. This says Yes Games understands they're handling people's money and should act accordingly. Perfect choice."
    },
    "lars": {
        "persona_type": "Trust Seeker",
        "name": "Lars",
        "age": 44,
        "style": "Skeptical/Critical",
        "q1": "This concerns me because while it looks professional, appearance doesn't equal security. I'd need to audit their actual security practices.",
        "q2": "Security-wise, color is irrelevant. Black might signal professionalism, but it could also be sophisticated branding covering poor security. I'm cautious.",
        "q3": "Yes, high contrast means good visibility. But finding it easily doesn't mean trusting it easily.",
        "q4": "Premium positioning obvious. Trust? Can't determine trust from an icon color - need to see their two-factor authentication, data encryption, license verification. Black can signal either quality OR just good marketing hiding problems.",
        "q5": 3,
        "q6": "I don't trust visual branding as a security signal. Black looks professional but I've seen too many slick-looking platforms with terrible security. Show me your security audit reports and open-source your code before I care about your icon color."
    },
    "kirsten": {
        "persona_type": "Trust Seeker",
        "name": "Kirsten",
        "age": 49,
        "style": "Enthusiastic but Trust-Conscious",
        "q1": "Love it! Looks very professional and trustworthy! But only if they actually are trustworthy!",
        "q2": "Black feels safe and established! I love that it's not using flashy manipulation tactics! It shows they respect responsible gambling!",
        "q3": "Yes! Would find it easily! The professional look helps me trust it's legitimate!",
        "q4": "Premium definitely! Trust is the big one - looks like a legitimate, licensed platform! Must show responsible gambling tools though! Not particularly energetic but that's GOOD - gambling should be controlled, not hyperenergetic!",
        "q5": 5,
        "q6": "Trust is key! Black helps build that trust because it looks professional and established! Love it, but only if their responsible gambling policies match the professional appearance!"
    },
    "soren": {
        "persona_type": "Trust Seeker",
        "name": "Søren",
        "age": 51,
        "style": "Analytical/Comparative",
        "q1": "Compared to other platforms, black signals premium positioning similar to financial services. Analysis indicates this targets higher-trust, higher-value customer segments.",
        "q2": "The data indicates black has highest trust correlation in professional services categories (banking 0.89, legal 0.84, consulting 0.91). Applied to gambling, this positions it as professional service rather than entertainment, which aligns with responsible gambling frameworks.",
        "q3": "Recognition testing would score high (contrast analysis: excellent). More importantly, brand recall studies show distinctive colors (either very bright or very minimal like black) score highest. This would perform well.",
        "q4": "Compared to other platforms: Premium (9/10 vs. industry average 5/10), Trust (8/10 vs. average 4/10), Professional (9/10 vs. average 5/10), Fun/Energy (2/10 vs. average 8/10). This clearly targets trust-conscious, professional segment over entertainment-seeking segment.",
        "q5": 5,
        "q6": "Analysis shows black is optimal for trust-building in financial services context. For gambling, this is strategic if targeting 40+ demographic with higher lifetime value and lower churn. Risk: under-appeal to 18-35 entertainment segment. Recommendation: Black for main brand, could use color variations in-app for game categories."
    },

    # CROSS-ENTERTAINMENT (5)
    "marcus": {
        "persona_type": "Cross-Entertainment",
        "name": "Marcus",
        "age": 25,
        "style": "Brief/Direct",
        "q1": "Clean. Modern. All-in-one feel.",
        "q2": "Black feels unified - works for sports, casino, everything.",
        "q3": "Yeah, stands out.",
        "q4": "Premium. Professional. Versatile.",
        "q5": 4,
        "q6": "Good for unified platform. Neutral enough to cover all entertainment types."
    },
    "sebastian": {
        "persona_type": "Cross-Entertainment",
        "name": "Sebastian",
        "age": 32,
        "style": "Detailed/Explanatory",
        "q1": "The way it should work is that a unified platform needs neutral branding that doesn't favor one vertical over another. Black does this perfectly - it's not 'sports red' or 'casino gold,' it's premium neutral that encompasses everything.",
        "q2": "Because users need to feel the platform serves multiple entertainment purposes equally. Black signals 'comprehensive platform' rather than specialized service. It's the visual equivalent of saying 'we do everything at premium quality.'",
        "q3": "From a user perspective, yes. The distinctiveness helps. More importantly, when users think 'where's my all-in-one entertainment app,' black's professional appearance matches that mental model better than specialized colors.",
        "q4": "Premium positioning crucial for unified platforms - says 'we invested in doing everything well, not just one thing.' Trust is high because professionalism. It's not hyper-energetic but that's good - different users want different things (sports intensity vs. casino fun vs. esports excitement). Black accommodates all without favoring one.",
        "q5": 5,
        "q6": "For cross-entertainment platforms, black is strategically brilliant. It avoids category pigeonholing while signaling premium multi-vertical capability. Think Netflix black, not Candy Crush colors. Perfect choice for unified platform positioning."
    },
    "nanna": {
        "persona_type": "Cross-Entertainment",
        "name": "Nanna",
        "age": 28,
        "style": "Skeptical/Critical",
        "q1": "This claims to be unified but black might just be them being lazy about distinct branding for each vertical.",
        "q2": "Skeptical of integration because most platforms say 'all-in-one' but deliver fragmented experience. Black doesn't tell me if they actually integrated well or just slapped different products together.",
        "q3": "Yes, recognizable. But the icon doesn't tell me anything about the actual user experience quality.",
        "q4": "Premium positioning obvious, but might be style over substance. Trust depends on execution, not color. I need to see if the UX actually delivers unified experience before caring about the black icon.",
        "q5": 3,
        "q6": "Black works theoretically for unified platforms, but I've seen too many apps with nice icons and terrible integration. Show me seamless product switching, unified wallet, consistent design system - then I'll care about your black branding."
    },
    "alexander": {
        "persona_type": "Cross-Entertainment",
        "name": "Alexander",
        "age": 24,
        "style": "Enthusiastic/Emotional",
        "q1": "YO! This is CLEAN! Love how it could work for everything - sports, slots, esports!",
        "q2": "Black is POWERFUL! Perfect for streaming content too! Works for all entertainment! Epic choice!",
        "q3": "100%! Would totally pop on screen! Easy to find when I need to switch between sports and casino!",
        "q4": "PREMIUM vibes! Professional! It's like 'we do EVERYTHING at high level!' Not limiting to one vibe! That versatility is FIRE!",
        "q5": 5,
        "q6": "Amazing how it has everything covered! Love the all-in-one energy! Black works for all content types! Streamer-approved!"
    },
    "ida": {
        "persona_type": "Cross-Entertainment",
        "name": "Ida",
        "age": 30,
        "style": "Analytical/Comparative",
        "q1": "Compared to separate apps (red sports app + gold casino app + green esports app), unified black signals integrated platform strategy. Value analysis indicates reduced cognitive load.",
        "q2": "Integration metrics show users prefer unified branding for cross-product usage. Black scores highest for 'works across all categories' (8.7/10) vs. specialized colors (4.2/10 outside primary category).",
        "q3": "Compared to maintaining multiple app icons, single black icon improves efficiency. Recognition studies show distinctive unified branding increases cross-product engagement by 34%.",
        "q4": "Value analysis indicates: Premium positioning (8/10), Professional integration (9/10), Category versatility (9/10). The unified black approach signals 'comprehensive platform' vs. 'collection of products.' This creates higher perceived value.",
        "q5": 5,
        "q6": "Compared to separate apps, unified black maximizes: (1) Brand consistency across verticals, (2) Premium positioning across all categories, (3) Reduced user confusion, (4) Professional 'super-app' perception. Optimal choice for cross-entertainment strategy."
    }
}

def main():
    """Generate all interview results"""

    base_path = Path("/Users/georgiyescom/Work/Skills Library/skills-library/results/2025-11-06_black-icon-testing")

    # Format results
    formatted_results = []
    for persona_id, data in INTERVIEW_RESPONSES.items():
        formatted_results.append({
            "persona": persona_id,
            "persona_type": data["persona_type"],
            "name": data["name"],
            "age": data["age"],
            "communication_style": data["style"],
            "responses": {
                "q1_first_reaction": data["q1"],
                "q2_feeling_context": data["q2"],
                "q3_recognition": data["q3"],
                "q4_associations": data["q4"],
                "q5_rating": data["q5"],
                "q6_other_thoughts": data["q6"]
            }
        })

    # Save results
    output_file = base_path / "interview_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(formatted_results, f, indent=2, ensure_ascii=False)

    print(f"✓ Generated {len(formatted_results)} interview responses")
    print(f"✓ Saved to: {output_file}")

    # Calculate aggregate statistics
    ratings = [data["q5"] for data in INTERVIEW_RESPONSES.values()]
    avg_rating = sum(ratings) / len(ratings)

    # Group by persona type
    persona_types = {}
    for data in INTERVIEW_RESPONSES.values():
        ptype = data["persona_type"]
        if ptype not in persona_types:
            persona_types[ptype] = []
        persona_types[ptype].append(data["q5"])

    print(f"\n{'='*60}")
    print(f"OVERALL RATING: {avg_rating:.2f}/5.00")
    print(f"{'='*60}")

    print("\nRATINGS BY PERSONA TYPE:")
    for ptype, ratings_list in persona_types.items():
        avg = sum(ratings_list) / len(ratings_list)
        print(f"  {ptype}: {avg:.2f}/5.00 (n={len(ratings_list)})")

    return formatted_results

if __name__ == "__main__":
    main()
