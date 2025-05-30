# app/resolvers/user_mutations.py
import graphene
from app.models.models import UserModel
from app.schemas.user import UserCreate
from app.utils.security import hash_password
from app.config.database import async_session  # suponiendo async SQLAlchemy

class RegisterUser(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
    
    ok = graphene.Boolean()
    user_id = graphene.Int()
    message = graphene.String()

    async def mutate(root, info, name, email, password):
        # Primero, crear el objeto para validar (opcional)
        data = UserCreate(name=name, email=email, password=password)

        async with async_session() as session:
            # Verificar si ya existe usuario con ese email
            existing_user = await session.execute(
                # consulta async SQLAlchemy para buscar usuario por email
                UserModel.__table__.select().where(UserModel.email == data.email)
            )
            existing_user = existing_user.scalar_one_or_none()

            if existing_user:
                return RegisterUser(ok=False, message="El correo ya está registrado", user_id=None)
            
            # Crear usuario nuevo
            hashed_pw = hash_password(data.password)
            new_user = UserModel(name=data.name, email=data.email, password=hashed_pw)

            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)

            return RegisterUser(ok=True, message="Usuario registrado con éxito", user_id=new_user.id)
