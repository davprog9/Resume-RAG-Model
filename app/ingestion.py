# Loading documents
import os
from langchain_community.document_loaders import PyPDFLoader

from chunking import chunking
from vector_store import vector_db_store
from uuid import uuid4

from pathlib import Path



# Path to the data folder
BASE_DIR = Path(__file__).resolve().parent.parent
pdf_path = BASE_DIR / "data"

doc_list = []

def loading_docs():

    '''
    Loading the data from the data folder into doc_list variable
    
    Data is being converted into 'Documents' object prior loading 

    All the files from the data file are being inserted into 'doc_list' variable 
    '''

    for file in os.listdir(pdf_path): # os.listdir() list of all the files from the folder
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(pdf_path, file)) # os.path.join() builds a file path
            docs = loader.load()
            doc_list.extend(docs) # .extend is different from .append(docs) which would add the entire list as a single item


def ingest():

    '''
    Ingesting the data into vector database

    1. First loading documents from the file
    2. Splitting the loaded data into chunks
    3. Making uuids for every chunk and storing all the chunks into vector database
    4. Vectors database automatically handles the embedding part
    '''

    # Loading documents
    loading_docs()
    
    # Chunking
    splitted_docs = chunking(doc_list)

    # Storing into vector database
    uuids = [str(uuid4()) for _ in range(len(splitted_docs))]

    vc_store = vector_db_store()
    vc_store.add_documents(documents=splitted_docs, ids=uuids)


# NOTE: The ingestion part is being run separately,
#       So this part can also be moved into the ingest() function and be run from somewhere else
print("Document ingestion started ")
ingest()
print("Document ingestion completed ")