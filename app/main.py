from gemini_client import client
from google.genai import errors # For raising API error in case if happens


try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain what RAG is in simple terms."
    )

    print(response.text)

except errors.APIError as e:
    print(f"Gemini API Error: {e}")