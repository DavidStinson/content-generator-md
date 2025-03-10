# Content Generation Automation Project - Training Data

## Project Overview

This project is part of a larger initiative to automate content generation for coding bootcamps. The goal is to leverage existing content to guide an LLM (Large Language Model) in generating new lesson and lab content that adheres to established standards and patterns.

The project consists of:
1. A structured metadata file (`sample_content/content_metadata`) that describes existing content
2. A script (`prepare_training_data.py`) that processes this metadata and generates training data for an LLM
3. The resulting training data (`data/training_data.json`) that can be used to fine-tune an LLM

## Metadata Structure

The metadata file contains detailed information about different types of educational content (labs, lessons, capstones, and course landing pages). Each content item includes:

### Basic Information
- `file_name`: Path to the content file
- `file_type`: Type of content (lab, lesson, capstone, course_landing)
- `topic`: Main subject of the content
- `learning_objectives`: Array of learning goals
- `duration`: Time required to complete
- `technologies`: Array of technologies/languages used
- `prerequisites`: Required prior knowledge
- `difficulty_level`: Beginner, intermediate, or advanced

### Content Metrics
- `word_count`: Total number of words
- `code_line_count`: Number of lines of code
- `total_line_count`: Total number of lines
- `number_of_images`: Count of images
- `number_of_diagrams`: Count of diagrams
- `text_to_code_ratio`: Proportion of text to code
- `content_density`: Words per minute and estimated reading time
- `code_blocks`: Count and average size of code examples

### Instructor Experience
- `delivery_guidance`:
  - `instructor_preparation_time`: Minutes needed to prepare
  - `demonstration_points`: Number of demonstration points
  - `common_questions_anticipated`: Expected student questions
  - `teaching_approach`: Pedagogical method (deductive, inductive, etc.)
  - `pacing_suggestions`: Time allocation for different sections

- `instructional_design`:
  - `scaffolding_level`: Amount of support provided
  - `knowledge_check_frequency`: How often comprehension is verified
  - `alternative_explanations`: Whether multiple explanations are provided
  - `instructor_notes_detail`: Level of detail in instructor notes

### Student Experience
- `learning_journey`:
  - `cognitive_load_pattern`: How complexity varies throughout
  - `autonomy_level`: Degree of independent work expected
  - `feedback_opportunities`: Points for understanding verification
  - `failure_recovery_guidance`: Support for common mistakes

- `engagement_factors`:
  - `interactivity_score`: Level of active participation
  - `real_world_relevance`: Connection to practical applications
  - `challenge_progression`: How difficulty increases
  - `achievement_milestones`: Points of accomplishment

## Training Data Generation

The `prepare_training_data.py` script processes the metadata and generates training data for an LLM. Here's how it works:

1. **Loading Metadata**: The script loads the metadata from `sample_content/content_metadata`.

2. **Processing Content**: For each content item in the metadata:
   - It locates the actual content file
   - It generates a rich prompt based on the metadata
   - It pairs the prompt with the content to create a training example

3. **Creating Variations**: The script creates variations of each prompt to provide more diverse training data.

4. **Saving Training Data**: All training examples are saved to `data/training_data.json`.

### Running the Script

To generate the training data, run:

```bash
python3 prepare_training_data.py
```

The script will output progress information as it runs and will tell you how many training examples were created.

## Using the Training Data

The generated training data can be used to fine-tune an LLM to create new educational content that follows your established patterns and standards. The training data consists of input-output pairs where:

- **Input**: A prompt that specifies the type of content to generate, along with detailed parameters about its structure, metrics, and experience factors.
- **Output**: The actual content that matches those specifications.

By training an LLM on these examples, it learns to generate new content that adheres to your specific standards when given similar prompts.

### Potential Improvements

1. **More Examples**: Add more content examples to provide a broader range of patterns.
2. **Additional Metadata**: Expand the metadata to capture more aspects of your content.
3. **Prompt Engineering**: Refine the prompt generation to better guide the LLM.
4. **Content Analysis**: Add more sophisticated analysis of content to extract more accurate metrics.

## Integration with CrewAI

As mentioned in the project goals, this training data preparation is a step toward building a workflow using CrewAI Agents. The enhanced metadata and training data will provide valuable context for these agents to understand your content creation standards and generate new content accordingly.
