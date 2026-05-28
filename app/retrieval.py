from vector_store import vector_db_store

def retrieve(user_query: str, k: int):
    '''
    User Query
        ↓
    Create query embedding
        ↓
    Search vector DB
        ↓
    Return top chunks
    '''

    closest_answer = vector_db_store().similarity_search(user_query, k=1)

    return closest_answer
