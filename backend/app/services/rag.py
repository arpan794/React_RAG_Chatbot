from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

vector_store = None

def process_document(file_path):
    global vector_store

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings()

    vector_store = FAISS.from_documents(docs, embeddings)

    return "Document processed successfully"



def query_document(question):
    global vector_store

    if vector_store is None:
        return "No document uploaded"
    
    docs = vector_store.similarity_search(question, k=3)

    response = "\n".join([doc.page_content for doc in docs])

    return response
   