from ariadne import QueryType, MutationType

query = QueryType()
mutation = MutationType()

@query.field("hello")
def resolve_hello(_, info):
    return "Hola desde EmQu Backend!"

@mutation.field("dummy")
def resolve_dummy(_, info):
    return "Esto es un dummy mutation"
