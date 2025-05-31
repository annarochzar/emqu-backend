# 📚 EmQu – Sistema de Gestión de Conocimientos Técnicos

Este proyecto es el resultado de una prueba técnica para la posición de **Backend Developer**. El objetivo fue desarrollar un sistema de gestión de conocimientos técnicos utilizando **FastAPI** con **GraphQL**, una base de datos relacional (**PostgreSQL**), y autenticación basada en **JWT**, diferenciando dos roles principales: `author` y `moderator`.

---

## ✅ Funcionalidades Implementadas

### 1. Gestión de Usuarios

- Registro de nuevos usuarios con nombre, correo electrónico y contraseña.
- Inicio de sesión mediante autenticación segura con JWT.
- Gestión de roles: `author` (autor) y `moderator` (moderador).
- Los autores pueden:
  - Crear, editar y eliminar sus propios artículos.
- Los moderadores pueden:
  - Consultar estadísticas globales del sistema.

### 2. Gestión de Artículos Técnicos

- CRUD completo para artículos técnicos.
- Cada artículo contiene:
  - Título
  - Contenido
  - Fecha de creación
  - Relación con temas (topics)
  - Relación con etiquetas (tags)
  - Autor del artículo
- Búsqueda y filtrado de artículos por:
  - Tema
  - Etiqueta
  - Palabra clave
  - Autor
- Consulta de los últimos N artículos publicados.

### 3. Métricas y Estadísticas (Accesibles solo por Moderadores)

Se desarrollaron consultas estadísticas exclusivas para moderadores, entre ellas:

- ✅ Total de artículos creados por tema.
- ✅ Total de artículos creados por usuario.
- ✅ Top 5 temas más utilizados.

**No implementado (por falta de tiempo):**

- ❌ Número de artículos por mes en los últimos 6 meses.
- ❌ Tiempo promedio entre publicaciones por usuario.
- ❌ Porcentaje de artículos por tema.

---

## 🧰 Tecnologías Utilizadas

| Herramienta       | Uso                                      |
|-------------------|-------------------------------------------|
| **FastAPI**       | Framework principal para la API backend  |
| **Strawberry GraphQL** | Definición de esquema y resolvers GraphQL |
| **PostgreSQL**    | Base de datos relacional principal       |
| **SQLAlchemy**    | ORM para modelado de entidades           |
| **Pydantic**      | Validación y serialización de datos      |
| **JWT**           | Autenticación basada en tokens           |
| **Alembic**       | Migraciones de base de datos             |
| **Uvicorn**       | Servidor ASGI para desarrollo            |
| **dotenv**        | Manejo de variables de entorno           |
---

## 📁 Estructura del Proyecto

app/
├── api/ # Endpoints REST (no utilizados)
├── auth/ # Autenticación y generación de tokens
├── config/ # Configuración (DB, variables, etc.)
├── core/ # Enumeraciones y lógica central
├── database/ # Inicialización y migraciones DB
├── dependencies/ # Inyecciones de dependencias
├── graphql/ # Esquemas y resolvers de GraphQL
│ ├── articles/
│ ├── tags/
│ ├── topics/
│ ├── users/
│ └── statistics/
├── main.py # Archivo principal de la app
├── models/ # Modelos ORM (User, Article, etc.)
├── resolvers/ # Lógica de negocio para resolvers
├── schema/ # Esquemas GraphQL combinados
├── schemas/ # Esquemas Pydantic
└── utils/ # Funciones utilitarias

---

## ⚙️ Configuración del Entorno

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/annarochzar/emqu-backend.git
   cd emqu-backend
2. Crear y activar entorno virtual:

   ```bash
    python -m venv venv
    source venv/bin/activate

3. Instalar dependencias:

   ```bash
    pip install -r requirements.txt

4. Configurar variables de entorno (.env):

    ```bash
    DATABASE_URL=postgresql+asyncpg://postgres:1234@localhost:5432/emqu_db
    SECRET_KEY=prueba_tec_backend
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Ejecutar migraciones:

    ```bash
    alembic upgrade head

6. Iniciar el servidor:

    ```bash
    uvicorn app.main:schema --reload

🧪 Pruebas
Las pruebas manuales se realizaron usando herramientas como Insomnia y GraphQL Playground.

Se validó el flujo completo de:

  1. Registro, login y autenticación.
  
  2. Creación y gestión de artículos.
  
  3. Ejecución de métricas con usuarios moderadores.

📌 Conclusiones
A pesar del tiempo limitado, se logró implementar una base sólida del sistema propuesto, priorizando las funcionalidades críticas como autenticación, gestión de artículos, y el acceso controlado a estadísticas por rol. Algunas métricas avanzadas quedaron pendientes por razones de tiempo y pueden ser abordadas como mejoras futuras.

👩‍💻 Autora
Desarrollado por Anna Paola Rocha Salazar como parte del proceso de evaluación técnica para la empresa EmQu.
