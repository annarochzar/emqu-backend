import strawberry
from datetime import datetime

@strawberry.type
class TopicType:
    id: int
    name: str