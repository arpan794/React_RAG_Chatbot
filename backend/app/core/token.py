from jose import JWTError, jwt
from datetime import datetime, timedelta

secret_key = "your_secret_key"
algorithm = "HS256"
access_token_expire_minutes = 30

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=access_token_expire_minutes)
    payload.update({"exp": expire})

    encoded_jwt = jwt.encode(payload, secret_key, algorithm=algorithm)
    return encoded_jwt