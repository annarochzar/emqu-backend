import strawberry
from app.graphql.users.mutations import UserMutation

@strawberry.type
class Query:
    # Puedes poner un ejemplo o dejarlo vacío
    hello: str = "Hola mundo"

@strawberry.type
class Mutation(UserMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
