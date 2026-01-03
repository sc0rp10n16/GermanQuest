"""
User progress tracking models
"""
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class UserProgress(Base):
    """User learning progress model"""
    __tablename__ = "user_progress"

    id = Column(Integer, primary_key=True, index=True)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False, index=True)
    times_seen = Column(Integer, default=0)
    times_correct = Column(Integer, default=0)
    last_reviewed = Column(DateTime(timezone=True), nullable=True)
    mastery_level = Column(Float, default=0.0)  # 0.0 to 1.0 scale

    # Relationship
    word = relationship("Word", back_populates="user_progress")
