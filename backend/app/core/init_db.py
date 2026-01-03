"""
Database initialization script
Creates tables and seeds the database with initial data
"""
from sqlalchemy.orm import Session
from app.models import Category, Word, UserStats
from app.core.database import SessionLocal, engine, Base


def init_categories(db: Session):
    """Initialize categories table with default categories"""

    # Check if data already exists
    if db.query(Category).first():
        print("Categories already exist, skipping initialization")
        return

    # Default categories
    categories = [
        {
            "name": "Greetings",
            "icon": "👋",
            "description": "Common greetings and polite expressions"
        },
        {
            "name": "Numbers",
            "icon": "🔢",
            "description": "Cardinal and ordinal numbers"
        },
        {
            "name": "Daily Objects",
            "icon": "🏠",
            "description": "Common household and daily items"
        },
        {
            "name": "Basic Verbs",
            "icon": "🏃",
            "description": "Essential verbs for everyday communication"
        },
        {
            "name": "Food Items",
            "icon": "🍽️",
            "description": "Common foods and drinks"
        },
        {
            "name": "Travel Phrases",
            "icon": "✈️",
            "description": "Useful phrases for traveling"
        },
    ]

    for cat_data in categories:
        category = Category(**cat_data)
        db.add(category)

    db.commit()
    print(f"Initialized {len(categories)} categories")


def init_words(db: Session):
    """Initialize words table with sample vocabulary"""

    # Check if data already exists
    if db.query(Word).first():
        print("Words already exist, skipping initialization")
        return

    # Get category IDs
    greetings = db.query(Category).filter(Category.name == "Greetings").first()
    numbers = db.query(Category).filter(Category.name == "Numbers").first()
    daily_objects = db.query(Category).filter(Category.name == "Daily Objects").first()
    basic_verbs = db.query(Category).filter(Category.name == "Basic Verbs").first()
    food_items = db.query(Category).filter(Category.name == "Food Items").first()

    # Sample words
    sample_words = [
        # Greetings
        {
            "german_word": "Hallo",
            "english_translation": "Hello",
            "category_id": greetings.id,
            "phonetic": "HAH-loh",
            "example_sentence": "Hallo, wie geht es dir?",
        },
        {
            "german_word": "Guten Morgen",
            "english_translation": "Good morning",
            "category_id": greetings.id,
            "phonetic": "GOO-ten MOR-gen",
            "example_sentence": "Guten Morgen! Schön dich zu sehen.",
        },
        {
            "german_word": "Auf Wiedersehen",
            "english_translation": "Goodbye",
            "category_id": greetings.id,
            "phonetic": "owf VEE-der-zayn",
            "example_sentence": "Auf Wiedersehen, bis morgen!",
        },
        {
            "german_word": "Danke",
            "english_translation": "Thank you",
            "category_id": greetings.id,
            "phonetic": "DAHN-keh",
            "example_sentence": "Danke für deine Hilfe!",
        },
        {
            "german_word": "Bitte",
            "english_translation": "Please / You're welcome",
            "category_id": greetings.id,
            "phonetic": "BIT-teh",
            "example_sentence": "Bitte, gern geschehen!",
        },

        # Numbers
        {
            "german_word": "eins",
            "english_translation": "one",
            "category_id": numbers.id,
            "phonetic": "eyns",
            "example_sentence": "Ich habe eins davon.",
        },
        {
            "german_word": "zwei",
            "english_translation": "two",
            "category_id": numbers.id,
            "phonetic": "tsvey",
            "example_sentence": "Zwei Kaffee, bitte.",
        },
        {
            "german_word": "drei",
            "english_translation": "three",
            "category_id": numbers.id,
            "phonetic": "dry",
            "example_sentence": "Es sind drei Personen hier.",
        },
        {
            "german_word": "vier",
            "english_translation": "four",
            "category_id": numbers.id,
            "phonetic": "feer",
            "example_sentence": "Der Tisch hat vier Beine.",
        },
        {
            "german_word": "fünf",
            "english_translation": "five",
            "category_id": numbers.id,
            "phonetic": "fewnf",
            "example_sentence": "Fünf Minuten, bitte!",
        },

        # Daily Objects
        {
            "german_word": "das Wasser",
            "english_translation": "water",
            "category_id": daily_objects.id,
            "phonetic": "dahs VAS-ser",
            "example_sentence": "Ich trinke Wasser.",
        },
        {
            "german_word": "der Tisch",
            "english_translation": "table",
            "category_id": daily_objects.id,
            "phonetic": "dehr TISH",
            "example_sentence": "Der Tisch ist groß.",
        },
        {
            "german_word": "der Stuhl",
            "english_translation": "chair",
            "category_id": daily_objects.id,
            "phonetic": "dehr SHTOOL",
            "example_sentence": "Der Stuhl ist bequem.",
        },

        # Basic Verbs
        {
            "german_word": "sein",
            "english_translation": "to be",
            "category_id": basic_verbs.id,
            "phonetic": "zyne",
            "example_sentence": "Ich bin Student.",
        },
        {
            "german_word": "haben",
            "english_translation": "to have",
            "category_id": basic_verbs.id,
            "phonetic": "HAH-ben",
            "example_sentence": "Ich habe einen Hund.",
        },
        {
            "german_word": "gehen",
            "english_translation": "to go",
            "category_id": basic_verbs.id,
            "phonetic": "GAY-en",
            "example_sentence": "Ich gehe nach Hause.",
        },
        {
            "german_word": "kommen",
            "english_translation": "to come",
            "category_id": basic_verbs.id,
            "phonetic": "KOM-men",
            "example_sentence": "Ich komme aus Deutschland.",
        },
        {
            "german_word": "machen",
            "english_translation": "to do / to make",
            "category_id": basic_verbs.id,
            "phonetic": "MAH-khen",
            "example_sentence": "Was machst du?",
        },

        # Food Items
        {
            "german_word": "das Brot",
            "english_translation": "bread",
            "category_id": food_items.id,
            "phonetic": "dahs BROHT",
            "example_sentence": "Ich esse Brot zum Frühstück.",
        },
        {
            "german_word": "die Milch",
            "english_translation": "milk",
            "category_id": food_items.id,
            "phonetic": "dee MILKH",
            "example_sentence": "Die Milch ist frisch.",
        },
        {
            "german_word": "der Käse",
            "english_translation": "cheese",
            "category_id": food_items.id,
            "phonetic": "dehr KAY-zeh",
            "example_sentence": "Der Käse schmeckt gut.",
        },
    ]

    # Add words to database
    for word_data in sample_words:
        word = Word(**word_data)
        db.add(word)

    db.commit()
    print(f"Initialized {len(sample_words)} words")


def init_user_stats(db: Session):
    """Initialize default user stats"""

    # Check if data already exists
    if db.query(UserStats).first():
        print("User stats already exist, skipping initialization")
        return

    # Create default user stats
    user_stats = UserStats(
        current_streak=0,
        longest_streak=0,
        total_xp=0,
        words_learned=0
    )
    db.add(user_stats)
    db.commit()
    print("Initialized user stats")


def init_db():
    """Initialize database with tables and seed data"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")

    db = SessionLocal()
    try:
        print("\nInitializing categories...")
        init_categories(db)

        print("\nInitializing words...")
        init_words(db)

        print("\nInitializing user stats...")
        init_user_stats(db)

        print("\nDatabase initialization completed successfully!")
    finally:
        db.close()


if __name__ == "__main__":
    init_db()
