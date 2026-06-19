from google import genai
from config import GEMINI_API_KEY

# Initializing the client
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_text(content):

    '''
    Model API text generation

    Parameters:
        content: The final formatted prompt template including the question and the context
    
    Return:
        Returns the response text from the model
    '''

    try:
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = content 
        )

        return response.text

    # Raise exception if there is a model API issue
    except Exception as e:
        print(f"Gemini API Error: {e}")
