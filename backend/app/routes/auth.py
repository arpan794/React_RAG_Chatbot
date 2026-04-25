from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.model.user import User
from app.core.security import hash_password, verify_password
from app.core.token import create_access_token

from app.schemas.user import UserCreate

from app.core.dependency import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
            )

    hashed_password = hash_password(user.password)

    new_user = User(
        email=user.email, 
        password=hashed_password
        )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message": "User registered successfully",
        "user": {
            "id": new_user.id,
            "email": new_user.email
        }
    }

@router.post("/login")
def login(user:UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(
            status_code=400, 
            detail="Invalid email or password"
            )
    
    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=400, 
            detail="Invalid email or password"
            )
    
    token = create_access_token(data={"sub": db_user.email})
    return {
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/profile")
def profile(current_user: str = Depends(get_current_user)):
    return {
        "message": "User profile",
        "email": current_user
    }

