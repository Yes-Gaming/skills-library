#!/usr/bin/env python3
"""
GOLDEN App Icon Testing - Individual Persona Interview
Executes authentic persona-based interviews for Yes Games golden app icon
"""

import anthropic
import os
import json
import sys

def conduct_persona_interview(persona_data, persona_id):
    """Conduct interview with single persona about GOLDEN app icon"""

    client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

    # Build detailed persona context
    persona_context = f"""You are conducting a user interview as {persona_data['name']}, a {persona_data['age']}-year-old from {persona_data['location']}.

YOUR COMPLETE BACKGROUND:
- Occupation: {persona_data['occupation']}
- Income: {persona_data['income']}
- Device: {persona_data['device']}
- Gambling Pattern: {persona_data['gambling_pattern']}
- Motivation: {persona_data['motivation']}
- Key Concern: {persona_data['key_concern']}
- Discovery: {persona_data['discovery']}

YOUR COMMUNICATION STYLE: {persona_data['communication_style']}
YOUR RESPONSE PATTERN: {persona_data['response_pattern']}
YOUR SURVEY VOICE EXAMPLES: {persona_data['survey_voice']}

CRITICAL: Stay completely in character. Use YOUR authentic voice, YOUR concerns, YOUR perspective. Do NOT sound like a formal survey respondent. Be natural, genuine, and true to your personality and background.

---

INTERVIEW CONTEXT:
You're being shown a concept for the Yes Games mobile app icon. The icon features:
- GOLDEN/GOLD colored background
- "YES" logotype in the center
- This would be what you see on your phone's home screen

The interviewer will ask you 6 questions about this GOLDEN app icon concept. Answer each naturally and authentically as yourself."""

    interview_questions = [
        "What's your first reaction when you see a GOLDEN app icon on your home screen?",
        "How does the color GOLDEN make you feel in a gaming or entertainment context?",
        "Would a GOLDEN icon help you find and recognize the Yes Games app quickly on your screen?",
        "Does GOLDEN give you any specific associations - like energy, fun, caution, cheap, premium, trust, or anything else?",
        "On a scale of 1-5, how would you rate this GOLDEN app icon? (1=terrible, 5=excellent)",
        "Any other thoughts or feelings about GOLDEN as the brand color for a gaming app?"
    ]

    conversation_history = []
    responses = {}

    # Conduct interview question by question
    for i, question in enumerate(interview_questions, 1):
        conversation_history.append({
            "role": "user",
            "content": f"{persona_context}\n\n{question}"
        })

        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            temperature=1.0,  # High temperature for natural variation
            messages=conversation_history
        )

        response_text = message.content[0].text
        responses[f"q{i}"] = {
            "question": question,
            "response": response_text
        }

        conversation_history.append({
            "role": "assistant",
            "content": response_text
        })

        # For subsequent questions, just add the question without full context
        if i < len(interview_questions):
            conversation_history.append({
                "role": "user",
                "content": interview_questions[i]
            })
            conversation_history.pop()  # Remove to add next time with just question

    return {
        "persona_id": persona_id,
        "persona_name": persona_data['name'],
        "persona_type": persona_data['persona_type'],
        "persona_style": persona_data['communication_style'],
        "responses": responses
    }

if __name__ == "__main__":
    # Read persona data from command line argument
    persona_json = sys.argv[1]
    persona_id = sys.argv[2]

    persona_data = json.loads(persona_json)

    # Conduct interview
    result = conduct_persona_interview(persona_data, persona_id)

    # Output as JSON
    print(json.dumps(result, indent=2))
