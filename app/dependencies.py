from fastapi import Depends , HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt,JWTError
from app.config import settings

oauth_schema = OAuth2PasswordBearer(tokenUrl="login")

def verify_access_token(token:str=Depends(oauth_schema)):

    try:
        
        payload = jwt.decode(token,settings.SECRET_KEY , algorithm=[settings.ALGORITHM])

        email = payload.get("sub")

        if email is None:

            raise HTTPException(status_code=404 , detail="Invalid Token")
        
        return email
    
    except JWTError:

        raise HTTPException(status_code=401 , detail="Token Verification Failed")
    