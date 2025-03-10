import json
import os
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("ANTHROPIC_API_KEY")

# If no API key is found, prompt the user
if not api_key:
    print("No ANTHROPIC_API_KEY found in environment variables.")
    api_key = input("Please enter your Anthropic API key: ")

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
    """Generate a rich prompt based on metadata - similar to prepare_training_data.py"""
    
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
    
    # Enhanced prompt with instructor experience
    if 'instructor_experience' in item:
        instr_exp = item['instructor_experience']
        instr_prompt = (
            f"Design this for a {instr_exp['delivery_guidance']['teaching_approach']} teaching approach "
            f"with {instr_exp['delivery_guidance']['demonstration_points']} demonstration points. "
            f"The instructor will need {instr_exp['delivery_guidance']['instructor_preparation_time']} minutes to prepare."
        )
    else:
        instr_prompt = ""
    
    # Enhanced prompt with student experience
    if 'student_experience' in item:
        student_exp = item['student_experience']
        student_prompt = (
            f"The content should follow a {student_exp['learning_journey']['cognitive_load_pattern']} cognitive load pattern "
            f"with {student_exp['learning_journey']['autonomy_level']} student autonomy and "
            f"{student_exp['engagement_factors']['interactivity_score']} interactivity."
        )
    else:
        student_prompt = ""
    
    # Add project standards from Content Creation Project Goals
    standards_prompt = """
    Follow these standards:
    - All lesson markdown should follow consistent brand guidelines
    - All lesson markdown should follow learning design patterns
    - We are a project-based learning organization with 30% theory and 70% applied hands-on practice
    - Content should be in American English
    - Include diagrams and visuals to illustrate points
    - Begin with clear learning objectives
    - Write for instructor live delivery over Zoom
    """
    
    # Combine all prompt components
    full_prompt = f"{basic_prompt} {metrics_prompt} {instr_prompt} {student_prompt} {standards_prompt}".strip()
    
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
        item_idx = int(input("\nEnter the number of the item to generate content for (or 0 for all): ")) - 1
        if item_idx == -1:
            # Generate for all items
            selected_items = items
        else:
            # Generate for a single item
            selected_items = [items[item_idx]]
    except (ValueError, IndexError):
        print("Invalid selection. Generating for the first item.")
        selected_items = [items[0]]
    
    # Generate content for selected items
    for item in selected_items:
        item_name = item.get('topic', item.get('course_title', 'unnamed'))
        print(f"\nGenerating content for: {item_name}")
        
        # Generate prompt from metadata
        prompt = generate_prompt_from_metadata(item)
        print(f"\nGenerated prompt:\n{prompt}\n")
        
        # Generate content using Claude
        print("Sending prompt to Claude 3 Sonnet...")
        content = generate_content_with_claude(prompt)
        
        # Save generated content
        filename = f"{item.get('file_type', 'content')}_{item_name.replace(' ', '_')}.md"
        save_generated_content(content, filename)
    
    print("\nContent generation complete!")

if __name__ == "__main__":
    main()
