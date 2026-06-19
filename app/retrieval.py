from vector_store import vector_db_store

def retrieve(user_query: str, k: int = 3):
    '''
    User Query
        ↓
    Create query embedding
        ↓
    Search vector DB
        ↓
    Return top k chunks
    '''
    vc_store = vector_db_store()
    closest_answer = vc_store.similarity_search(user_query, k)

    return closest_answer