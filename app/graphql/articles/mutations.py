# app/graphql/articles/mutations.py

import strawberry
from typing import List
from strawberry.types import Info
from datetime import datetime

from app.models import ArticleModel, TagModel, TopicModel
from app.config.database import async_session
from app.graphql.articles.types import ArticleType
from app.dependencies.auth import get_current_user
from app.models import UserModel
from sqlalchemy import select


@strawberry.input
class CreateArticleInput:
    title: str
    content: str
    topic_ids: List[int]
    tag_ids: List[int]

@strawberry.type
class CreateArticle:
    @strawberry.mutation
    async def create_article(self, info: Info, data: CreateArticleInput) -> ArticleType:
        current_user: UserModel = await get_current_user(info)

        async with async_session() as session:
            # Crear artículo base
            new_article = ArticleModel(
                title=data.title,
                content=data.content,
                created_at=datetime.utcnow(),
                author_id=current_user.id
            )

            # Agregar temas
            topics = await session.execute(
                select(TopicModel).where(TopicModel.id.in_(data.topic_ids))
            )
            new_article.topics = topics.scalars().all()

            # Agregar etiquetas
            tags_result = await session.execute(
                select(TagModel).where(TagModel.id.in_(data.tag_ids))
            )
            new_article.tags = tags_result.scalars().all()


            session.add(new_article)
            await session.commit()
            await session.refresh(new_article)

            return new_article


@strawberry.input
class UpdateArticleInput:
    id: int
    title: str
    content: str
    topic_ids: List[int]
    tag_ids: List[int]

@strawberry.type
class UpdateArticle:
    @strawberry.mutation
    async def update_article(self, info: Info, data: UpdateArticleInput) -> ArticleType:
        current_user: UserModel = await get_current_user(info)

        async with async_session() as session:
            article = await session.get(ArticleModel, data.id)

            if not article:
                raise Exception("Artículo no encontrado.")
            if article.author_id != current_user.id:
                raise Exception("No tienes permiso para modificar este artículo.")

            article.title = data.title
            article.content = data.content

            # Actualizar relaciones
            new_topics_result = await session.execute(
                select(TopicModel).where(TopicModel.id.in_(data.topic_ids))
            )
            article.topics = new_topics_result.scalars().all()

            new_tags_result = await session.execute(
                select(TagModel).where(TagModel.id.in_(data.tag_ids))
            )
            article.tags = new_tags_result.scalars().all()


            await session.commit()
            await session.refresh(article)

            return article



@strawberry.type
class DeleteArticle:
    @strawberry.mutation
    async def delete_article(self, info: Info, article_id: int) -> bool:
        current_user: UserModel = await get_current_user(info)

        async with async_session() as session:
            article = await session.get(ArticleModel, article_id)

            if not article:
                raise Exception("Artículo no encontrado.")
            if article.author_id != current_user.id:
                raise Exception("No tienes permiso para eliminar este artículo.")

            await session.delete(article)
            await session.commit()
            return True
