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

def generate_prompt_from_metadata(item):
    """Generate a rich prompt based on metadata"""
    
    # Basic prompt template - handle different content types
    if item['file_type'] == 'course_landing':
        # For course landing pages, use course_title instead of topic
        basic_prompt = f"Generate a {item['file_type']} for {item['course_title']}. Course description: {item['course_description']}"
        
        # For course landing pages, use learning_path instead of learning_objectives if available
        if 'learning_path' in item:
            basic_prompt += f". Learning path: {', '.join(item['learning_path'])}"
    else:
        # For other content types, use topic and learning_objectives
        basic_prompt = f"Generate a {item['file_type']} on {item['topic']}. Learning objectives: {', '.join(item['learning_objectives'])}"
    
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
    
    # Add project standards
    standards_prompt = """
    Follow these standards:
    - All lesson markdown should follow consistent brand guidelines
    - All lesson markdown should follow learning design patterns
    - We are a project-based learning organization with 30% theory and 70% applied hands-on practice
    - Content should be in American English
    - Include diagrams and visuals to illustrate points
    - Begin with clear learning objectives
    - Write for instructor live delivery over Zoom
    
    For this example, please keep the response brief (around 200-300 words).
    """
    
    # Combine all prompt components
    full_prompt = f"{basic_prompt} {metrics_prompt} {standards_prompt}".strip()
    
    return full_prompt

def generate_content_with_claude(prompt):
    """Generate content using Claude 3 Sonnet"""
    try:
        # Create a message using the Claude 3 Sonnet model
        message = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=1000,
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
    
    # For this example, we'll just use the first item from the first category
    first_category = list(metadata.keys())[0]
    first_item = metadata[first_category][0]
    
    item_name = first_item.get('topic', first_item.get('course_title', 'unnamed'))
    print(f"\nGenerating content for: {item_name}")
    
    # Generate prompt from metadata
    prompt = generate_prompt_from_metadata(first_item)
    print(f"\nGenerated prompt:\n{prompt}\n")
    
    # Generate content using Claude
    print("Sending prompt to Claude 3 Sonnet...")
    content = generate_content_with_claude(prompt)
    
    # Print the generated content
    print("\n=== Generated Content ===\n")
    print(content)
    print("\n=== End of Generated Content ===\n")
    
    # Save generated content
    filename = f"metadata_example_{item_name.replace(' ', '_')}.md"
    save_generated_content(content, filename)
    
    print("\nContent generation complete!")

if __name__ == "__main__":
    main()
