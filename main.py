import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)

client = genai.Client(api_key=api_key)
def get_response():
    if len(sys.argv) > 1 and isinstance(sys.argv[1], str):
        user_input = sys.argv[1]

        messages = [
            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
        ]
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config=config # We're using the config variable created above
        )
        if not response.function_calls:
            print(response.text)
        else: 
            function_call_part = response.function_calls[0]
            print(f"Calling function: {function_call_part.name}({function_call_part.args}")
        if len(sys.argv) > 2 and sys.argv[2].lower() == "--verbose":
            tokenStr = f"User prompt: {user_input} \nPrompt tokens: {response.usage_metadata.prompt_token_count} \nResponse tokens: {response.usage_metadata.candidates_token_count}"
            print(tokenStr)
    else: 
        print("Invalid response. Try actual words ya ding dong.")
        sys.exit(1)

get_response()