from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

vector_store = None

def process_document(file_path):
    global vector_store

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(docs, embeddings)

    return "Document processed successfully"



def query_document(question):
    global vector_store

    if vector_store is None:
        return "No document uploaded"
    
    # docs = vector_store.similarity_search(question, k=3)
    
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(question)

    response = "\n".join([doc.page_content for doc in docs])

    return response
   