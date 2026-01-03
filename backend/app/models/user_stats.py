"""
User statistics models
"""
from sqlalchemy import Column, Integer
from app.core.database import Base


class UserStats(Base):
    """User statistics model for tracking overall progress"""
    __tablename__ = "user_stats"

    id = Column(Integer, primary_key=True, index=True)
    current_streak = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    total_xp = Column(Integer, default=0)
    words_learned = Column(Integer, default=0)
