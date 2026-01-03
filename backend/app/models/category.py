"""
Category database models
"""
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class Category(Base):
    """Category model for organizing vocabulary words"""
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True, index=True)
    icon = Column(String(50), nullable=True)  # Icon name or emoji
    description = Column(Text, nullable=True)

    # Relationship to words
    words = relationship("Word", back_populates="category")
