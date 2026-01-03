"""
Pydantic schemas
"""
from app.schemas.category import CategoryBase, CategoryCreate, CategoryUpdate, CategoryResponse
from app.schemas.word import WordBase, WordCreate, WordUpdate, WordResponse
from app.schemas.user_progress import UserProgressBase, UserProgressCreate, UserProgressUpdate, UserProgressResponse
from app.schemas.user_stats import UserStatsBase, UserStatsCreate, UserStatsUpdate, UserStatsResponse

__all__ = [
    "CategoryBase", "CategoryCreate", "CategoryUpdate", "CategoryResponse",
    "WordBase", "WordCreate", "WordUpdate", "WordResponse",
    "UserProgressBase", "UserProgressCreate", "UserProgressUpdate", "UserProgressResponse",
    "UserStatsBase", "UserStatsCreate", "UserStatsUpdate", "UserStatsResponse",
]
