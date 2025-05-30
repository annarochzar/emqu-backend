from fastapi import Depends
from strawberry.types import Info
from jose import JWTError, jwt
from app.config.database import async_session
from app.models.models import UserModel
from sqlalchemy.future import select
from app.config.settings import settings


async def get_current_user(info: Info) -> UserModel:
    authorization: str = info.context["request"].headers.get("Authorization")
    if not authorization:
        raise Exception("No se proporcionó token de autenticación.")

    token = authorization.replace("Bearer ", "")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise Exception("Token inválido.")
    except JWTError:
        raise Exception("Token inválido.")

    async with async_session() as session:
        result = await session.execute(select(UserModel).where(UserModel.id == int(user_id)))
        user = result.scalars().first()
        if not user:
            raise Exception("Usuario no encontrado.")
        return user
