from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.rag import query_document
from app.model.chat import chat_history
from app.schemas.chat_schema import ChatRequest
from backend.app.routes.auth import get_db

router = APIRouter()

@router.post("/chat")
def chat(chat_request: ChatRequest, db: Session = Depends(get_db)):
    answer = query_document(chat_request.question, chat_request.user_id)

    new_chat = chat_history(
        user_id=chat_request.user_id,
        question=chat_request.question,
        answer=answer
    )
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return {"response": answer}