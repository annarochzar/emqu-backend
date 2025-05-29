from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Carga variables del archivo .env
load_dotenv()

# Obtiene la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# Crea el motor de conexión a la base de datos
engine = create_async_engine(DATABASE_URL, echo=True)

# Crea una sesión asincrónica
AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base para los modelos ORM
Base = declarative_base()

# Función para obtener la sesión en otras partes del código
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
