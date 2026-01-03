"""
Pydantic schemas for vocabulary endpoints
"""
from pydantic import BaseModel, Field
from typing import Optional

class VocabularyBase(BaseModel):
    """Base vocabulary schema"""
    german_word: str = Field(..., min_length=1, max_length=200)
    english_translation: str = Field(..., min_length=1, max_length=200)
    pronunciation: Optional[str] = None
    example_sentence_de: Optional[str] = None
    example_sentence_en: Optional[str] = None
    category: str
    difficulty_level: str = "A1"
    word_type: Optional[str] = None
    gender: Optional[str] = None

class VocabularyCreate(VocabularyBase):
    """Schema for creating vocabulary"""
    pass

class VocabularyResponse(VocabularyBase):
    """Schema for vocabulary response"""
    id: int

    class Config:
        from_attributes = True

class TranslationRequest(BaseModel):
    """Translation request schema"""
    text: str = Field(..., min_length=1)
    source_language: str = Field(default="en")
    target_language: str = Field(default="de")

class TranslationResponse(BaseModel):
    """Translation response schema"""
    original_text: str
    translated_text: str
    source_language: str
    target_language: str
