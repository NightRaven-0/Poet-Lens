import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API (retrieve API key from environment variable)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Select the Gemini model for text generation
model = genai.GenerativeModel('gemini-pro')

def generate_poem(image_caption, mood):
    """
    Generates a poem based on the image caption and mood using the Gemini API.

    Args:
        image_caption: A string describing the content of the image.
        mood: A string representing the desired mood of the poem.

    Returns:
        A string containing the generated poem, or None if an error occurs.
    """
    prompt = f"Please write a short poem about the following image, with a '{mood}' mood:\n\n{image_caption}\n\nPoem:"

    try:
        response = model.generate_content(prompt)
        # Gemini returns a response object, the poem is in response.text
        return response.text
    except Exception as e:
        print(f"Error generating poem: {e}")
        return None

if __name__ == '__main__':
    # Example usage (for testing)
    caption = "A lone tree stands on a hill under a starry night."
    mood = "serene"
    poem = generate_poem(caption, mood)
    if poem:
        print("Generated Poem:\n", poem)