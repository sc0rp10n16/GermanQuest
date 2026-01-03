"""
Test script to interact with the database
"""
from app.core.database import SessionLocal
from app.models import Category, Word, UserProgress, UserStats

def test_categories():
    """Test querying categories"""
    print("\n" + "="*60)
    print("CATEGORIES")
    print("="*60)
    db = SessionLocal()
    try:
        categories = db.query(Category).all()
        print(f"Found {len(categories)} categories:\n")
        for cat in categories:
            print(f"  {cat.icon} {cat.name}")
            print(f"     ID: {cat.id}")
            print(f"     Description: {cat.description}")
            print(f"     Words in category: {len(cat.words)}")
            print()
    finally:
        db.close()

def test_words():
    """Test querying words"""
    print("\n" + "="*60)
    print("SAMPLE WORDS")
    print("="*60)
    db = SessionLocal()
    try:
        # Get first 5 words
        words = db.query(Word).limit(5).all()
        print(f"Showing first 5 words:\n")
        for word in words:
            print(f"  {word.german_word} = {word.english_translation}")
            print(f"     Phonetic: {word.phonetic}")
            print(f"     Category: {word.category.name}")
            print(f"     Example: {word.example_sentence}")
            print()
    finally:
        db.close()

def test_words_by_category():
    """Test querying words by category"""
    print("\n" + "="*60)
    print("WORDS BY CATEGORY - Greetings")
    print("="*60)
    db = SessionLocal()
    try:
        category = db.query(Category).filter(Category.name == "Greetings").first()
        if category:
            print(f"\nWords in '{category.name}' category:\n")
            for word in category.words:
                print(f"  {word.german_word} = {word.english_translation}")
                print(f"     {word.phonetic}")
                print()
    finally:
        db.close()

def test_user_stats():
    """Test querying user stats"""
    print("\n" + "="*60)
    print("USER STATS")
    print("="*60)
    db = SessionLocal()
    try:
        stats = db.query(UserStats).first()
        if stats:
            print(f"\n  Current Streak: {stats.current_streak} days")
            print(f"  Longest Streak: {stats.longest_streak} days")
            print(f"  Total XP: {stats.total_xp}")
            print(f"  Words Learned: {stats.words_learned}")
            print()
    finally:
        db.close()

def test_create_progress():
    """Test creating user progress"""
    print("\n" + "="*60)
    print("CREATE USER PROGRESS")
    print("="*60)
    db = SessionLocal()
    try:
        # Get a word
        word = db.query(Word).first()

        # Check if progress exists
        existing = db.query(UserProgress).filter(UserProgress.word_id == word.id).first()

        if existing:
            print(f"\nProgress already exists for '{word.german_word}'")
            print(f"  Times seen: {existing.times_seen}")
            print(f"  Times correct: {existing.times_correct}")
            print(f"  Mastery level: {existing.mastery_level}")
        else:
            # Create new progress
            from datetime import datetime
            progress = UserProgress(
                word_id=word.id,
                times_seen=1,
                times_correct=0,
                last_reviewed=datetime.now(),
                mastery_level=0.0
            )
            db.add(progress)
            db.commit()
            print(f"\nCreated progress tracking for '{word.german_word}'")
            print(f"  Times seen: {progress.times_seen}")
            print(f"  Times correct: {progress.times_correct}")
            print(f"  Mastery level: {progress.mastery_level}")
        print()
    finally:
        db.close()

def test_update_stats():
    """Test updating user stats"""
    print("\n" + "="*60)
    print("UPDATE USER STATS")
    print("="*60)
    db = SessionLocal()
    try:
        stats = db.query(UserStats).first()
        if stats:
            # Update stats
            old_xp = stats.total_xp
            old_words = stats.words_learned

            stats.total_xp += 10
            stats.words_learned += 1
            stats.current_streak = 1

            db.commit()

            print(f"\nUpdated user stats:")
            print(f"  Total XP: {old_xp} → {stats.total_xp}")
            print(f"  Words Learned: {old_words} → {stats.words_learned}")
            print(f"  Current Streak: {stats.current_streak}")
            print()
    finally:
        db.close()

if __name__ == "__main__":
    print("\n" + "🇩🇪 GERMANQUEST DATABASE TEST 🇩🇪".center(60))

    try:
        test_categories()
        test_words()
        test_words_by_category()
        test_user_stats()
        test_create_progress()
        test_update_stats()

        print("\n" + "="*60)
        print("✅ ALL TESTS COMPLETED SUCCESSFULLY")
        print("="*60 + "\n")

    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        import traceback
        traceback.print_exc()
