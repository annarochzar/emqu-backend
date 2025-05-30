# app/graphql/topics/mutations.py

import strawberry
from strawberry.types import Info
from app.models import TopicModel
from app.config.database import async_session
from app.graphql.topics.types import TopicType

@strawberry.input
class CreateTopicInput:
    name: str

@strawberry.type
class CreateTopic:
    @strawberry.mutation
    async def create_topic(self, info: Info, data: CreateTopicInput) -> TopicType:
        async with async_session() as session:
            topic = TopicModel(name=data.name)
            session.add(topic)
            await session.commit()
            await session.refresh(topic)
            return topic


@strawberry.input
class UpdateTopicInput:
    id: int
    name: str

@strawberry.type
class UpdateTopic:
    @strawberry.mutation
    async def update_topic(self, info: Info, data: UpdateTopicInput) -> TopicType:
        async with async_session() as session:
            topic = await session.get(TopicModel, data.id)
            if not topic:
                raise Exception("Tópico no encontrado.")

            topic.name = data.name
            await session.commit()
            await session.refresh(topic)
            return topic


@strawberry.type
class DeleteTopic:
    @strawberry.mutation
    async def delete_topic(self, info: Info, topic_id: int) -> bool:
        async with async_session() as session:
            topic = await session.get(TopicModel, topic_id)
            if not topic:
                raise Exception("Tópico no encontrado.")
            await session.delete(topic)
            await session.commit()
            return True
