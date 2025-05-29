from fastapi import FastAPI
from ariadne.asgi import GraphQL
from app.schema import schema

app = FastAPI(
    title="EmQu Knowledge API",
    description="Gestor de conocimientos técnicos para EmQu",
    version="1.0.0"
)

graphql_app = GraphQL(schema, debug=True)

app.mount("/graphql", graphql_app)
