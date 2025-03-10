# Improved Prompt Structure for Content Generation

This document summarizes the improvements made to the prompt structure for generating content that more closely matches the GA lesson and lab examples.

## Key Improvements

1. **Added Explicit Format Instructions**
   - Included specific HTML/markdown structure for headers
   - Added template for metadata sections (author, duration, etc.)
   - Specified GA branding elements

2. **Incorporated Few-Shot Examples**
   - Added complete examples of lesson and lab formats
   - Showed the specific structure of learning objectives, content sections, and code examples

3. **Enhanced Content Standards**
   - Emphasized the 30% theory/70% hands-on practice ratio
   - Specified requirements for diagrams and visuals
   - Highlighted the instructor-led, live delivery context

4. **Included Specific Styling Guidelines**
   - Added instructions for callouts, notes, and tips formatting
   - Specified code block formatting requirements
   - Detailed how to format exercises and activities

## Results

The improved prompt structure has resulted in generated content that much more closely matches the example lessons and labs:

1. **Lesson Format Improvements**
   - Proper HTML header structure with headline and subhead spans
   - GA logo at the top
   - Metadata table with Title, Type, Duration, and Author
   - Correctly formatted learning objectives
   - Proper heading hierarchy
   - Notes formatted with the 📚 icon
   - Code blocks with syntax highlighting
   - Images with captions

2. **Lab Format Improvements**
   - GA logo at the top
   - Metadata table with Title, Type, Duration, and Author
   - Multi-day lab with clear day-by-day breakdowns
   - Detailed learning objectives
   - Step-by-step instructions for each task
   - Submission instructions at the end

## Implementation

We've created two new scripts that implement the improved prompt structure:

1. **improved_claude_generator.py**
   - A comprehensive script that integrates with your metadata
   - Allows you to select a category and item to generate content for
   - Generates a prompt based on the metadata with improved formatting instructions
   - Sends the prompt to Claude and saves the generated content

2. **test_improved_prompt.py**
   - A simplified script for testing the improved prompt structure
   - Generates a prompt for a specified topic and file type
   - Sends the prompt to Claude and saves the generated content

## How to Use

### Using the Improved Claude Generator

1. Run the script:
   ```
   python3 improved_claude_generator.py
   ```

2. Follow the prompts to select a category and item to generate content for.

3. Review the generated prompt and confirm that you want to proceed.

4. The script will send the prompt to Claude and save the generated content to the `generated_content` directory.

### Using the Test Improved Prompt Script

1. Edit the script to specify the topic and file type:
   ```python
   # Test parameters
   topic = "Your Topic"
   file_type = "lesson"  # or "lab"
   ```

2. Run the script:
   ```
   python3 test_improved_prompt.py
   ```

3. The script will generate a prompt, send it to Claude, and save the generated content to the `generated_content` directory.

## Prompt Structure

The improved prompt structure consists of the following components:

```
{basic_prompt}

{metrics_prompt}

{format_instructions}

{standards_prompt}

{example_prompt}

Please generate complete, well-structured content that follows all the guidelines above.
```

Where:
- `basic_prompt` includes the topic and learning objectives
- `metrics_prompt` specifies content metrics like word count and text-to-code ratio
- `format_instructions` provides specific formatting guidelines based on the file type
- `standards_prompt` outlines the content standards
- `example_prompt` includes an example of the desired format

## Next Steps

1. **Fine-tune the Prompt Structure**: Continue to refine the prompt structure based on the results.
2. **Expand the Example Library**: Add more examples of different content types.
3. **Integrate with CrewAI**: As mentioned in your project goals, integrate this with CrewAI Agents.
4. **Implement Quality Control**: Add a review process for generated content.

## Example Generated Content

You can find examples of content generated using the improved prompt structure in the `generated_content` directory:

- `test_improved_lesson_Python_Unit_Testing.md`: A lesson on Python Unit Testing
- `test_improved_lab_Django_REST_Framework.md`: A lab on Django REST Framework

These examples demonstrate how the improved prompt structure generates content that closely matches your example lessons and labs.


##To Run Prompts moving forward

Option 1: Using the test_improved_prompt.py script (Quickest method)
Edit the test_improved_prompt.py file:

Change the topic variable to your desired lesson topic
Make sure file_type is set to "lesson" (or "lab" if you want to create a lab)
You can also customize the learning objectives if needed
Run the script:

python3 test_improved_prompt.py
Review the generated content:

The script will save the generated lesson to the generated_content directory
Check the content to ensure it meets your standards
Make any manual edits or refinements as needed
Option 2: Using the improved_claude_generator.py script (More comprehensive)
Add metadata for your new lesson:

Edit the sample_content/content_metadata file to include information about your new lesson
Include details like topic, learning objectives, content metrics, etc.
Run the improved generator script:

python3 improved_claude_generator.py
Follow the interactive prompts:

Select the category your lesson belongs to
Select your new lesson from the list
Review the generated prompt and confirm
The script will generate the content and save it to the generated_content directory
Option 3: Creating a custom script for batch generation
If you want to generate multiple lessons at once, you could:

Create a list of lesson topics and their details
Modify the improved_claude_generator.py script to loop through this list
Generate all lessons in a batch process