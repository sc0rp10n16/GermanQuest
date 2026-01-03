"""
Vocabulary database models
"""
from sqlalchemy import Column, Integer, String, Text, Enum
from app.core.database import Base
import enum

class DifficultyLevel(enum.Enum):
    """Difficulty levels for vocabulary"""
    A1 = "A1"
    A2 = "A2"
    B1 = "B1"

class Category(enum.Enum):
    """Vocabulary categories"""
    GREETINGS = "greetings"
    NUMBERS = "numbers"
    DAILY_OBJECTS = "daily_objects"
    BASIC_VERBS = "basic_verbs"
    FOOD_ITEMS = "food_items"
    TRAVEL_PHRASES = "travel_phrases"

class Vocabulary(Base):
    """Vocabulary word model"""
    __tablename__ = "vocabulary"

    id = Column(Integer, primary_key=True, index=True)
    german_word = Column(String(200), nullable=False, index=True)
    english_translation = Column(String(200), nullable=False)
    pronunciation = Column(String(200), nullable=True)
    example_sentence_de = Column(Text, nullable=True)
    example_sentence_en = Column(Text, nullable=True)
    category = Column(String(50), nullable=False)
    difficulty_level = Column(String(10), nullable=False, default="A1")
    word_type = Column(String(50), nullable=True)  # noun, verb, adjective, etc.
    gender = Column(String(10), nullable=True)  # der, die, das for nouns
