"""
Pydantic schemas for user progress endpoints
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UserProgressBase(BaseModel):
    """Base user progress schema"""
    word_id: int
    times_seen: int = Field(default=0, ge=0)
    times_correct: int = Field(default=0, ge=0)
    last_reviewed: Optional[datetime] = None
    mastery_level: float = Field(default=0.0, ge=0.0, le=1.0)


class UserProgressCreate(BaseModel):
    """Schema for creating user progress"""
    word_id: int
    times_seen: int = Field(default=0, ge=0)
    times_correct: int = Field(default=0, ge=0)
    last_reviewed: Optional[datetime] = None
    mastery_level: float = Field(default=0.0, ge=0.0, le=1.0)


class UserProgressUpdate(BaseModel):
    """Schema for updating user progress"""
    times_seen: Optional[int] = Field(None, ge=0)
    times_correct: Optional[int] = Field(None, ge=0)
    last_reviewed: Optional[datetime] = None
    mastery_level: Optional[float] = Field(None, ge=0.0, le=1.0)


class UserProgressResponse(UserProgressBase):
    """Schema for user progress response"""
    id: int

    class Config:
        from_attributes = True
