from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware



origins = [
    "http://localhost:5173",  # React app
    "http://127.0.0.1:5173"
]

def cors_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,   # or ["*"] for testing
        allow_credentials=True,
        allow_methods=["*"],     # IMPORTANT
        allow_headers=["*"],     # IMPORTANT
)
