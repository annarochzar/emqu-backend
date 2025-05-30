import strawberry
from app.graphql.users.mutations import UserMutation
from app.graphql.articles.mutations import CreateArticle, UpdateArticle, DeleteArticle

@strawberry.type
class Query:
    hello: str = "Hola mundo"

@strawberry.type
class Mutation(UserMutation, CreateArticle, UpdateArticle, DeleteArticle):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
