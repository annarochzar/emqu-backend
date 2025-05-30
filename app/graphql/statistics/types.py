import strawberry

@strawberry.type
class TopicArticleCount:
    topic: str
    count: int

@strawberry.type
class UserArticleCount:
    user: str
    count: int
