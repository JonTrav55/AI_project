import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

messages = [
    types.Content(role="user", parts=[types.Part(text=sys.argv[1])])
]

parser = argparse.ArgumentParser()
parser.add_argument('prompt', help='The user prompt')
parser.add_argument('--verbose', action='store_true', help='Enable verbose output')

args = parser.parse_args()

def main():
    print("Hello from ai-project!")

             
    if len(sys.argv) != 3:
         print("Usage:python3 main.py <your prompt here>")
         sys.exit(1)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if args.verbose:
        print(f"User prompt: {response.text}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.cache_tokens_details}")
    else:
        print(response.text)
        print("Prompt tokens:",response.usage_metadata.prompt_token_count)
        print("Response tokens:",response.usage_metadata.cache_tokens_details)

if __name__ == "__main__":
    main()
