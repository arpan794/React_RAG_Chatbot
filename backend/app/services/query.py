from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from app.services.rag import FAISS_DIR
from langchain_community.memory import ConversationBufferMemory
from langchain_community.chains import RetrievalQA
from langchain_openai import ChatOpenAI
import os


def load_vector_store(user_id):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    load_path = os.path.join(FAISS_DIR, f"{user_id}_faiss_index")

    if not os.path.exists(load_path):
        return None 

    return FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)


memory_store = {}

def query_document(question, user_id):
    vector_store = load_vector_store(user_id)

    if vector_store is None:
        return "No document uploaded"

    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    llm = ChatOpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo",
        temperature=0
    )

    if user_id not in memory_store:
        memory_store[user_id] = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
            )
        
    memory = memory_store[user_id]

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        memory=memory
    )

    response = qa_chain.invoke({ "query": question })

    return response["result"]

