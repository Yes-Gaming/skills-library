#!/usr/bin/env python3
"""
BLACK App Icon Testing - 25 Parallel Persona Interviews
Simulates authentic user interviews using Claude API
"""

import anthropic
import os
import json
import asyncio
from pathlib import Path

# Personas list
PERSONAS = [
    "emma", "lucas", "sofie", "mikkel", "marie",  # Casual Entertainer
    "thomas", "peter", "kasper", "morten", "nikolaj",  # Sports Enthusiast
    "anna", "viktor", "katrine", "oliver", "caroline",  # Casino Explorer
    "jens", "hanne", "lars", "kirsten", "soren",  # Trust Seeker
    "marcus", "sebastian", "nanna", "alexander", "ida"  # Cross-Entertainment
]

def conduct_interview(persona_name: str, prompt_path: str, api_key: str) -> dict:
    """Conduct a single interview with Claude API"""

    # Read the prompt
    with open(prompt_path, 'r') as f:
        prompt = f.read()

    # Initialize Anthropic client
    client = anthropic.Anthropic(api_key=api_key)

    # Conduct interview
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        temperature=1.0,  # Higher temperature for more natural variation
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    response_text = message.content[0].text

    return {
        "persona": persona_name,
        "response": response_text,
        "tokens_used": message.usage.input_tokens + message.usage.output_tokens
    }

async def run_all_interviews():
    """Run all 25 interviews in parallel"""

    # Get API key from environment
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")

    base_path = Path("/Users/georgiyescom/Work/Skills Library/skills-library/results/2025-11-06_black-icon-testing")

    # Create list of tasks
    tasks = []
    for persona in PERSONAS:
        prompt_path = base_path / f"prompt_{persona}.txt"
        tasks.append((persona, prompt_path))

    print(f"Starting {len(tasks)} parallel interviews...")
    print("=" * 60)

    # Run interviews sequentially (to avoid rate limits, but quickly)
    results = []
    for i, (persona, prompt_path) in enumerate(tasks, 1):
        print(f"[{i}/{len(tasks)}] Interviewing {persona.upper()}...")
        try:
            result = conduct_interview(persona, prompt_path, api_key)
            results.append(result)
            print(f"  ✓ {persona} completed ({result['tokens_used']} tokens)")
        except Exception as e:
            print(f"  ✗ {persona} failed: {e}")
            results.append({
                "persona": persona,
                "error": str(e)
            })

    print("=" * 60)
    print(f"Completed {len(results)} interviews")

    # Save all results
    output_file = base_path / "interview_results.json"
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {output_file}")

    return results

if __name__ == "__main__":
    asyncio.run(run_all_interviews())
