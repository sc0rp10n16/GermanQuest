"""
Pydantic schemas for word endpoints
"""
from pydantic import BaseModel, Field
from typing import Optional


class WordBase(BaseModel):
    """Base word schema"""
    german_word: str = Field(..., min_length=1, max_length=200)
    english_translation: str = Field(..., min_length=1, max_length=200)
    category_id: int
    phonetic: Optional[str] = Field(None, max_length=200)
    example_sentence: Optional[str] = None
    audio_path: Optional[str] = Field(None, max_length=500)


class WordCreate(WordBase):
    """Schema for creating a word"""
    pass


class WordUpdate(BaseModel):
    """Schema for updating a word"""
    german_word: Optional[str] = Field(None, min_length=1, max_length=200)
    english_translation: Optional[str] = Field(None, min_length=1, max_length=200)
    category_id: Optional[int] = None
    phonetic: Optional[str] = Field(None, max_length=200)
    example_sentence: Optional[str] = None
    audio_path: Optional[str] = Field(None, max_length=500)


class WordResponse(WordBase):
    """Schema for word response"""
    id: int

    class Config:
        from_attributes = True
