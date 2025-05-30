from fastapi import Request
from jose import JWTError, jwt
from app.models.models import UserModel
from app.config.settings import settings  # Asegúrate que contiene SECRET_KEY y ALGORITHM
from app.config.database import async_session
from sqlalchemy.future import select

async def get_current_user(request: Request) -> UserModel:
    auth = request.headers.get("authorization")
    if not auth or not auth.startswith("Bearer "):
        raise Exception("No autorizado")

    token = auth.split(" ")[1]

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise Exception("Token inválido")
    except JWTError:
        raise Exception("Token inválido")

    async with async_session() as session:
        result = await session.execute(select(UserModel).where(UserModel.id == int(user_id)))
        user = result.scalars().first()
        if user is None:
            raise Exception("Usuario no encontrado")
        return user
