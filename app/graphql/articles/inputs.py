import strawberry

@strawberry.input
class ArticleInput:
    title: str
    content: str
    tag_ids: list[int]  # asumiendo que los tags ya existen
    topic_ids: list[int]  # asumiendo que los topics ya existen