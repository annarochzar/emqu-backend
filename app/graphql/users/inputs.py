import strawberry

@strawberry.input
class RegisterUserInput:
    name: str
    email: str
    password: str
    role: str = "author"  # Por defecto "author", pero puede ser "moderator"