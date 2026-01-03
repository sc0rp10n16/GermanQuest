"""
Word database models
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Word(Base):
    """Word model for vocabulary items"""
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    german_word = Column(String(200), nullable=False, index=True)
    english_translation = Column(String(200), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False, index=True)
    phonetic = Column(String(200), nullable=True)  # Phonetic pronunciation
    example_sentence = Column(Text, nullable=True)  # Example sentence in German
    audio_path = Column(String(500), nullable=True)  # Path to audio file

    # Relationships
    category = relationship("Category", back_populates="words")
    user_progress = relationship("UserProgress", back_populates="word")
