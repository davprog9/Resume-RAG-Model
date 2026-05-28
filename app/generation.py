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
    
    # Retrieving closest chunks and building the context for the prompt
    closest_chunks = retrieve(user_query, k=3)
    context = "\n\n".join([doc.page_content for doc in closest_chunks])
    
    # Final prompt formatted
    final_prompt = TEMPLATE.format(Question = user_query, Context = context)
    
    # Calling the Gemini API and generating the final answer
    answer = generate_text(final_prompt)
    
    return answer