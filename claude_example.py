import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file (if it exists)
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("ANTHROPIC_API_KEY")

# If no API key is found, prompt the user
if not api_key:
    print("No ANTHROPIC_API_KEY found in environment variables.")
    api_key = input("Please enter your Anthropic API key: ")

# Initialize the Anthropic client
client = Anthropic(api_key=api_key)

def generate_content(prompt):
    """
    Generate content using Claude 3 Sonnet
    
    Args:
        prompt (str): The prompt to send to Claude
        
    Returns:
        str: The generated content
    """
    try:
        # Create a message using the Claude 3 Sonnet model
        message = client.messages.create(
            model="claude-3-sonnet-20240229",  # Using the model name as a string
            max_tokens=1000,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Return the generated content
        return message.content[0].text
    except Exception as e:
        return f"Error generating content: {str(e)}"

if __name__ == "__main__":
    # Example prompt based on your content generation project
    prompt = """
    Generate a lab exercise on Python unit testing. 
    Learning objectives: 
    - Understand the basics of unit testing in Python
    - Learn how to use the unittest framework
    - Practice writing test cases for functions
    
    The content should be approximately 1000 words with a text-to-code ratio of 60:40.
    Include 2 images and 1 diagram.
    """
    
    # Generate content
    content = generate_content(prompt)
    
    # Print the generated content
    print("\n=== Generated Content ===\n")
    print(content)
    print("\n=== End of Generated Content ===\n")
