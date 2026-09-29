import os
from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Read Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

# Check whether API key exists
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file.")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Send prompt to Gemini
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the meaning of Palak"
)

# Display the response
print("\nGemini Response:\n")
print(response.text)