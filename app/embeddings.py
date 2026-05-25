from langchain_huggingface import HuggingFaceEmbeddings

# Loading the Qwen embedding model using HuggingFaceEmbeddings, can be done with SentenceTrasnformer as well
embedding_function = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")