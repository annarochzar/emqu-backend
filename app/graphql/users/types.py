import strawberry
from datetime import datetime

@strawberry.type
class UserType:
    id: int
    name: str
    email: str
    role: str
    created_at: datetime 