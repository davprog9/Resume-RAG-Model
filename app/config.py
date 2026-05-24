from dotenv import load_dotenv # Reads .env file
import os

# searches for .env
# reads it
# loads variables into the environment
load_dotenv() 


# Retrieves GEMINI_API_KEY from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Missing GEMINI_API_KEY in environment")