"""
User progress tracking models
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.core.database import Base

class UserProgress(Base):
    """User learning progress model"""
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    vocabulary_id = Column(Integer, ForeignKey("vocabulary.id"), nullable=False)
    times_reviewed = Column(Integer, default=0)
    times_correct = Column(Integer, default=0)
    times_incorrect = Column(Integer, default=0)
    is_mastered = Column(Boolean, default=False)
    last_reviewed = Column(DateTime(timezone=True), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class LearningSession(Base):
    """Learning session tracking"""
    __tablename__ = "learning_sessions"

    id = Column(Integer, primary_key=True, index=True)
    session_date = Column(DateTime(timezone=True), server_default=func.now())
    words_practiced = Column(Integer, default=0)
    correct_answers = Column(Integer, default=0)
    incorrect_answers = Column(Integer, default=0)
    duration_minutes = Column(Integer, nullable=True)
    category = Column(String(50), nullable=True)
