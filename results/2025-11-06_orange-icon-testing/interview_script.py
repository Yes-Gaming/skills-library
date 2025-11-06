#!/usr/bin/env python3
"""
ORANGE App Icon Testing - Persona Interview Script
Interviews 25 personas about ORANGE background app icon with YES logotype
"""

import json
import sys
from datetime import datetime

# Persona definitions - 25 personas (5 from each type)
PERSONAS = {
    # CASUAL ENTERTAINER (5)
    "emma": {
        "name": "Emma",
        "type": "Casual Entertainer",
        "age": 24,
        "occupation": "Retail supervisor at H&M",
        "style": "Brief/Direct",
        "voice_pattern": "Like it / Don't like it / It's fine",
        "key_concern": "Don't want anything complicated or time-consuming"
    },
    "lucas": {
        "name": "Lucas",
        "type": "Casual Entertainer",
        "age": 27,
        "occupation": "Junior UX designer at tech startup",
        "style": "Detailed/Explanatory",
        "voice_pattern": "Well, I think the reason is... because when you look at...",
        "key_concern": "Poor UX and cluttered interfaces annoy me"
    },
    "sofie": {
        "name": "Sofie",
        "type": "Casual Entertainer",
        "age": 23,
        "occupation": "Marketing student at Copenhagen Business School",
        "style": "Skeptical/Critical",
        "voice_pattern": "This feels like... / I don't trust this because...",
        "key_concern": "Too many apps try to manipulate you with flashy stuff"
    },
    "mikkel": {
        "name": "Mikkel",
        "type": "Casual Entertainer",
        "age": 22,
        "occupation": "Bartender at popular nightclub",
        "style": "Enthusiastic/Emotional",
        "voice_pattern": "This is awesome! / Love it! / So cool!",
        "key_concern": "Boring games are a total buzzkill"
    },
    "marie": {
        "name": "Marie",
        "type": "Casual Entertainer",
        "age": 26,
        "occupation": "Data analyst at Danske Bank",
        "style": "Analytical/Comparative",
        "voice_pattern": "If we compare this to... / Looking at the options...",
        "key_concern": "Need transparency in RTP and clear information"
    },

    # SPORTS ENTHUSIAST (5)
    "thomas": {
        "name": "Thomas",
        "type": "Sports Enthusiast",
        "age": 29,
        "occupation": "Personal trainer",
        "style": "Brief/Direct",
        "voice_pattern": "Good / Bad / Works for me",
        "key_concern": "App needs to be fast during live matches - no lag"
    },
    "peter": {
        "name": "Peter",
        "type": "Sports Enthusiast",
        "age": 32,
        "occupation": "Software developer, football fanatic",
        "style": "Detailed/Explanatory",
        "voice_pattern": "The way I see it... because if you analyze...",
        "key_concern": "Need comprehensive statistics and market depth"
    },
    "kasper": {
        "name": "Kasper",
        "type": "Sports Enthusiast",
        "age": 27,
        "occupation": "Journalist at sports media outlet",
        "style": "Skeptical/Critical",
        "voice_pattern": "Most betting apps... but this one... / I'm skeptical because...",
        "key_concern": "Too many sites are predatory or have hidden terms"
    },
    "morten": {
        "name": "Morten",
        "type": "Sports Enthusiast",
        "age": 26,
        "occupation": "Sports coach for youth football",
        "style": "Enthusiastic/Emotional",
        "voice_pattern": "YES! This is it! / Absolutely love... / Amazing!",
        "key_concern": "Has to capture the emotion and energy of the game"
    },
    "nikolaj": {
        "name": "Nikolaj",
        "type": "Sports Enthusiast",
        "age": 34,
        "occupation": "Financial analyst, data-driven bettor",
        "style": "Analytical/Comparative",
        "voice_pattern": "Compared to Platform X... / The metrics show...",
        "key_concern": "Need accurate odds, deep markets, and reliable data feeds"
    },

    # CASINO EXPLORER (5)
    "anna": {
        "name": "Anna",
        "type": "Casino Explorer",
        "age": 25,
        "occupation": "Graphic designer",
        "style": "Brief/Direct",
        "voice_pattern": "Looks good / Don't like it / Too plain",
        "key_concern": "Boring games or poor graphics turn me off immediately"
    },
    "viktor": {
        "name": "Viktor",
        "type": "Casino Explorer",
        "age": 28,
        "occupation": "Game developer, appreciates design",
        "style": "Detailed/Explanatory",
        "voice_pattern": "The reason this works is... because technically...",
        "key_concern": "Poor UX or lazy game design frustrates me"
    },
    "katrine": {
        "name": "Katrine",
        "type": "Casino Explorer",
        "age": 24,
        "occupation": "Psychology student",
        "style": "Skeptical/Critical",
        "voice_pattern": "This seems designed to... / I'm suspicious of...",
        "key_concern": "Hate when apps use psychological tricks to keep you playing"
    },
    "oliver": {
        "name": "Oliver",
        "type": "Casino Explorer",
        "age": 22,
        "occupation": "Esports content creator",
        "style": "Enthusiastic/Emotional",
        "voice_pattern": "Epic! / Fire! / This slaps! / Love it!",
        "key_concern": "Needs to be visually stunning and constantly new content"
    },
    "caroline": {
        "name": "Caroline",
        "type": "Casino Explorer",
        "age": 29,
        "occupation": "Mathematics teacher",
        "style": "Analytical/Comparative",
        "voice_pattern": "Statistically... / Compared to... / The numbers show...",
        "key_concern": "Need transparent RTP information and fair games"
    },

    # TRUST SEEKER (5)
    "jens": {
        "name": "Jens",
        "type": "Trust Seeker",
        "age": 47,
        "occupation": "Small business owner (plumbing)",
        "style": "Brief/Direct",
        "voice_pattern": "Trustworthy / Looks secure / Seems legitimate",
        "key_concern": "Must be licensed, secure, and trustworthy"
    },
    "hanne": {
        "name": "Hanne",
        "type": "Trust Seeker",
        "age": 52,
        "occupation": "Senior accountant",
        "style": "Detailed/Explanatory",
        "voice_pattern": "The reason I trust/don't trust is... because when you consider...",
        "key_concern": "Need transparent terms, visible licensing, clear responsible gambling tools"
    },
    "lars": {
        "name": "Lars",
        "type": "Trust Seeker",
        "age": 44,
        "occupation": "IT security consultant",
        "style": "Skeptical/Critical",
        "voice_pattern": "This concerns me because... / Security-wise... / I don't trust this because...",
        "key_concern": "Most gambling sites have terrible security or hidden practices"
    },
    "kirsten": {
        "name": "Kirsten",
        "type": "Trust Seeker",
        "age": 49,
        "occupation": "Kindergarten director",
        "style": "Enthusiastic but Trust-Conscious",
        "voice_pattern": "Love it, but only if... / Looks fun AND safe / Trust is key!",
        "key_concern": "Must show responsible gambling messages and limits"
    },
    "soren": {
        "name": "Søren",
        "type": "Trust Seeker",
        "age": 51,
        "occupation": "Financial advisor",
        "style": "Analytical/Comparative",
        "voice_pattern": "Compared to other platforms... / The data indicates... / Analysis shows...",
        "key_concern": "Need detailed payout information, RTP transparency, audit reports"
    },

    # CROSS-ENTERTAINMENT (5)
    "marcus": {
        "name": "Marcus",
        "type": "Cross-Entertainment",
        "age": 25,
        "occupation": "Junior graphic designer at digital agency",
        "style": "Brief/Direct",
        "voice_pattern": "All-in-one / Unified / Integrated well",
        "key_concern": "Hate switching between apps - needs to be unified"
    },
    "sebastian": {
        "name": "Sebastian",
        "type": "Cross-Entertainment",
        "age": 32,
        "occupation": "Product manager at tech company",
        "style": "Detailed/Explanatory",
        "voice_pattern": "The way it should work is... because users need...",
        "key_concern": "Platform integration and sync across devices is critical"
    },
    "nanna": {
        "name": "Nanna",
        "type": "Cross-Entertainment",
        "age": 28,
        "occupation": "UX researcher",
        "style": "Skeptical/Critical",
        "voice_pattern": "This claims to be unified but... / Skeptical of integration because...",
        "key_concern": "Platforms claim integration but deliver fragmented experience"
    },
    "alexander": {
        "name": "Alexander",
        "type": "Cross-Entertainment",
        "age": 24,
        "occupation": "Twitch streamer / content creator",
        "style": "Enthusiastic/Emotional",
        "voice_pattern": "Amazing how it has everything! / Love the all-in-one! / Epic!",
        "key_concern": "Needs to be content-worthy and shareable across platforms"
    },
    "ida": {
        "name": "Ida",
        "type": "Cross-Entertainment",
        "age": 30,
        "occupation": "Business analyst",
        "style": "Analytical/Comparative",
        "voice_pattern": "Compared to separate apps... / Integration metrics show... / Value analysis indicates...",
        "key_concern": "Need data consistency and unified account management"
    }
}

QUESTIONS = [
    "What's your first reaction when you see an ORANGE app icon with 'YES' on your home screen?",
    "How does the color ORANGE make you feel in a gaming and entertainment context?",
    "Would an ORANGE icon help you find and recognize the Yes Games app quickly on your phone?",
    "Does ORANGE give you any specific associations? (energy, fun, caution, cheap, premium, trust, etc.)",
    "On a scale of 1-5, how would you rate an ORANGE app icon for Yes Games? (1=poor, 5=excellent)",
    "Any other thoughts about ORANGE as the brand color for Yes Games?"
]

def generate_persona_response(persona_key, question_num):
    """Generate authentic response based on persona characteristics"""
    persona = PERSONAS[persona_key]
    question = QUESTIONS[question_num]

    # Response templates based on persona style and question
    responses = {
        # Q1: First reaction
        0: {
            "emma": "Orange? It's bright. Catches the eye I guess.",
            "lucas": "Well, orange is interesting because it's high-contrast and definitely stands out among other app icons. From a design perspective, it's attention-grabbing without being as aggressive as red.",
            "sofie": "Orange feels very marketing-heavy to me. Like it's trying too hard to get attention. Makes me think of cheap telecom brands or budget airlines.",
            "mikkel": "Oh wow, orange! That's bold! I love how it pops! Very energetic and fun!",
            "marie": "Orange is a strategic choice. If I compare it to competitors who use red, yellow, or blue, orange is definitely differentiating. It's visible.",

            "thomas": "Orange. Bold choice. Stands out.",
            "peter": "Orange is strategically interesting because in the Danish market, most sports betting apps use dark colors or red. This would differentiate from Bet365's green, Unibet's green, and others. The visibility is strong.",
            "kasper": "Orange immediately makes me think of budget brands. Telecom companies use orange. I'm skeptical it conveys the right premium or trustworthy image for gambling.",
            "morten": "ORANGE! That's awesome! Super energetic! Love how it stands out - perfect for getting pumped about betting!",
            "nikolaj": "Orange offers good differentiation in a market dominated by red and dark blue. From a visibility standpoint, it ranks high. Comparing to competitor color schemes, it's distinctive.",

            "anna": "Orange is bold. Very visible. Could work if executed well.",
            "viktor": "Orange is technically a good choice for visibility and attention. The reason it works is because it sits between the warmth of red and the brightness of yellow, creating energy without aggression. Design-wise, it's smart.",
            "katrine": "Orange feels manipulative to me. It's the color of urgency and 'act now' marketing tactics. I'm suspicious of why they'd choose something so psychologically activating.",
            "oliver": "ORANGE IS FIRE! Love it! So bright and eye-catching! Epic choice!",
            "caroline": "Statistically, orange is less common in gaming apps, which gives it differentiation value. Compared to the oversaturated red market, orange is distinctive.",

            "jens": "Orange is different. Not sure how I feel about it yet. Need to see if it looks professional.",
            "hanne": "The reason I'm uncertain about orange is because when you consider traditional gambling and gaming colors, orange isn't commonly associated with trust or security. Red and gold are traditional, green suggests money and go-ahead. Orange is more retail or telecommunications.",
            "lars": "Security-wise, orange doesn't convey trust to me. It feels more commercial, more sales-oriented. I'm concerned it might signal a less serious platform.",
            "kirsten": "Orange is bright and fun! But trust is key - does orange feel trustworthy? I need to see it feel safe too.",
            "soren": "Compared to other platforms that use darker, more conservative colors to convey trust and professionalism, orange is unconventional. The data on color psychology suggests orange is energizing but not necessarily trust-building.",

            "marcus": "Orange. Unified and bright. Could work for an all-in-one platform.",
            "sebastian": "The way orange should work for a unified platform is it needs to convey versatility because users need to feel it covers sports, casino, and entertainment. Orange is energetic enough for that, but it needs to avoid feeling too playful or non-serious.",
            "nanna": "This claims to be a bold choice, but I'm skeptical of orange because it's been overused by budget brands. Does it actually convey premium multi-platform experience or just 'cheap and cheerful'?",
            "alexander": "ORANGE! Amazing! Love how bold it is! Perfect for streaming content - super visible and energetic!",
            "ida": "Compared to separate apps with different branding, one orange icon for everything is actually good integration strategy. Value analysis indicates strong brand consistency."
        },

        # Q2: How does orange make you feel?
        1: {
            "emma": "Energetic. Maybe too energetic. It's loud.",
            "lucas": "Orange conveys energy and optimism. Psychologically, it's associated with enthusiasm and excitement, which fits gaming and entertainment. But it can also feel cheap if not executed with the right shade and design quality.",
            "sofie": "Orange feels pushy to me. Like discount sales and 'limited time offers.' In entertainment it might work, but it feels manipulative.",
            "mikkel": "Orange makes me feel PUMPED! It's fun, exciting, energetic! Perfect for gaming!",
            "marie": "Orange creates a sense of energy and approachability. Compared to aggressive red or neutral blue, it's balanced. Looking at color psychology data, it stimulates activity without anxiety.",

            "thomas": "Energetic. Active. Good for sports.",
            "peter": "Orange in a sports context conveys action and energy without the aggression of red. It's activating, which fits live betting. The psychological association with movement and dynamism is appropriate for sports engagement.",
            "kasper": "In sports media, orange can feel cheap or secondary. Most premium sports brands avoid it. I'm skeptical it conveys quality.",
            "morten": "Orange feels ELECTRIC! Perfect for the energy of match day! Gets me excited!",
            "nikolaj": "Psychologically, orange rates high on energy and engagement metrics. In sports betting, where excitement and quick decisions matter, it's strategically sound. Compared to calming blues or aggressive reds, it balances activation with approachability.",

            "anna": "Orange feels creative and playful. Could work for fun casino games.",
            "viktor": "The reason orange works in gaming is because it triggers dopamine-associated responses - warmth, reward anticipation, energy. Technically, it's stimulating without being as stress-inducing as red. For casino entertainment, that balance is important.",
            "katrine": "Orange feels designed to keep you engaged and activated. That's exactly the psychological manipulation I'm wary of in gambling apps.",
            "oliver": "Orange is SO HYPE! Makes me feel energized and ready to play! Love the vibe!",
            "caroline": "Orange has psychological associations with creativity and play. Compared to serious gold or aggressive red, it's more casual and fun-focused, which matches casino exploration behavior.",

            "jens": "Orange feels more playful than trustworthy. I'm not sure that's what I want from a betting platform.",
            "hanne": "When you consider how color affects trust perception, orange is energizing but not security-conveying. Green, blue, and even dark red feel more established and trustworthy. Orange feels newer, less proven.",
            "lars": "Orange doesn't convey security to me. It feels commercial and sales-focused rather than professional and secure. This concerns me for a financial transaction platform.",
            "kirsten": "Orange feels fun and friendly, which I love! But only if it also looks safe and responsible. The color itself feels welcoming.",
            "soren": "Analysis shows orange is associated with friendliness and energy, but trust metrics are lower compared to blue or green. For a financial services platform, which gambling essentially is, that's a concern.",

            "marcus": "Orange feels unified and versatile. Works for multiple entertainment types.",
            "sebastian": "The way orange should work emotionally is it needs to feel both exciting for sports/casino and reliable for account management. Users need to feel energized but not overwhelmed.",
            "nanna": "Orange claims to be energizing, but skeptical it can convey both fun entertainment AND serious financial management. Feels like it leans too far toward playful.",
            "alexander": "Orange makes me feel HYPED! Amazing energy! Perfect for all types of gaming content!",
            "ida": "Emotionally, orange provides consistent energy across sports, casino, and social features. Integration-wise, that's valuable - one emotional tone unifying all experiences."
        },

        # Q3: Recognition and findability
        2: {
            "emma": "Yeah, I'd find it. It's bright enough.",
            "lucas": "Absolutely. Orange has high visibility on both iOS and Android home screens. Most apps use blue, red, or dark colors, so orange would stand out. From a findability perspective, it's effective.",
            "sofie": "It would stand out, sure. But standing out and building trust are different things. I could find it, but would I want to open it?",
            "mikkel": "YES! It would totally pop! Super easy to spot! Love how visible it is!",
            "marie": "Looking at typical home screen layouts, orange provides strong contrast. Compared to most app colors, it would be in the top 20% for findability. Data supports high visibility.",

            "thomas": "Yes. Easy to spot. Fast to find. That matters during matches.",
            "peter": "Recognition is crucial for sports betting apps because you often need to access them quickly during live matches. Orange would be highly visible, which reduces friction. That's strategically important for engagement.",
            "kasper": "It would be visible, yes. But most betting apps achieve visibility. The question is whether orange builds the right associations beyond just being easy to find.",
            "morten": "ABSOLUTELY! Would jump right out at me! Perfect for quick access before kick-off!",
            "nikolaj": "Visibility metrics would be high. Compared to competitor apps in similar color families, orange offers 15-20% better distinctiveness. For quick access during time-sensitive betting, that's valuable.",

            "anna": "Very visible. Easy to find. That's important.",
            "viktor": "The technical reason orange aids recognition is contrast ratio and uniqueness in the current app ecosystem. Most entertainment apps cluster around red/blue/purple, so orange sits in a less saturated space, improving recall and findability.",
            "katrine": "It would be easy to find, but that feels intentional - making it impossible to miss or forget. Classic engagement design.",
            "oliver": "SO easy to find! Would literally glow on my home screen! Epic visibility!",
            "caroline": "From a statistical standpoint, orange performs well on findability. Compared to less distinct colors, recognition speed is 20-30% faster.",

            "jens": "I'd find it easily. But does it look like something I trust? That matters more.",
            "hanne": "Recognition is one factor, but when you consider the full user journey, trust and credibility matter more than pure visibility. Orange achieves visibility but I'm uncertain about trust.",
            "lars": "Yes, I'd find it. But high visibility can also mean high profile for a gambling app, which raises privacy concerns. Do I want my gambling app to be the most visible icon on my screen?",
            "kirsten": "I'd find it easily, and that's good! But recognition and trust need to go together. Orange is certainly recognizable.",
            "soren": "Visibility data supports strong findability. However, compared to platforms prioritizing discretion and professionalism, extremely high visibility might not align with certain user segments who value privacy.",

            "marcus": "Very findable. One icon for everything is simple.",
            "sebastian": "Recognition for a unified platform is critical because users need instant access across multiple use cases. Orange's visibility serves that need well - whether opening for sports, casino, or account management.",
            "nanna": "It would be findable, but skeptical whether high visibility is always positive. Some users want discretion with gambling apps.",
            "alexander": "SUPER easy to find! Perfect for quick content access! Love how it stands out!",
            "ida": "Findability metrics support orange. Compared to managing multiple app icons, one highly visible orange icon improves access efficiency by 30-40%."
        },

        # Q4: Specific associations
        3: {
            "emma": "Energy. Maybe too much energy. Bit loud.",
            "lucas": "Orange gives associations of energy, creativity, and optimism. In retail, it's associated with value and approachability. In tech, it can feel innovative or youthful. For entertainment, it leans toward fun and accessible rather than premium or luxury.",
            "sofie": "Cheap. Sales. Discount brands. Telecom companies. 'Act now!' marketing. Not premium or trustworthy.",
            "mikkel": "Energy! Fun! Excitement! Perfect vibes for gaming and entertainment!",
            "marie": "Orange associates with: energy (strong), approachability (moderate), value/affordability (moderate), fun (strong). Less strong: premium, luxury, trust, security. If we compare to gold (premium) or navy (trust), orange optimizes for energy and fun.",

            "thomas": "Energy. Action. Sports. Works.",
            "peter": "Orange in sports contexts associates with: energy, action, movement, warmth, enthusiasm. It's less associated with: tradition, premium, exclusivity. For modern sports betting emphasizing live engagement, the energy association is strong and appropriate.",
            "kasper": "Cheap. Commercial. Sales-oriented. Most premium sports brands avoid orange because it doesn't convey quality or heritage.",
            "morten": "ENERGY! EXCITEMENT! FUN! All the right associations for sports and gaming!",
            "nikolaj": "Association analysis: Energy (95%), Fun (88%), Approachable (82%), Value (65%), Premium (35%), Trust (48%). Compared to brand positioning needs, the energy/fun scores align with entertainment focus, but trust deficit is notable.",

            "anna": "Creative. Playful. Fun. Good for casual gaming.",
            "viktor": "Orange associates with: creativity (design/artistic contexts), playfulness, energy, warmth, friendliness. The technical reason is wavelength sits between aggressive red and cheerful yellow, creating balanced activation. For casual casino gaming, these associations fit well.",
            "katrine": "Urgency. Call-to-action. Psychological activation. Designed to trigger impulse behavior. Those are the associations I see.",
            "oliver": "FUN! ENERGY! HYPE! CREATIVITY! All amazing associations for gaming!",
            "caroline": "Statistical associations: Energy (92%), Creativity (85%), Fun (88%), Affordability (70%), Premium (32%), Trustworthiness (45%). The data shows strong entertainment alignment but weaker premium/trust signals.",

            "jens": "Energy and fun, yes. Trust and security? Not so much. That's my concern.",
            "hanne": "The associations I get from orange are: energy, friendliness, approachability, but also: commercial, sales-oriented, less established. For a gambling platform where I'm trusting them with money, those associations concern me.",
            "lars": "Commercial. Consumer-facing. Retail. Telecommunications. Not financial services. Not security. Not trust. Those associations are concerning for a gambling platform.",
            "kirsten": "Fun and friendly associations, which I like! But trust is the KEY association I need, and orange doesn't strongly convey that.",
            "soren": "Association analysis: Energy (88%), Fun (85%), Commercial (75%), Trust (42%), Security (38%), Premium (35%). Compared to trust-critical platforms, orange significantly underperforms on security and reliability associations, which are paramount for financial transactions.",

            "marcus": "Versatile. Energetic. All-in-one. Modern.",
            "sebastian": "Orange associates with: versatility, energy, modern tech, accessibility. The way it should work for unified platforms is conveying 'everything in one place' - orange's approachability supports that. Users need to feel it's comprehensive and welcoming.",
            "nanna": "Claims versatility, but I associate orange with: cheap, commercial, budget brands. Skeptical it conveys premium multi-platform experience.",
            "alexander": "ENERGY! CREATIVITY! FUN! MODERN! Perfect associations for entertainment platform!",
            "ida": "Association analysis for unified platforms: Energy (90%), Versatility (72%), Modern (78%), Integrated (65%), Premium (40%). Integration metrics are decent, but premium perception gap is notable for high-value users."
        },

        # Q5: Rating 1-5
        4: {
            "emma": "3. It's fine. Not bad, not amazing.",
            "lucas": "I'd give it a 3.5, rounding to 4. The reasoning is that orange achieves strong visibility and energy, which are positives for entertainment. However, it sacrifices some premium perception and trust signals that could matter for user acquisition among certain segments.",
            "sofie": "2. I don't trust it. Feels too commercial and pushy. Like a discount brand.",
            "mikkel": "5! Love it! So energetic and fun! Perfect for gaming!",
            "marie": "Looking at the criteria: Visibility (5), Energy (5), Trust (2), Premium (2), Distinctiveness (5). Overall weighted rating: 3.8, which I'd round to 4. If we compare to ideal entertainment brand colors, it's above average but not optimal.",

            "thomas": "4. Strong visibility and energy. Works for sports.",
            "peter": "I'd rate it 4 out of 5. The reason is: excellent visibility and energy alignment with sports betting's time-sensitive nature, but moderate trust signals which matter for financial transactions. If you analyze user priorities, visibility and engagement score high, trust slightly lower, averaging to 4.",
            "kasper": "2. Too commercial, not premium enough, doesn't convey trust or quality.",
            "morten": "5! LOVE IT! Perfect energy for sports and gaming!",
            "nikolaj": "Rating breakdown: Visibility (5), Energy (5), Distinctiveness (5), Trust (3), Premium (2). Weighted by sports betting priorities (engagement>trust), overall score: 4.2, round to 4.",

            "anna": "4. Bold, visible, creative. Works for casual gaming.",
            "viktor": "Technical rating: 4 out of 5. The reason is strong design fundamentals (contrast, visibility, energy) scoring 5, 5, and 5. However, premium perception scores 2, pulling the average down. For casino exploration focused on fun over luxury, the balance is appropriate, hence 4.",
            "katrine": "2. Too manipulative. Designed for psychological activation, not user wellbeing.",
            "oliver": "5! EPIC! Fire! Love everything about it! Perfect!",
            "caroline": "Statistical rating across criteria: Visibility (5), Energy (5), Fun (5), Trust (2.5), Premium (2). Overall: 3.9, round to 4. Compared to optimal gaming app color profiles, it's above average.",

            "jens": "3. Visible and energetic, but doesn't feel trustworthy enough. I need trust.",
            "hanne": "The reason I'd give it 2.5, rounding to 3, is because while orange achieves visibility (4) and energy (4), it significantly underperforms on trust (2) and security perception (2). When you consider that gambling platforms are essentially financial services requiring high trust, the trust deficit is critical.",
            "lars": "2. Security and trust concerns override any visibility benefits. Orange doesn't convey the professionalism and security I need.",
            "kirsten": "3. Love the fun energy (4), but only if trust is there (2). The average is 3. Trust is KEY!",
            "soren": "Analysis-based rating: Visibility (5), Energy (5), Trust (2), Security (2), Premium (3). Weighted by trust-seeker priorities (trust>energy), overall: 2.8, round to 3. Compared to trust-optimized color schemes, orange underperforms significantly.",

            "marcus": "4. Unified, visible, modern. Works well for all-in-one.",
            "sebastian": "Rating: 4. The way I calculate this is: Visibility (5), Energy (5), Modern appeal (4), Integration perception (4), Trust (3), Premium (2). Users need high visibility and energy for engagement, which orange delivers. The trust gap is manageable with other trust-building elements in design.",
            "nanna": "3. Claims to be bold and modern, but skeptical it conveys premium unified experience. Feels more budget than premium.",
            "alexander": "5! ABSOLUTELY LOVE IT! Perfect for all content types! Amazing!",
            "ida": "Value analysis rating: Visibility (5), Integration clarity (4), Modern appeal (4), Energy (5), Premium (2.5), Trust (3). Overall: 3.9, round to 4. Compared to optimal unified platform branding, orange performs well on key integration metrics."
        },

        # Q6: Other thoughts
        5: {
            "emma": "It's bold. Some people will love it, some won't. I'm neutral.",
            "lucas": "Final thought: orange is a strategic differentiator in a crowded market. It optimizes for visibility and energy, which supports engagement. However, consider whether sacrificing trust signals is worth it. Perhaps pair the bold color with trust-building design elements like clear licensing, security badges, responsible gambling messaging. The color alone isn't the full story.",
            "sofie": "Unless the execution is extremely premium and sophisticated, orange will feel cheap. It's a risky choice. Would need perfect design execution to overcome the budget brand associations.",
            "mikkel": "I think it's an awesome choice! Bold, fun, energetic! Love brands that dare to be different! Orange rocks!",
            "marie": "Final analysis: Orange is data-backed for visibility and engagement. If the strategy prioritizes user acquisition through distinctiveness and energy, it works. If the strategy prioritizes trust and premium perception, consider alternatives. Know your priority metrics.",

            "thomas": "Bold choice. Stands out. That matters in sports betting. I'd use it.",
            "peter": "Strategically, orange makes sense for sports betting if the goal is to emphasize energy, live engagement, and modern appeal over tradition and heritage. It's a younger, more dynamic positioning. Just ensure other trust elements are rock-solid since color alone doesn't build trust.",
            "kasper": "I'd be concerned about brand perception long-term. Orange might get attention initially, but does it build lasting trust and quality associations? I'm skeptical.",
            "morten": "LOVE IT! Bold choices make memorable brands! Orange has so much energy and excitement! Perfect!",
            "nikolaj": "Final analysis: Orange optimizes for differentiation (high value in saturated market) and engagement (critical for retention). Trust metrics are lower but can be offset with strong execution on security messaging, licensing visibility, and professional UX. Overall strategic score: 7.5/10.",

            "anna": "It's a statement color. Confident choice. Could build a strong visual brand if done right.",
            "viktor": "Final technical thought: Orange provides excellent foundation for brand recognition and energy. The execution quality will determine success - shade selection, pairing with typography, overall design sophistication. With premium execution, orange can overcome 'cheap' associations. With poor execution, it will reinforce them.",
            "katrine": "Orange is a deliberate psychological choice designed to activate and engage users frequently. I appreciate the boldness but remain wary of the intentions behind such activating color psychology in gambling.",
            "oliver": "ORANGE IS PERFECT! Love bold brands that stand out! This is the energy gaming needs! Epic choice!",
            "caroline": "Statistical final thought: Orange performs in top 25% for visibility and engagement, bottom 35% for trust and premium. Success depends on whether engagement or trust is the priority business metric. For acquisition-focused growth, orange scores high. For retention of trust-sensitive users, it scores lower.",

            "jens": "I'd need to see how it's executed. The color concerns me on trust, but maybe strong design can fix that.",
            "hanne": "My final thought is this: orange CAN work for a gambling platform, but only if every other element screams trust, security, and professionalism. The color is working against trust, so the design, messaging, licensing visibility, and responsible gambling tools must work twice as hard. Is that the right strategic tradeoff?",
            "lars": "Orange is concerning for trust and security perception. In cybersecurity and financial services, this choice would be questioned. I'd personally be more hesitant to trust a platform with orange branding unless other trust signals were exceptionally strong.",
            "kirsten": "I want to love it because it's fun and energetic! But they MUST pair it with clear trust signals. If they do, it could work. If they don't, the fun won't overcome my trust concerns.",
            "soren": "Final analysis: Orange represents a calculated risk. High reward in terms of differentiation and energy, but significant trust deficit. For Trust Seeker segments (40+, high lifetime value), this is suboptimal. Would recommend testing alternative color schemes that maintain visibility while improving trust metrics. Blue-orange, navy-orange, or darker sophisticated orange might balance both needs better.",

            "marcus": "Orange unifies everything under one bold identity. That clarity is valuable for all-in-one platforms.",
            "sebastian": "Final product thought: Orange works IF the platform execution is seamless. Users need to feel the energy matches the capability. If the platform is buggy or fragmented despite bold branding, the disconnect will be jarring. Orange sets high expectations for integrated, energetic experience.",
            "nanna": "Skeptical orange can deliver premium unified experience perception. Would need exceptional execution to overcome budget/commercial associations. Testing with target users is critical.",
            "alexander": "ORANGE IS PERFECT! Creates strong brand identity across all content! Love the boldness! This is how you stand out!",
            "ida": "Final value analysis: For unified platforms, orange provides 85% color consistency value across verticals, 90% visibility value, but only 55% premium perception value. If the business model prioritizes broad market engagement over premium positioning, orange is strategically sound. If pursuing high-value premium users, consider alternatives."
        }
    }

    return responses[question_num][persona_key]

def conduct_interview(persona_key):
    """Conduct full interview with one persona"""
    persona = PERSONAS[persona_key]

    interview_data = {
        "persona_id": persona_key,
        "persona_name": persona["name"],
        "persona_type": persona["type"],
        "age": persona["age"],
        "occupation": persona["occupation"],
        "communication_style": persona["style"],
        "timestamp": datetime.now().isoformat(),
        "responses": []
    }

    for q_num, question in enumerate(QUESTIONS):
        response = generate_persona_response(persona_key, q_num)
        interview_data["responses"].append({
            "question_number": q_num + 1,
            "question": question,
            "answer": response
        })

    return interview_data

def main():
    """Run all 25 interviews"""
    if len(sys.argv) > 1:
        # Single persona mode
        persona_key = sys.argv[1]
        if persona_key not in PERSONAS:
            print(f"Error: Unknown persona '{persona_key}'")
            sys.exit(1)

        result = conduct_interview(persona_key)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # All personas mode
        results = []
        for persona_key in PERSONAS.keys():
            results.append(conduct_interview(persona_key))

        print(json.dumps(results, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
