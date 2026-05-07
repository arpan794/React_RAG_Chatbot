from sqlalchemy import Column, Integer, String
from app.db.database import Base

class chat_history(Base):
    __tablename__ = "chats"

    id = Column(Integer,primary_key=True, index=True)
    user_id = Column(Integer)
    question = Column(String)
    answer = Column(String)


