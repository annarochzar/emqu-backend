import strawberry
from typing import List
from strawberry.types import Info
from sqlalchemy import select, func

from app.config.database import async_session
from app.models import ArticleModel, TopicModel, UserModel
from app.graphql.statistics.types import TopicArticleCount, UserArticleCount
from app.dependencies.auth import get_current_user
from app.models.models import UserRoleEnum



@strawberry.type
class StatisticsQueries:

    @strawberry.field
    async def total_articles_by_topic(self, info: Info) -> List[TopicArticleCount]:
        current_user = await get_current_user(info)
        print("ROL:", current_user.role, type(current_user.role))

        if current_user.role != UserRoleEnum.moderator:
            raise Exception("Solo los moderadores pueden ver estadísticas.")

        async with async_session() as session:
            result = await session.execute(
                select(TopicModel.name, func.count(ArticleModel.id))
                .join(ArticleModel, TopicModel.id == ArticleModel.topic_id)
                .group_by(TopicModel.name)
            )
            return [TopicArticleCount(topic=t, count=c) for t, c in result.all()]

    @strawberry.field
    async def total_articles_by_user(self, info: Info) -> List[UserArticleCount]:
        current_user = await get_current_user(info)
        print("ROL:", current_user.role, type(current_user.role))

        if current_user.role != UserRoleEnum.moderator:
            raise Exception("Solo los moderadores pueden ver estadísticas.")

        async with async_session() as session:
            result = await session.execute(
                select(UserModel.name, func.count(ArticleModel.id))
                .join(ArticleModel, UserModel.id == ArticleModel.author_id)
                .group_by(UserModel.name)
            )
            return [UserArticleCount(user=u, count=c) for u, c in result.all()]

    @strawberry.field
    async def top_5_topics(self, info: Info) -> List[TopicArticleCount]:
        current_user = await get_current_user(info)
        print("ROL:", current_user.role, type(current_user.role))
        if current_user.role != UserRoleEnum.moderator:
            raise Exception("Solo los moderadores pueden ver estadísticas.")

        async with async_session() as session:
            result = await session.execute(
                select(TopicModel.name, func.count(ArticleModel.id))
                .join(ArticleModel, TopicModel.id == ArticleModel.topic_id)
                .group_by(TopicModel.name)
                .order_by(func.count(ArticleModel.id).desc())
                .limit(5)
            )
            return [TopicArticleCount(topic=t, count=c) for t, c in result.all()]
