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

def read_metadata(filepath):
    """Read metadata from a file with error handling"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading metadata file {filepath}: {e}")
        return None

def read_example_content(file_type):
    """Read example content based on file type"""
    example_paths = {
        'lesson': 'sample_content/GA Lesson Examples/react-router-dom-main/concepts/README.md',
        'lab': 'sample_content/GA Lab Examples/django-crud-drf-lab-main/README.md'
    }
    
    # Default to lesson if file_type not found
    path = example_paths.get(file_type, example_paths['lesson'])
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Truncate to a reasonable size for an example
            if len(content) > 1000:
                content = content[:1000] + "\n...\n[Example truncated for brevity]"
            return content
    except Exception as e:
        print(f"Error reading example content from {path}: {e}")
        return "Example content not available."

def generate_format_instructions(file_type):
    """Generate format instructions based on file type"""
    if file_type == 'lesson':
        return """
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
    elif file_type == 'lab':
        return """
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
    else:
        return """
FORMAT STRUCTURE:
- Use proper markdown formatting
- Include clear headings and subheadings
- Format code examples with proper syntax highlighting
- Include diagrams and images where appropriate
"""

def generate_prompt_from_metadata(item):
    """Generate a rich prompt based on metadata with improved formatting instructions"""
    
    # Get file type
    file_type = item.get('file_type', 'lesson').lower()
    
    # Basic prompt template - handle different content types
    if file_type == 'course_landing':
        # For course landing pages, use course_title instead of topic
        basic_prompt = f"Generate a {file_type} for {item['course_title']}. Course description: {item['course_description']}"
        
        # For course landing pages, use learning_path instead of learning_objectives if available
        if 'learning_path' in item:
            basic_prompt += f". Learning path: {', '.join(item['learning_path'])}"
    else:
        # For other content types, use topic and learning_objectives
        basic_prompt = f"Generate a {file_type} on {item['topic']}. Learning objectives: {', '.join(item['learning_objectives'])}"
    
    # Enhanced prompt with content metrics
    if 'content_metrics' in item:
        metrics = item['content_metrics']
        metrics_prompt = (
            f"The content should be approximately {metrics['word_count']} words with a "
            f"text-to-code ratio of {metrics['text_to_code_ratio']}. "
            f"Include {metrics['number_of_images']} images and {metrics['number_of_diagrams']} diagrams."
        )
    else:
        metrics_prompt = ""
    
    # Add format instructions based on file type
    format_prompt = generate_format_instructions(file_type)
    
    # Add example content based on file type
    example_content = read_example_content(file_type)
    example_prompt = f"""
EXAMPLE STRUCTURE:
The following is an example of how the content should be structured and formatted:

{example_content}

Your generated content should follow a similar structure and formatting style.
"""
    
    # Add project standards
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

{format_prompt}

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
    # Load metadata
    metadata_path = 'sample_content/content_metadata'
    metadata = read_metadata(metadata_path)
    
    if not metadata:
        print("Failed to load metadata. Exiting.")
        return
    
    print(f"Loaded metadata with {len(metadata)} categories")
    
    # Ask user which category to generate content for
    print("\nAvailable categories:")
    for i, category in enumerate(metadata.keys()):
        print(f"{i+1}. {category}")
    
    try:
        category_idx = int(input("\nEnter the number of the category to generate content for: ")) - 1
        categories = list(metadata.keys())
        selected_category = categories[category_idx]
    except (ValueError, IndexError):
        print("Invalid selection. Using the first category.")
        selected_category = list(metadata.keys())[0]
    
    print(f"\nSelected category: {selected_category}")
    
    # Ask user which item to generate content for
    items = metadata[selected_category]
    print("\nAvailable items:")
    for i, item in enumerate(items):
        print(f"{i+1}. {item.get('topic', item.get('course_title', 'Unnamed item'))}")
    
    try:
        item_idx = int(input("\nEnter the number of the item to generate content for: ")) - 1
        selected_item = items[item_idx]
    except (ValueError, IndexError):
        print("Invalid selection. Using the first item.")
        selected_item = items[0]
    
    item_name = selected_item.get('topic', selected_item.get('course_title', 'unnamed'))
    print(f"\nGenerating content for: {item_name}")
    
    # Generate prompt from metadata with improved formatting
    prompt = generate_prompt_from_metadata(selected_item)
    print(f"\nGenerated prompt:\n{prompt}\n")
    
    # Ask user if they want to proceed with this prompt
    proceed = input("\nDo you want to proceed with this prompt? (y/n): ").lower()
    if proceed != 'y':
        print("Generation cancelled.")
        return
    
    # Generate content using Claude
    print("Sending prompt to Claude 3 Sonnet...")
    content = generate_content_with_claude(prompt)
    
    # Print the generated content
    print("\n=== Generated Content ===\n")
    print(content)
    print("\n=== End of Generated Content ===\n")
    
    # Save generated content
    file_type = selected_item.get('file_type', 'content')
    filename = f"improved_{file_type}_{item_name.replace(' ', '_')}.md"
    save_generated_content(content, filename)
    
    print("\nContent generation complete!")

if __name__ == "__main__":
    main()
