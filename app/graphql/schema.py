import strawberry

# Mutaciones
from app.graphql.users.mutations import UserMutation
from app.graphql.articles.mutations import CreateArticle, UpdateArticle, DeleteArticle
from app.graphql.tags.mutations import CreateTag
from app.graphql.topics.mutations import CreateTopic

# Consultas
from app.graphql.articles.queries import ArticleQueries
from app.graphql.statistics.queries import StatisticsQueries

@strawberry.type
class Query(
    ArticleQueries,
    StatisticsQueries
):
    pass

@strawberry.type
class Mutation(
    UserMutation,
    CreateArticle,
    UpdateArticle,
    DeleteArticle,
    CreateTag,
    CreateTopic,
):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
