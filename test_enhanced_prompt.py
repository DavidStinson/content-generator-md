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
            if len(content) > 2000:
                content = content[:2000] + "\n...\n[Example truncated for brevity]"
            return content
    except Exception as e:
        print(f"Error reading example content from {file_path}: {e}")
        return "Example content not available."

def generate_format_instructions(file_type):
    """Generate enhanced format instructions based on file type"""
    if file_type == 'lesson':
        return """
FORMAT STRUCTURE:
- Begin with: <h1>
  <span class="headline">[MAIN TITLE]</span>
  <span class="subhead">[SUBTITLE]</span>
</h1>
- Include the GA logo at the top: ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)
- Include a metadata table with: Title, Type, Duration, Author
- Format learning objectives as: **Learning objective:** By the end of this lesson, students will [OBJECTIVES]
- Use proper heading hierarchy (h1, h2, h3)
- Format notes as: > 📚 *[NOTE TEXT]*
- Include code blocks with proper syntax highlighting
- Use bullet points for lists
- Include diagrams and images with proper captions
- Number steps explicitly (e.g., "Step 1:", "Step 2:")
- Include "Try it out" sections after each major step
- Add instructor notes about potential confusion points
- Include timing estimates for each section
- Add "Why This Matters" sections connecting concepts to job skills
"""
    elif file_type == 'lab':
        return """
FORMAT STRUCTURE:
- Begin with the GA logo: ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)
- Include a metadata table with: Title, Type, Duration, Author
- Format as a multi-day lab with clear day-by-day breakdowns
- Include detailed learning objectives
- Include user stories that define functionality from the user's perspective
- Provide step-by-step instructions for each task
- Include submission instructions at the end
- Use code blocks with proper syntax highlighting
- Include diagrams and images where appropriate
- Add hints using expandable sections with <details> tags
- Include checkpoint moments where students can verify their progress
- Add "Challenge" sections for students who want to go deeper
"""
    else:
        return """
FORMAT STRUCTURE:
- Use proper markdown formatting
- Include clear headings and subheadings
- Format code examples with proper syntax highlighting
- Include diagrams and images where appropriate
"""

def generate_enhanced_content_standards():
    """Generate enhanced content standards"""
    return """
CONTENT STANDARDS:
- Follow 30% theory, 70% hands-on practice ratio
- Include at least 5 hands-on activities
- Each concept should be immediately followed by application
- Write in American English
- Include diagrams and visuals to illustrate points
- Begin with clear learning objectives
- Write for instructor live delivery over Zoom
- Ensure content is engaging and interactive
- Include practical examples and demonstrations
- Provide opportunities for students to apply what they've learned
- Ensure the content follows a logical flow
- Include references to additional resources where appropriate
- Frame the lesson within a realistic development scenario
- Include references to industry practices
- Add "Why This Matters" sections connecting concepts to job skills
"""

def generate_enhanced_step_by_step_guidance():
    """Generate enhanced step-by-step guidance"""
    return """
STEP-BY-STEP GUIDANCE:
- Build functionality incrementally, with each step building on the previous one
- Show immediate results after each step (e.g., "Run the code and observe...")
- Provide code snippets at each step, not just at the end
- Include screenshots or descriptions of expected results after key steps
- Use diagrams to show architecture/component relationships
- Highlight what changes between steps
- Include prompts like "Take a minute to consider what this code is doing"
- Explain why certain approaches are used, not just how
- Include notes explaining concepts in context
- Add "Try it out" moments after each significant change
- Include specific questions for students to consider at key points
"""

def generate_enhanced_prompt(topic, file_type):
    """Generate an enhanced prompt with formatting instructions and examples"""
    
    # Example paths
    example_paths = {
        'lesson': 'sample_content/GA Lesson Examples/ikea-app-and-gcp-deploy-content-main/build-express-app.md',
        'lab': 'sample_content/GA Lab Examples/lifting-state-in-react-lab-main/exercise/README.md'
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
        
        format_instructions = generate_format_instructions('lesson')
    else:  # lab
        learning_objectives = [
            "Build a functional " + topic + " application",
            "Implement key features of " + topic,
            "Test and debug a " + topic + " implementation"
        ]
        
        format_instructions = generate_format_instructions('lab')
    
    # Basic prompt
    basic_prompt = f"Generate a {file_type} on {topic}. Learning objectives: {', '.join(learning_objectives)}"
    
    # Content metrics
    metrics_prompt = "The content should be approximately 1000 words with a text-to-code ratio of 0.7. Include 2 images and 1 diagram."
    
    # Enhanced content standards
    standards_prompt = generate_enhanced_content_standards()
    
    # Enhanced step-by-step guidance
    step_by_step_prompt = generate_enhanced_step_by_step_guidance()
    
    # Example prompt
    example_prompt = f"""
EXAMPLE STRUCTURE:
The following is an example of how the content should be structured and formatted:

{example_content}

Your generated content should follow a similar structure and formatting style.
"""
    
    # Combine all prompt components
    full_prompt = f"""
{basic_prompt}

{metrics_prompt}

{format_instructions}

{standards_prompt}

{step_by_step_prompt}

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
    topic = "React State Management"
    file_type = "lab"  # or "lesson"
    
    print(f"Generating enhanced prompt for a {file_type} on {topic}...")
    
    # Generate enhanced prompt
    prompt = generate_enhanced_prompt(topic, file_type)
    
    print(f"\nGenerated prompt:\n{prompt}\n")
    
    # Generate content using Claude
    print("Sending prompt to Claude 3 Sonnet...")
    content = generate_content_with_claude(prompt)
    
    # Print the generated content
    print("\n=== Generated Content ===\n")
    print(content)
    print("\n=== End of Generated Content ===\n")
    
    # Save generated content
    filename = f"test_enhanced_{file_type}_{topic.replace(' ', '_')}.md"
    save_generated_content(content, filename)
    
    print("\nContent generation complete!")

if __name__ == "__main__":
    main()
