from fastapi import APIRouter
from app.services.rag import query_document
from app.schemas.chat_schema import ChatRequest

router = APIRouter()

@router.post("/chat")
def chat(chat_request: ChatRequest):
    answer = query_document(chat_request.question)
    return {"response": answer}