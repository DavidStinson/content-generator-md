# Using Anthropic Claude 3 API for Content Generation

This guide explains how to use the Anthropic Claude 3 API for generating educational content in this project.

## Setup

1. **Install Required Packages**

   The required packages are already listed in `requirements.txt`. You can install them with:

   ```bash
   pip install -r requirements.txt
   ```

2. **Get an API Key**

   - Sign up for an account at [Anthropic Console](https://console.anthropic.com/)
   - Create an API key from your dashboard
   - Copy the API key

3. **Set Your API Key**

   There are two ways to set your API key:

   - **Option 1**: Edit the `.env` file and replace `your_api_key_here` with your actual API key:
     ```
     ANTHROPIC_API_KEY=your_actual_api_key
     ```

   - **Option 2**: Set it as an environment variable in your terminal:
     ```bash
     # For macOS/Linux
     export ANTHROPIC_API_KEY=your_actual_api_key
     
     # For Windows Command Prompt
     set ANTHROPIC_API_KEY=your_actual_api_key
     
     # For Windows PowerShell
     $env:ANTHROPIC_API_KEY="your_actual_api_key"
     ```

## Using the Example Script

The `claude_example.py` script demonstrates how to use the Claude 3 Sonnet model to generate content:

```bash
python claude_example.py
```

This will:
1. Load your API key from the environment or `.env` file
2. Send a sample prompt to Claude 3 Sonnet
3. Print the generated content

## Integrating with Your Project

To integrate Claude 3 with your content generation workflow:

1. **Import the necessary modules**:
   ```python
   from anthropic import Anthropic
   ```

2. **Initialize the client**:
   ```python
   client = Anthropic(api_key=your_api_key)
   ```

3. **Generate content**:
   ```python
   message = client.messages.create(
       model="claude-3-sonnet-20240229",
       max_tokens=1000,
       messages=[
           {"role": "user", "content": your_prompt}
       ]
   )
   
   # Access the generated content
   generated_text = message.content[0].text
   ```

## API Usage Notes

- The Claude 3 Sonnet model is powerful for generating educational content but has costs associated with API usage
- Monitor your usage in the Anthropic Console
- The model name format is `claude-3-sonnet-20240229` (not imported as a constant)
- Responses are returned as a message object with a `content` attribute containing the generated text

## Troubleshooting

- **ImportError**: Make sure you've installed the latest version of the Anthropic package
- **Authentication Error**: Check that your API key is correct and properly set
- **Rate Limiting**: If you hit rate limits, implement exponential backoff in your requests

## Additional Resources

- [Anthropic API Documentation](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- [Claude 3 Model Details](https://docs.anthropic.com/claude/docs/models-overview)
- [Python SDK Documentation](https://github.com/anthropics/anthropic-sdk-python)
