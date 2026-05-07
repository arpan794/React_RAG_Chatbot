from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

FAISS_DIR = "faiss_indices"
os.makedirs(FAISS_DIR, exist_ok=True)

def process_document(file_path, user_id):

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(docs, embeddings)
    
    save_path = os.path.join(FAISS_DIR, f"{user_id}_faiss_index")
    vector_store.save_local(save_path)

    return "Document processed successfully"



