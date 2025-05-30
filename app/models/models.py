from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum 
from sqlalchemy import Enum


from app.config.database import Base 

class UserRoleEnum(str, enum.Enum):
    author = "author"
    moderator = "moderator"

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRoleEnum), default=UserRoleEnum.author, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    articles = relationship(
        "ArticleModel", 
        back_populates="author",
        lazy="selectin",
    )

class ArticleModel(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    author_id = Column(Integer, ForeignKey("users.id"))
    
    author = relationship(
        "UserModel", 
        foreign_keys=[author_id],
        back_populates="articles",
        lazy="selectin",
    )

    tags = relationship(
        "TagModel",
        secondary="article_tag",
        back_populates="articles",
        lazy="selectin",
    )

    topics = relationship(
        "TopicModel",
        secondary="article_topic",
        back_populates="articles",
        lazy="selectin",
    )

class TopicModel(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)

    articles = relationship(
        "ArticleModel",
        secondary="article_topic",
        back_populates="topics",
        lazy="selectin",
    )

class TagModel(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)

    articles = relationship(
        "ArticleModel",
        secondary="article_tag",
        back_populates="tags",
        lazy="selectin",
    )

class ArticleTopicModel(Base):
    __tablename__ = "article_topic"

    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id"), primary_key=True)

class ArticleTagModel(Base):
    __tablename__ = "article_tag"

    article_id = Column(Integer, ForeignKey("articles.id"), primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), primary_key=True)
