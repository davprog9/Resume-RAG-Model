'''
builds prompt
inserts retrieved chunks
calls Gemini
returns answer


prompt = f"""
Answer using context only.

Context:
{context}

Question:
{query}
"""
'''

from retrieval import retrieve
from gemini_client import generate_text

# Opening and reading the prompt .txt file
with open("app/prompt_template.txt", "r") as file:
    TEMPLATE = file.read()

def generate_answer(user_query: str):
    '''
    Generating a model answer
     - Retrieving the closest chunks of user_query
     - Building the context
     - Building the final prompt template
     - Generating the final answer by feeding the prompt template

    Parameters:
        user_query (str): User query (question)

    Return:
        Returns the model answer
    '''
    
    # Retrieving closest chunks and building the context for the prompt
    closest_chunks = retrieve(user_query, k=10)

    context = "\n\n".join([doc.page_content for doc in closest_chunks])
    
    # Final prompt formatted
    final_prompt = TEMPLATE.format(Question = user_query, Context = context)
    
    # Calling the Gemini API and generating the final answer
    answer = generate_text(final_prompt)
    
    return answer