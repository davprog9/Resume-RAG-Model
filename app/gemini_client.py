from google import genai
from config import GEMINI_API_KEY

# Initializing the client
client = genai.Client(api_key=GEMINI_API_KEY)

def generate_text(prompt):

    '''
    Model text generation generator

    Parameters:
        content: The final formatted prompt template including the question and the context
    
    Return:
        Yields chunks of the response text from the model
    '''

    try:
        response = client.models.generate_content_stream( # Use generate_content for non-streaming style response
            model = "gemini-2.5-flash",
            contents = prompt 
        )

        # Iterating over chunks for streaming-style response 
        for chunk in response:
            if chunk.text:
                yield chunk.text # yields every chunk

    # Raise exception if there is a model API issue
    except Exception as e:
        print(f"Gemini API Error: {e}")
