from embeddings import embedding_function
from langchain_chroma import Chroma
from sentence_transformers import SentenceTransformer

# Vector database
def vector_db_store() -> Chroma:

    vector_store = Chroma(
        collection_name="resume_info",
        embedding_function=embedding_function,
        persist_directory="./resume_info_chromadb",  # Where to save data locally, remove if not necessary
    )

    return vector_store