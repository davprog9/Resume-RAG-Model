from google import genai
#from google import errors
#from gemini_client import client
from config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)

def generate_text(content):
    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = content 
        )

        print(response.text)

    except ImportError as e:
        print(f"Gemini API Error: {e}")
