# Claude API Testing Summary

This document summarizes the tests we've conducted with the Anthropic Claude API and provides guidance on how to use it for content generation in your project.

## Tests Conducted

We've successfully tested the Anthropic Claude 3 Sonnet API with the following scripts:

1. **Basic API Test** (`test_claude_api.py`):
   - Verified API connectivity
   - Sent a simple message to Claude
   - Received and displayed the response

2. **Content Generation Test** (`test_content_generation.py`):
   - Generated a lesson introduction on Python unit testing
   - Applied project standards (30% theory/70% practice, American English, etc.)
   - Saved the generated content to a file

3. **Metadata-Based Content Generation** (`claude_metadata_example.py`):
   - Loaded metadata from your project
   - Generated a prompt based on the metadata
   - Created content following the specified requirements
   - Saved the generated content to a file

## How to Use the Claude API for Content Generation

### Basic Usage

```python
from anthropic import Anthropic
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize the client
client = Anthropic(api_key=api_key)

# Send a message to Claude
message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ]
)

# Access the response
response_text = message.content[0].text
```

### Integrating with Your Project

For your content generation project, we've created two main scripts:

1. **claude_example.py**: A simple example showing how to use the Claude API
2. **claude_content_generator.py**: A more comprehensive script that integrates with your metadata

To generate content based on your metadata:

1. Ensure your API key is set in the `.env` file
2. Run `python3 claude_content_generator.py`
3. Follow the prompts to select a category and item
4. The script will generate content based on the selected metadata and save it to the `generated_content` directory

### Prompt Engineering

Based on our tests, effective prompts for your content generation should include:

1. **Basic Information**:
   - Content type (lab, lesson, etc.)
   - Topic
   - Learning objectives

2. **Content Metrics**:
   - Word count
   - Text-to-code ratio
   - Number of images/diagrams

3. **Project Standards**:
   - 30% theory, 70% applied hands-on practice
   - American English
   - Clear learning objectives
   - Instructor live delivery format

### API Notes

- The current model (`claude-3-sonnet-20240229`) is deprecated and will reach end-of-life on July 21st, 2025
- Consider updating to the latest model when available
- Monitor your API usage as there are costs associated with API calls
- The API key is stored in the `.env` file and should not be committed to version control

## Generated Content Examples

We've generated the following example content:

1. **sample_lesson_intro.md**: A lesson introduction on Python unit testing
2. **metadata_example_Django_CRUD_with_Django_Rest_Framework.md**: A lab on Django CRUD with Django Rest Framework

These examples demonstrate how Claude can generate content that follows your project's standards and requirements.

## Next Steps

1. **Refine Prompts**: Experiment with different prompt structures to improve content quality
2. **Batch Processing**: Consider implementing batch processing for generating multiple content items
3. **Quality Control**: Implement a review process for generated content
4. **Integration with CrewAI**: As mentioned in your project goals, integrate this with CrewAI Agents

## Resources

- [Anthropic API Documentation](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [Claude 3 Model Details](https://docs.anthropic.com/claude/docs/models-overview)
- [Python SDK Documentation](https://github.com/anthropics/anthropic-sdk-python)
