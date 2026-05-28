# Loading documents
import os
from langchain_community.document_loaders import PyPDFLoader

from chunking import chunking
from vector_store import vector_db_store
from uuid import uuid4

doc_list = []

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

pdf_path = BASE_DIR / "data"


def loading_docs():
    for file in os.listdir(pdf_path): # os.listdir() list of all the files from the foler
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_path, file)) # os.path.join() builds a file path
            docs = loader.load()
            doc_list.extend(docs) # .extend is different from .append(docs) which would add the entire list as a single item

# NOTE: All the files from the data are being inserted into 'doc_list' variable 


'''
Load docs
↓
Clean docs
↓
Chunk docs
↓
Create embeddings
↓
Store embeddings
'''
def ingest():

    # Loading documents
    loading_docs()
    
    # Chunking
    splitted_docs = chunking(doc_list)

    # Storing into vector database
    uuids = [str(uuid4()) for _ in range(len(splitted_docs))]

    vc_store = vector_db_store()
    vc_store.add_documents(documents=splitted_docs, ids=uuids)



print("Document ingestion started ")
ingest()
print("Document ingestion completed ")