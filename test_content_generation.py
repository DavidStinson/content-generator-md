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

# Content generation prompt based on project requirements
content_prompt = """
Generate a short lesson introduction on Python unit testing.

Learning objectives:
- Understand the basics of unit testing in Python
- Learn how to use the unittest framework
- Practice writing test cases for functions

The content should follow these standards:
- Project-based learning with 30% theory and 70% applied hands-on practice
- Content in American English
- Include clear learning objectives at the beginning
- Written for instructor live delivery over Zoom

Please keep the response brief (around 200 words) for this test.
"""

print("\nSending content generation prompt to Claude 3 Sonnet...")
try:
    # Create a message using the Claude 3 Sonnet model
    message = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=500,
        messages=[
            {"role": "user", "content": content_prompt}
        ]
    )
    
    # Print the response
    print("\n=== Generated Content ===\n")
    print(message.content[0].text)
    print("\n=== End of Generated Content ===\n")
    
    # Save the generated content to a file
    output_dir = "generated_content"
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = os.path.join(output_dir, "sample_lesson_intro.md")
    with open(output_file, "w") as f:
        f.write(message.content[0].text)
    
    print(f"Content saved to {output_file}")
    print("Test completed successfully!")
    
except Exception as e:
    print(f"\nError: {str(e)}")
