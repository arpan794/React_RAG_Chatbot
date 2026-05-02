import os
import uuid
from fastapi import APIRouter, UploadFile, File
import shutil
from app.services.rag import process_document

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    
    os.makedirs("uploads, exist_ok=True")

    file_path = f"uploads/{uuid.uuid4()}_{file.filename}" # to prevent file overwrite risk

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_document(file_path)

    return {"message": result}