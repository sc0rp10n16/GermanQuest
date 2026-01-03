# GermanQuest - German Learning Companion

A personal, offline-first mobile application designed to help newcomers to Germany learn the German language efficiently, focusing on practical communication and survival skills.

## Project Overview

GermanQuest is a comprehensive language learning application consisting of:
- **Frontend**: React Native mobile app (iOS focused) built with Expo and TypeScript
- **Backend**: FastAPI REST API with SQLite database

## Features

- **Vocabulary Trainer**: Build foundational German vocabulary with 500+ basic words
- **Translation Tool**: Offline text translation between English and German
- **Learning Modules**: Interactive A1-level learning experiences with gamification
- **Progress Tracking**: Monitor your learning journey and track improvements
- **Offline-First**: Full functionality without internet connection

## Technology Stack

### Frontend
- React Native with Expo
- TypeScript
- iOS platform (primary target)

### Backend
- FastAPI (Python)
- SQLite database
- SQLAlchemy ORM

## Project Structure

```
GermanQuest/
├── frontend/               # React Native mobile app
│   ├── src/
│   │   ├── screens/       # Screen components
│   │   ├── components/    # Reusable components
│   │   ├── navigation/    # Navigation configuration
│   │   ├── services/      # API services
│   │   ├── utils/         # Utility functions
│   │   ├── types/         # TypeScript types
│   │   ├── constants/     # App constants
│   │   └── hooks/         # Custom React hooks
│   └── assets/            # Images, fonts, etc.
│
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── models/       # Database models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── services/     # Business logic
│   │   ├── core/         # Config & database
│   │   └── utils/        # Utility functions
│   └── main.py           # FastAPI application
│
└── German_Learning_Companion_PRD.md  # Product Requirements Document
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python 3.11+
- iOS device or simulator (for mobile testing)
- Expo CLI

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python -m app.core.init_db  # Initialize database
uvicorn main:app --reload  # Start server
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
npm start  # Start Expo development server
```

Scan the QR code with Expo Go app on your iOS device or press `i` to open in iOS simulator.

## Development Roadmap

### Phase 1: Setup and Core Features ✅
- [x] Project initialization
- [x] Basic folder structure
- [x] Database setup
- [ ] Vocabulary trainer UI
- [ ] Basic translation module

### Phase 2: AI and Learning Features
- [ ] Integrate offline AI models
- [ ] Pronunciation support
- [ ] Learning path development
- [ ] Performance optimization

### Phase 3: Testing and Refinement
- [ ] Functionality testing
- [ ] User experience review
- [ ] Performance tuning
- [ ] Bug fixes

## Documentation

- [Product Requirements Document](./German_Learning_Companion_PRD.md)
- [Backend Documentation](./backend/README.md)
- [Frontend Documentation](./frontend/README.md)

## License

This is a personal project for educational purposes.

## Contact

For questions or feedback, please create an issue in the repository.
