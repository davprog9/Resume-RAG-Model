from google import genai, errors
from gemini_client import client
from config import GEMINI_API_KEY


client = genai.Client(api_key=GEMINI_API_KEY)

def generate_text():
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Explain what RAG is in simple terms."
        )

        print(response.text)

    except errors.APIError as e:
        print(f"Gemini API Error: {e}")
