import strawberry
from app.graphql.users.types import UserType, LoginResponseType
from app.graphql.users.inputs import RegisterUserInput, LoginInput
from app.models.models import UserModel
from app.config.database import async_session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from app.auth.jwt_handler import create_access_token
from sqlalchemy.future import select


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def register_user(self, input: RegisterUserInput) -> UserType:
        async with async_session() as session:
            hashed_password = pwd_context.hash(input.password)
            new_user = UserModel(
                name=input.name,
                email=input.email,
                password=hashed_password,
                role=input.role,
            )
            session.add(new_user)
            try:
                await session.commit()
                await session.refresh(new_user)
                return UserType(
                    id=new_user.id,
                    name=new_user.name,
                    email=new_user.email,
                    role=new_user.role,
                    created_at=new_user.created_at,
                )
            except IntegrityError:
                await session.rollback()
                raise Exception("Email ya registrado.")
    
    @strawberry.mutation
    async def login_user(self, data: LoginInput) -> LoginResponseType:
        async with async_session() as session:
            # Busca usuario por email
            result = await session.execute(select(UserModel).filter_by(email=data.email))
            user = result.scalars().first()
            
            if not user:
                raise Exception("Usuario o contraseña inválidos")
            
            # Verifica contraseña
            if not pwd_context.verify(data.password, user.password):
                raise Exception("Usuario o contraseña inválidos")
            
            # Genera token JWT (por ejemplo, con user.id)
            access_token = create_access_token(data={"sub": str(user.id)})
            
            return LoginResponseType(
                access_token=access_token,
                token_type="bearer"
            )