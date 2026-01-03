"""
Quick database query script - shows database statistics
"""
from app.core.database import SessionLocal
from app.models import Category, Word, UserProgress, UserStats

db = SessionLocal()

try:
    # Get counts
    category_count = db.query(Category).count()
    word_count = db.query(Word).count()
    progress_count = db.query(UserProgress).count()
    stats = db.query(UserStats).first()

    print("\n📊 DATABASE STATISTICS")
    print("=" * 40)
    print(f"Categories: {category_count}")
    print(f"Words: {word_count}")
    print(f"User Progress Records: {progress_count}")
    print(f"\n👤 USER STATS")
    print(f"Streak: {stats.current_streak} (longest: {stats.longest_streak})")
    print(f"Total XP: {stats.total_xp}")
    print(f"Words Learned: {stats.words_learned}")

    print(f"\n📚 WORDS PER CATEGORY")
    print("-" * 40)
    categories = db.query(Category).all()
    for cat in categories:
        word_count_in_cat = len(cat.words)
        print(f"{cat.icon} {cat.name:20s} {word_count_in_cat:3d} words")

    print("\n")

finally:
    db.close()
