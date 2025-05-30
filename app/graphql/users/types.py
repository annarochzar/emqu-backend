import strawberry
from datetime import datetime

@strawberry.type
class UserType:
    id: int
    name: str
    email: str
    role: str
    created_at: datetime 

@strawberry.type
class LoginResponseType:
    access_token: str
    token_type: str
