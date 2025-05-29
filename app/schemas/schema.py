from ariadne import QueryType, make_executable_schema, gql

type_defs = gql("""
    type Query {
        hello: String!
    }
""")

query = QueryType()

@query.field("hello")
def resolve_hello(_, info):
    return "¡Hola desde EmQu GraphQL!"

schema = make_executable_schema(type_defs, query)
