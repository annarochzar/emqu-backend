from fastapi import FastAPI
from ariadne import gql, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL

from app.api.resolvers import query, mutation

# Carga esquema desde un archivo .graphql o directo en string
type_defs = gql("""
    type Query {
        hello: String!
    }
    type Mutation {
        dummy: String
    }
""")

schema = make_executable_schema(type_defs, query, mutation)

app = FastAPI()

# Monta la ruta /graphql con GraphQL Playground habilitado
app.add_route("/graphql", GraphQL(schema, debug=True))
