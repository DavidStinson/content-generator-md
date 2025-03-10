import json
import os
import random

def read_file(filepath):
    """Read content from a file with error handling"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return None

def generate_prompt(item):
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
    
    # Combine all prompt components
    full_prompt = f"{basic_prompt} {metrics_prompt} {instr_prompt} {student_prompt}".strip()
    
    return full_prompt

def prepare_training_data():
    """Prepare training data from metadata and content files"""
    # Load metadata
    metadata_path = 'sample_content/content_metadata'
    print(f"Attempting to load metadata from: {metadata_path}")
    try:
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
            print(f"Successfully loaded metadata with {len(metadata)} categories")
            for category, items in metadata.items():
                print(f"  Category: {category} has {len(items)} items")
    except Exception as e:
        print(f"Error loading metadata: {e}")
        return []

    training_data = []

    # Map category names to directory names
    category_dir_map = {
        "GA_Lab_Examples": "GA Lab Examples",
        "GA_Lesson_Examples": "GA Lesson Examples",
        "GA_Capstone_Examples": "GA Capstone Examples",
        "GA_Course_Landing_Page_Examples": "GA Course Landing Page Examples"
    }
    
    for category, items in metadata.items():
        # Get the corresponding directory name
        dir_name = category_dir_map.get(category, category)
        
        for item in items:
            # Construct the correct file path
            file_path = os.path.join('sample_content', dir_name, item['file_name'])
            print(f"Looking for file: {file_path}")
            
            content = read_file(file_path)
            if content:
                # Generate a rich prompt
                prompt = generate_prompt(item)
                print(f"Generated prompt: {prompt[:100]}...")
                
                # Create input-output pair
                training_example = {
                    'input': prompt,
                    'output': content
                }

                training_data.append(training_example)
                print(f"Added training example for: {item['file_name']}")
            else:
                print(f"Warning: Could not read content from {file_path}")

    print(f"Total training examples created: {len(training_data)}")
    return training_data

def create_variation_prompts(training_data, num_variations=2):
    """Create variations of prompts for more diverse training data"""
    variations = []
    
    prompt_templates = [
        "Create a {file_type} about {topic} that covers these objectives: {objectives}. {metrics} {instructor} {student}",
        "I need a {file_type} on {topic}. Make sure it addresses: {objectives}. {metrics} {instructor} {student}",
        "Write a comprehensive {file_type} covering {topic}. Include these learning goals: {objectives}. {metrics} {instructor} {student}"
    ]
    
    for example in training_data:
        original_input = example['input']
        
        # Extract components from original input
        components = {
            'file_type': '',
            'topic': '',
            'objectives': '',
            'metrics': '',
            'instructor': '',
            'student': ''
        }
        
        # Very basic extraction - in a real implementation, this would be more sophisticated
        if 'Generate a ' in original_input and ' on ' in original_input:
            file_type_part = original_input.split('Generate a ')[1].split(' on ')[0]
            components['file_type'] = file_type_part
            
            topic_part = original_input.split(' on ')[1].split('. Learning objectives:')[0]
            components['topic'] = topic_part
            
            if 'Learning objectives:' in original_input:
                objectives_part = original_input.split('Learning objectives: ')[1].split('. The content')[0]
                components['objectives'] = objectives_part
            
            if 'The content should be' in original_input:
                metrics_part = original_input.split('The content should be')[1].split('Design this for')[0]
                components['metrics'] = 'The content should be' + metrics_part
            
            if 'Design this for' in original_input:
                instructor_part = original_input.split('Design this for')[1].split('The content should follow')[0]
                components['instructor'] = 'Design this for' + instructor_part
            
            if 'The content should follow' in original_input:
                student_part = original_input.split('The content should follow')[1]
                components['student'] = 'The content should follow' + student_part
        
        # Create variations using templates
        for i in range(min(num_variations, len(prompt_templates))):
            template = prompt_templates[i]
            new_prompt = template.format(
                file_type=components['file_type'],
                topic=components['topic'],
                objectives=components['objectives'],
                metrics=components['metrics'],
                instructor=components['instructor'],
                student=components['student']
            )
            
            variations.append({
                'input': new_prompt,
                'output': example['output']
            })
    
    return variations

if __name__ == "__main__":
    # Create base training data
    data = prepare_training_data()
    print(f"Prepared {len(data)} base training examples")
    
    # Create variations for more diverse training
    variations = create_variation_prompts(data)
    print(f"Created {len(variations)} additional variations")
    
    # Combine original examples and variations
    all_data = data + variations
    
    # Save the training data to a file
    os.makedirs('data', exist_ok=True)
    with open('data/training_data.json', 'w') as f:
        json.dump(all_data, f, indent=2)

    print(f"Total of {len(all_data)} training examples saved to data/training_data.json")
