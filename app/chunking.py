from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter


def chunking(documents) -> list:
    """
    Document chunking function

    Parameters:
        documents (list): List of Document objects
    Return:
        Returns splitted documents
    """
    
    c_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap = 50,
        separators = ["\n\n", "\n", " ", ""]  # fallback levels: paragraphs, lines, words, characters
    )

    splitted_docs = c_splitter.split_documents(documents)

    print("Documents splitting completed")
    print("Total Documents: " + str(len(documents)))
    print("Total Chunks: " + str(len(splitted_docs)))

    return splitted_docs
    