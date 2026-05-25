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