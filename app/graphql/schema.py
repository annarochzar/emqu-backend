import strawberry
from app.graphql.users.mutations import UserMutation
from app.graphql.articles.mutations import CreateArticle, UpdateArticle, DeleteArticle
from app.graphql.tags.mutations import CreateTag
from app.graphql.topics.mutations import CreateTopic

@strawberry.type
class Query:
    hello: str = "Hola mundo"

@strawberry.type
class Mutation(UserMutation, CreateArticle, UpdateArticle, DeleteArticle, CreateTag, CreateTopic):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
