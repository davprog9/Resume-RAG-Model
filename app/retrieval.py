from vector_store import vector_db_store

def find_closest(user_query: str, k=1) -> list[str]:
    return vector_db_store.similarity_search(user_query, k=k)


def retrieve(user_query: str):
    '''
    User Query
        ↓
    Create query embedding
        ↓
    Search vector DB
        ↓
    Return top chunks
    '''

    closest_answer = find_closest(user_query)

    return closest_answer
