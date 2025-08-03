import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'

client = genai.Client(api_key=api_key)
def get_response():
    if len(sys.argv) > 1 and isinstance(sys.argv[1], str):
        user_input = sys.argv[1]
        messages = [
            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
        ]
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt)
        )
        
        print(response.text)
        if len(sys.argv) > 2 and sys.argv[2].lower() == "--verbose":
            tokenStr = f"User prompt: {user_input} \nPrompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}"
            print(tokenStr)
    else: 
        print("Invalid response. Try actual words ya ding dong.")
        sys.exit(1)

get_response()