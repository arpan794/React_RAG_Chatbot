from fastapi import FastAPI
from app.db.database import engine, Base
from app.model import user
from app.routes import auth, upload, chat
from app.middleware.cors_middleware import cors_middleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

cors_middleware(app)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

@app.get("/")
def root():
    return {"message": "Backend is running!"}



