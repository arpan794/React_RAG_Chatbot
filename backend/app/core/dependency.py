from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from app.core.token import secret_key, algorithm

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, secret_key,
                             algorithms=[algorithm])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(
                status_code=401, 
                detail="Invalid authentication credentials"
                )
        return email
    except JWTError:
        raise HTTPException(
            status_code=401, 
            detail="Invalid authentication credentials"
            )

        