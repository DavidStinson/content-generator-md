import json
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

def read_example_content(file_path):
    """Read example content from a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Truncate to a reasonable size for an example
            if len(content) > 1000:
                content = content[:1000] + "\n...\n[Example truncated for brevity]"
            return content
    except Exception as e:
        print(f"Error reading example content from {file_path}: {e}")
        return "Example content not available."

def generate_improved_prompt(topic, file_type):
    """Generate an improved prompt with formatting instructions and examples"""
    
    # Example paths
    example_paths = {
        'lesson': 'sample_content/GA Lesson Examples/react-router-dom-main/concepts/README.md',
        'lab': 'sample_content/GA Lab Examples/django-crud-drf-lab-main/README.md'
    }
    
    # Default to lesson if file_type not found
    example_path = example_paths.get(file_type.lower(), example_paths['lesson'])
    
    # Read example content
    example_content = read_example_content(example_path)
    
    # Basic information
    if file_type.lower() == 'lesson':
        learning_objectives = [
            "Understand the core concepts of " + topic,
            "Implement basic " + topic + " functionality",
            "Debug common issues with " + topic
        ]
        
        format_instructions = """
FORMAT STRUCTURE:
- Begin with: <h1>
  <span class="headline">[MAIN TITLE]</span>
  <span class="subhead">[SUBTITLE]</span>
</h1>
- Include a metadata table with: Title, Type, Duration, Author
- Format learning objectives as: **Learning objective:** By the end of this lesson, students will [OBJECTIVES]
- Use the GA logo at the top: ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)
- Format notes as: > 📚 *[NOTE TEXT]*
- Use proper heading hierarchy (h1, h2, h3)
- Include code blocks with proper syntax highlighting
- Use bullet points for lists
- Include diagrams and images with proper captions
"""
    else:  # lab
        learning_objectives = [
            "Build a functional " + topic + " application",
            "Implement key features of " + topic,
            "Test and debug a " + topic + " implementation"
        ]
        
        format_instructions = """
FORMAT STRUCTURE:
- Begin with the GA logo: ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)
- Include a metadata table with: Title, Type, Duration, Author
- Format as a multi-day lab with clear day-by-day breakdowns
- Include detailed learning objectives
- Provide step-by-step instructions for each task
- Include submission instructions at the end
- Use code blocks with proper syntax highlighting
- Include diagrams and images where appropriate
"""
    
    # Basic prompt
    basic_prompt = f"Generate a {file_type} on {topic}. Learning objectives: {', '.join(learning_objectives)}"
    
    # Content metrics
    metrics_prompt = "The content should be approximately 800 words with a text-to-code ratio of 0.7. Include 2 images and 1 diagram."
    
    # Example prompt
    example_prompt = f"""
EXAMPLE STRUCTURE:
The following is an example of how the content should be structured and formatted:

{example_content}

Your generated content should follow a similar structure and formatting style.
"""
    
    # Standards prompt
    standards_prompt = """
CONTENT STANDARDS:
- Follow 30% theory, 70% hands-on practice ratio
- Write in American English
- Include diagrams and visuals to illustrate points
- Begin with clear learning objectives
- Write for instructor live delivery over Zoom
- Ensure content is engaging and interactive
- Include practical examples and demonstrations
- Provide opportunities for students to apply what they've learned
- Ensure the content follows a logical flow
- Include references to additional resources where appropriate
"""
    
    # Combine all prompt components
    full_prompt = f"""
{basic_prompt}

{metrics_prompt}

{format_instructions}

{standards_prompt}

{example_prompt}

Please generate complete, well-structured content that follows all the guidelines above.
""".strip()
    
    return full_prompt

def generate_content_with_claude(prompt):
    """Generate content using Claude 3 Sonnet"""
    try:
        # Create a message using the Claude 3 Sonnet model
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=4000,  # Increased token limit for longer content
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Return the generated content
        return message.content[0].text
    except Exception as e:
        return f"Error generating content: {str(e)}"

def save_generated_content(content, filename, output_dir="generated_content"):
    """Save generated content to a file"""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Save content to file
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Content saved to {filepath}")
        return filepath
    except Exception as e:
        print(f"Error saving content to {filepath}: {e}")
        return None

def main():
    # Test parameters
    topic = "Django REST Framework"
    file_type = "lab"  # or "lesson"
    
    print(f"Generating improved prompt for a {file_type} on {topic}...")
    
    # Generate improved prompt
    prompt = generate_improved_prompt(topic, file_type)
    
    print(f"\nGenerated prompt:\n{prompt}\n")
    
    # Generate content using Claude
    print("Sending prompt to Claude 3 Sonnet...")
    content = generate_content_with_claude(prompt)
    
    # Print the generated content
    print("\n=== Generated Content ===\n")
    print(content)
    print("\n=== End of Generated Content ===\n")
    
    # Save generated content
    filename = f"test_improved_{file_type}_{topic.replace(' ', '_')}.md"
    save_generated_content(content, filename)
    
    print("\nContent generation complete!")

if __name__ == "__main__":
    main()
