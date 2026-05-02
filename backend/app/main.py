from fastapi import FastAPI
from app.db.database import engine, Base
from app.model import user
from app.routes import auth, upload
from app.middleware.cors_middleware import cors_middleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

cors_middleware(app)

app.include_router(auth.router, upload.router)

@app.get("/")
def root():
    return {"message": "Backend is running!"}



