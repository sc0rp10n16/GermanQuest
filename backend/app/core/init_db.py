"""
Database initialization script
Seeds the database with initial vocabulary data
"""
from sqlalchemy.orm import Session
from app.models.vocabulary import Vocabulary
from app.core.database import SessionLocal, engine, Base

def init_vocabulary_data(db: Session):
    """Initialize vocabulary table with sample data"""

    # Check if data already exists
    if db.query(Vocabulary).first():
        print("Vocabulary data already exists, skipping initialization")
        return

    # Sample vocabulary data
    sample_vocabulary = [
        # Greetings
        {"german_word": "Hallo", "english_translation": "Hello", "pronunciation": "HAH-loh",
         "category": "greetings", "difficulty_level": "A1", "word_type": "interjection"},
        {"german_word": "Guten Morgen", "english_translation": "Good morning", "pronunciation": "GOO-ten MOR-gen",
         "category": "greetings", "difficulty_level": "A1", "word_type": "phrase"},
        {"german_word": "Auf Wiedersehen", "english_translation": "Goodbye", "pronunciation": "owf VEE-der-zayn",
         "category": "greetings", "difficulty_level": "A1", "word_type": "phrase"},
        {"german_word": "Danke", "english_translation": "Thank you", "pronunciation": "DAHN-keh",
         "category": "greetings", "difficulty_level": "A1", "word_type": "interjection"},
        {"german_word": "Bitte", "english_translation": "Please/You're welcome", "pronunciation": "BIT-teh",
         "category": "greetings", "difficulty_level": "A1", "word_type": "interjection"},

        # Numbers
        {"german_word": "eins", "english_translation": "one", "pronunciation": "eyns",
         "category": "numbers", "difficulty_level": "A1", "word_type": "number"},
        {"german_word": "zwei", "english_translation": "two", "pronunciation": "tsvey",
         "category": "numbers", "difficulty_level": "A1", "word_type": "number"},
        {"german_word": "drei", "english_translation": "three", "pronunciation": "dry",
         "category": "numbers", "difficulty_level": "A1", "word_type": "number"},

        # Daily Objects
        {"german_word": "das Wasser", "english_translation": "water", "pronunciation": "VAS-ser",
         "category": "daily_objects", "difficulty_level": "A1", "word_type": "noun", "gender": "das"},
        {"german_word": "das Brot", "english_translation": "bread", "pronunciation": "broht",
         "category": "food_items", "difficulty_level": "A1", "word_type": "noun", "gender": "das"},
        {"german_word": "die Milch", "english_translation": "milk", "pronunciation": "milkh",
         "category": "food_items", "difficulty_level": "A1", "word_type": "noun", "gender": "die"},

        # Basic Verbs
        {"german_word": "sein", "english_translation": "to be", "pronunciation": "zyne",
         "category": "basic_verbs", "difficulty_level": "A1", "word_type": "verb"},
        {"german_word": "haben", "english_translation": "to have", "pronunciation": "HAH-ben",
         "category": "basic_verbs", "difficulty_level": "A1", "word_type": "verb"},
        {"german_word": "gehen", "english_translation": "to go", "pronunciation": "GAY-en",
         "category": "basic_verbs", "difficulty_level": "A1", "word_type": "verb"},
        {"german_word": "kommen", "english_translation": "to come", "pronunciation": "KOM-men",
         "category": "basic_verbs", "difficulty_level": "A1", "word_type": "verb"},
    ]

    # Add vocabulary to database
    for vocab_data in sample_vocabulary:
        vocab = Vocabulary(**vocab_data)
        db.add(vocab)

    db.commit()
    print(f"Initialized {len(sample_vocabulary)} vocabulary words")

def init_db():
    """Initialize database with tables and seed data"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully")

    db = SessionLocal()
    try:
        print("Initializing vocabulary data...")
        init_vocabulary_data(db)
        print("Database initialization completed successfully")
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
