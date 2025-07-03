#!/usr/bin/env python3
import os
import sys
from google import genai

# --- Configuration ---
MODEL_NAME = "gemma-3n-e4b-it"
SYSTEM_PROMPT = """
You are a silent command-line fixer. Your only output must be the raw, corrected shell command.
Do not add any explanation. Do not add markdown. Your entire response must be ONLY the command itself.
"""
# --- End Configuration ---

def get_gemini_suggestion(failed_command, error_output):
    """Contacts the API to get only the corrected command string."""
    try:
        client = genai.Client()
        full_prompt = f"{SYSTEM_PROMPT}\n\n--- USER'S PROBLEM ---\nCommand: `{failed_command}`\nError: ```{error_output}```\n\nProvide the raw command fix."
        
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=full_prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"Error from API: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    command = sys.argv[1]
    output = sys.argv[2]
    suggestion = get_gemini_suggestion(command, output)
    print(suggestion)
