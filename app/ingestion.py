# Loading documents
import os
from langchain_community.document_loaders import PyPDFLoader

data_folder = "../data"
doc_list = []

for file in os.listdir(data_folder): # os.listdir() list of all the files from the foler
    if file.endswith(".pdf"):
        loader = PyPDFLoader(os.path.join(data_folder, file)) # os.path.join() builds a file path
        docs = loader.load()
        doc_list.extend(docs) # .extend is different from .append(docs) which would add the entire list as a single item



# NOTE: All the files from the data are being inserted into 'doc_list' variable 