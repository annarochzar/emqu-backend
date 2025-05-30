# app/config/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el motor de la base de datos (asíncrono)
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear el sessionmaker
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Declarative base para los modelos
Base = declarative_base()

# Función para obtener la sesión de base de datos
async def get_db():
    async with async_session() as session:
        yield session
