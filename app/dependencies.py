from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth

security = HTTPBearer()

async def has_access(credentials: HTTPAuthorizationCredentials= Depends(security)):
    """
        Function that is used to validate the bearer token with Firebase
    """
    token = credentials.credentials

    try:
        user = auth.verify_id_token(token)
        return user
    except Exception as e:  # catches any exception
        print(e)
        raise HTTPException(
            status_code=401,
            detail='Invalid Auth token')
