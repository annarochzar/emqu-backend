# app/graphql/articles/types.py
import strawberry
from datetime import datetime

from app.graphql.tags.types import TagType
from app.graphql.topics.types import TopicType
from app.graphql.users.types import UserType  # importa el tipo de usuario


@strawberry.type
class ArticleType:
    id: int
    title: str
    content: str
    date: datetime
    author_id: int
    tags: list[TagType]
    topics: list[TopicType]

    # Alias para 'date' con el nombre que espera el frontend
    @strawberry.field(name="createdAt")
    def created_at(self) -> datetime:
        return self.date

    # Relación con el autor (tipo UserType)
    @strawberry.field
    def author(self) -> UserType:
        return self.author  # esto asume que tu modelo tiene .author
