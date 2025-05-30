# app/graphql/tags/mutations.py

import strawberry
from strawberry.types import Info
from app.models import TagModel
from app.config.database import async_session
from app.graphql.tags.types import TagType

@strawberry.input
class CreateTagInput:
    name: str

@strawberry.type
class CreateTag:
    @strawberry.mutation
    async def create_tag(self, info: Info, data: CreateTagInput) -> TagType:
        async with async_session() as session:
            tag = TagModel(name=data.name)
            session.add(tag)
            await session.commit()
            await session.refresh(tag)
            return tag


@strawberry.input
class UpdateTagInput:
    id: int
    name: str

@strawberry.type
class UpdateTag:
    @strawberry.mutation
    async def update_tag(self, info: Info, data: UpdateTagInput) -> TagType:
        async with async_session() as session:
            tag = await session.get(TagModel, data.id)
            if not tag:
                raise Exception("Etiqueta no encontrada.")
            tag.name = data.name
            await session.commit()
            await session.refresh(tag)
            return tag


@strawberry.type
class DeleteTag:
    @strawberry.mutation
    async def delete_tag(self, info: Info, tag_id: int) -> bool:
        async with async_session() as session:
            tag = await session.get(TagModel, tag_id)
            if not tag:
                raise Exception("Etiqueta no encontrada.")
            await session.delete(tag)
            await session.commit()
            return True
