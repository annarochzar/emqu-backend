import strawberry
from typing import List, Optional
from strawberry.types import Info
from sqlalchemy import select, desc

from sqlalchemy import and_
from app.models import ArticleModel
from app.config.database import async_session
from app.graphql.articles.types import ArticleType
from app.dependencies.auth import get_current_user
from app.models import UserModel
from app.models import TopicModel
from app.models import TagModel


@strawberry.type
class ArticleQueries:

    @strawberry.field
    async def get_all_articles(self) -> List[ArticleType]:
        async with async_session() as session:
            result = await session.execute(select(ArticleModel))
            return result.scalars().all()

    @strawberry.field
    async def get_my_articles(self, info: Info) -> List[ArticleType]:
        current_user: UserModel = await get_current_user(info)

        async with async_session() as session:
            result = await session.execute(
                select(ArticleModel).where(ArticleModel.author_id == current_user.id)
            )
            return result.scalars().all()

    @strawberry.field
    async def article_by_id(self, info: Info, id: int) -> Optional[ArticleType]:
        async with async_session() as session:
            article = await session.get(ArticleModel, id)
            return article

    @strawberry.field
    async def articles(self, info: Info,
                       topic_id: Optional[int] = None,
                       tag_id: Optional[int] = None,
                       author_id: Optional[int] = None,
                       limit: int = 10) -> List[ArticleType]:
        async with async_session() as session:
            query = select(ArticleModel)

            filters = []
            if topic_id:
                # Filtrar artículos que tengan el topic dado
                filters.append(ArticleModel.topics.any(TopicModel.id == topic_id))
            if tag_id:
                # Filtrar artículos que tengan la etiqueta dada
                filters.append(ArticleModel.tags.any(TagModel.id == tag_id))
            if author_id:
                filters.append(ArticleModel.author_id == author_id)

            if filters:
                query = query.where(and_(*filters))

            query = query.order_by(ArticleModel.created_at.desc()).limit(limit)

            result = await session.execute(query)
            return result.scalars().all()

    @strawberry.field
    async def get_last_articles(self, limit: int = 5) -> List[ArticleType]:
        async with async_session() as session:
            result = await session.execute(
                select(ArticleModel).order_by(desc(ArticleModel.created_at)).limit(limit)
            )
            return result.scalars().all()
