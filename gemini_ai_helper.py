#!/usr/bin/env python3
import sys
from google import genai

# --- Configuration ---
MODEL_NAME = "gemma-3n-e4b-it"
SYSTEM_PROMPT = """
You are a helpful but slightly tsundere Linux assistant. The user has a question or a goal.
Follow these rules strictly:
1. Provide a brief, one or two-sentence explanation of the best approach.
2. On the very next line, provide the single, most relevant command to achieve the user's goal.
3. The command MUST be raw text. Do NOT wrap it in markdown.
"""
# --- End Configuration ---

def get_gemini_explanation(user_query):
    """Contacts the API to get an explanation and a raw command."""
    try:
        client = genai.Client()
        full_prompt = f"{SYSTEM_PROMPT}\n\n--- USER'S GOAL ---\n{user_query}\n\nProvide the explanation and raw command."
        
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=full_prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"An error occurred while contacting the API:\n{e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gemini_ai_helper.py \"<user query>\"")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    explanation = get_gemini_explanation(query)
    print(explanation)
