"""
Pydantic schemas for user stats endpoints
"""
from pydantic import BaseModel, Field
from typing import Optional


class UserStatsBase(BaseModel):
    """Base user stats schema"""
    current_streak: int = Field(default=0, ge=0)
    longest_streak: int = Field(default=0, ge=0)
    total_xp: int = Field(default=0, ge=0)
    words_learned: int = Field(default=0, ge=0)


class UserStatsCreate(UserStatsBase):
    """Schema for creating user stats"""
    pass


class UserStatsUpdate(BaseModel):
    """Schema for updating user stats"""
    current_streak: Optional[int] = Field(None, ge=0)
    longest_streak: Optional[int] = Field(None, ge=0)
    total_xp: Optional[int] = Field(None, ge=0)
    words_learned: Optional[int] = Field(None, ge=0)


class UserStatsResponse(UserStatsBase):
    """Schema for user stats response"""
    id: int

    class Config:
        from_attributes = True
