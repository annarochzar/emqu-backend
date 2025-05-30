from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    # Esto es solo un ejemplo temporal
    if token != "fake-token":
        raise HTTPException(status_code=401, detail="Token inválido")
    return {"id": 1, "name": "Test User", "role": "author"}
