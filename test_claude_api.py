import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    print("Error: No ANTHROPIC_API_KEY found in environment variables or .env file.")
    exit(1)

print(f"Using API key: {api_key[:8]}...{api_key[-4:]}")

# Initialize the Anthropic client
client = Anthropic(api_key=api_key)

# Simple test message
test_prompt = "Hello Claude! Please respond with a short greeting and tell me what today's date is. Today is March 6th, 2025."

print("\nSending test message to Claude 3 Sonnet...")
try:
    # Create a message using the Claude 3 Sonnet model
    message = client.messages.create(
        model="claude-3-sonnet-20240229",  # Note: There's a deprecation warning for this model
        max_tokens=100,
        messages=[
            {"role": "user", "content": test_prompt}
        ]
    )
    
    # Print the response
    print("\n=== Claude's Response ===\n")
    print(message.content[0].text)
    print("\n=== End of Response ===\n")
    print("Test completed successfully!")
    
except Exception as e:
    print(f"\nError: {str(e)}")
