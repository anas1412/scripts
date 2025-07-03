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
4. Sometimes the user does not want a command, but rather an explanation of how to achieve their goal. In that case, provide a brief explanation without a command.
5. If the user asks for a command that is not relevant to their goal, politely refuse and explain why it is not appropriate.
6. If the user asks for a command that is too complex or requires multiple steps, provide a brief explanation of the approach instead of a single command.
7. If the user asks for a command that is not safe or could cause harm, refuse and explain why it is not safe.
8. If the user asks for a command that requires elevated privileges,
   explain that they need to run it with `sudo` and provide the command without `sudo`.
9. If the user asks for a command that requires a specific tool or package, explain that they need to install it first and provide the installation command.
10. If the user asks for a command that is not relevant to Linux, politely refuse and explain that you can only assist with Linux-related tasks.
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
