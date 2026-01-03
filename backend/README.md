# GermanQuest Backend API

FastAPI-based REST API for the German Learning Companion application.

## Features

- RESTful API endpoints for vocabulary and learning modules
- SQLite database for offline-first functionality
- Vocabulary management and tracking
- User progress monitoring
- Translation services (planned)

## Tech Stack

- **Framework**: FastAPI 0.115.0
- **Database**: SQLite with SQLAlchemy ORM
- **Validation**: Pydantic
- **Server**: Uvicorn

## Project Structure

```
backend/
├── app/
│   ├── api/              # API route handlers
│   ├── core/             # Core configuration
│   │   ├── config.py     # Application settings
│   │   ├── database.py   # Database connection
│   │   └── init_db.py    # Database initialization
│   ├── models/           # SQLAlchemy models
│   │   ├── vocabulary.py
│   │   └── user_progress.py
│   ├── schemas/          # Pydantic schemas
│   │   └── vocabulary.py
│   ├── services/         # Business logic
│   └── utils/            # Utility functions
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
└── germanquest.db        # SQLite database (created on first run)
```

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Database

```bash
python -m app.core.init_db
```

This will:
- Create all necessary database tables
- Seed the database with initial vocabulary data (15+ words)

### 5. Run Development Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### 6. View API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Health & Status

- `GET /` - Root endpoint with API information
- `GET /health` - Health check endpoint

### Vocabulary (Coming Soon)

- `GET /api/v1/vocabulary` - Get all vocabulary words
- `GET /api/v1/vocabulary/{id}` - Get specific word
- `POST /api/v1/vocabulary` - Add new word
- `GET /api/v1/vocabulary/category/{category}` - Get words by category

### Translation (Coming Soon)

- `POST /api/v1/translate` - Translate text

### Progress Tracking (Coming Soon)

- `GET /api/v1/progress` - Get user progress
- `POST /api/v1/progress` - Update progress

## Database Models

### Vocabulary
- `id`: Primary key
- `german_word`: German word
- `english_translation`: English translation
- `pronunciation`: Phonetic pronunciation
- `category`: Word category (greetings, numbers, etc.)
- `difficulty_level`: A1, A2, or B1
- `word_type`: noun, verb, adjective, etc.
- `gender`: der, die, das (for nouns)
- `example_sentence_de`: Example sentence in German
- `example_sentence_en`: Example sentence in English

### UserProgress
- Tracks learning progress for each vocabulary word
- Records review counts, success rate, and mastery status

### LearningSession
- Tracks individual learning sessions
- Records session statistics and duration

## Environment Variables

Create a `.env` file in the backend directory (optional):

```env
APP_NAME=GermanQuest API
VERSION=1.0.0
DEBUG=True
DATABASE_URL=sqlite:///./germanquest.db
```

## Development

### Adding New Endpoints

1. Create route handler in `app/api/`
2. Define Pydantic schemas in `app/schemas/`
3. Implement business logic in `app/services/`
4. Import and include router in `main.py`

### Database Migrations

For schema changes:
1. Update models in `app/models/`
2. Delete `germanquest.db`
3. Run `python -m app.core.init_db` to recreate

## Testing

```bash
# Install testing dependencies
pip install pytest pytest-asyncio httpx

# Run tests
pytest
```

## Troubleshooting

### Database Issues

If you encounter database errors:
```bash
# Delete the database
rm germanquest.db

# Reinitialize
python -m app.core.init_db
```

### Port Already in Use

If port 8000 is busy:
```bash
uvicorn main:app --reload --port 8001
```

## Next Steps

- [ ] Implement vocabulary API endpoints
- [ ] Add translation service with Hugging Face models
- [ ] Create progress tracking endpoints
- [ ] Add authentication (if needed)
- [ ] Implement caching for performance
- [ ] Add comprehensive tests

## Contributing

This is a personal project, but suggestions are welcome!
