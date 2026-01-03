# GermanQuest Mobile App

React Native mobile application for learning German, built with Expo and TypeScript.

## Features

- **Vocabulary Trainer**: Interactive flashcard-style learning
- **Translation Tool**: Quick English-German translations
- **Learning Modules**: Gamified A1-level lessons
- **Progress Tracking**: Visual progress indicators
- **Offline-First**: Works without internet connection

## Tech Stack

- **Framework**: React Native with Expo
- **Language**: TypeScript
- **Platform**: iOS (primary), Android (future)
- **Navigation**: React Navigation (to be added)
- **State Management**: React Context / Redux (to be determined)

## Project Structure

```
frontend/
├── src/
│   ├── screens/          # Screen components
│   │   ├── Home/
│   │   ├── Vocabulary/
│   │   ├── Translation/
│   │   └── Progress/
│   ├── components/       # Reusable components
│   │   ├── common/      # Buttons, Cards, etc.
│   │   ├── vocabulary/  # Flashcards, WordList
│   │   └── learning/    # Quiz, LessonCard
│   ├── navigation/       # Navigation configuration
│   ├── services/        # API services
│   │   └── api.ts       # Backend API client
│   ├── utils/           # Utility functions
│   ├── types/           # TypeScript type definitions
│   ├── constants/       # App constants & config
│   └── hooks/           # Custom React hooks
├── assets/              # Images, fonts, icons
├── App.tsx             # Root component
├── app.json            # Expo configuration
└── package.json        # Dependencies
```

## Setup Instructions

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn
- Expo CLI (`npm install -g expo-cli`)
- iOS Simulator (Xcode) or Expo Go app on your iPhone

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Start Development Server

```bash
npm start
```

This will start the Expo development server and show a QR code.

### 3. Run on Device/Simulator

**iOS Simulator (macOS only):**
```bash
npm run ios
```

**iOS Device (via Expo Go):**
1. Install "Expo Go" app from App Store
2. Scan the QR code shown in the terminal

**Web (for testing):**
```bash
npm run web
```

## Available Scripts

- `npm start` - Start Expo development server
- `npm run ios` - Run on iOS simulator
- `npm run android` - Run on Android emulator
- `npm run web` - Run in web browser
- `npm test` - Run tests (to be configured)

## Configuration

### app.json

Main Expo configuration file. Update as needed:

```json
{
  "expo": {
    "name": "GermanQuest",
    "slug": "germanquest",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#ffffff"
    },
    "ios": {
      "supportsTablet": true,
      "bundleIdentifier": "com.germanquest.app"
    }
  }
}
```

## Connecting to Backend

The app will connect to the FastAPI backend running locally.

### API Configuration

Create `src/services/api.ts`:

```typescript
const API_BASE_URL = __DEV__
  ? 'http://localhost:8000'  // Development
  : 'https://your-production-url.com';  // Production

export const api = {
  baseURL: API_BASE_URL,
  // API methods will be defined here
};
```

## Development Guidelines

### File Naming Conventions

- Components: PascalCase (e.g., `VocabularyCard.tsx`)
- Utilities: camelCase (e.g., `formatDate.ts`)
- Screens: PascalCase folders (e.g., `Home/HomeScreen.tsx`)

### TypeScript

- Define types in `src/types/`
- Use interfaces for objects and props
- Avoid `any` type when possible

### Styling

- Use StyleSheet.create() for performance
- Consider using a styling library (e.g., styled-components, NativeWind)
- Keep styles close to components

## Next Steps

### Phase 1 - Core UI
- [ ] Set up navigation (React Navigation)
- [ ] Create Home screen
- [ ] Build Vocabulary Trainer UI
- [ ] Implement Translation screen
- [ ] Design Progress tracking screen

### Phase 2 - Backend Integration
- [ ] Set up API client
- [ ] Connect vocabulary trainer to backend
- [ ] Implement offline data persistence
- [ ] Add error handling and loading states

### Phase 3 - Features
- [ ] Add flashcard animations
- [ ] Implement spaced repetition algorithm
- [ ] Add pronunciation audio
- [ ] Create quiz mode
- [ ] Implement achievements/gamification

### Phase 4 - Polish
- [ ] Add splash screen
- [ ] Design app icon
- [ ] Improve UX/UI
- [ ] Add haptic feedback
- [ ] Performance optimization

## Dependencies to Add

```bash
# Navigation
npm install @react-navigation/native @react-navigation/native-stack
npm install react-native-screens react-native-safe-area-context

# State Management (optional)
npm install zustand
# or
npm install @reduxjs/toolkit react-redux

# API calls
npm install axios

# Local storage
npm install @react-native-async-storage/async-storage

# UI components (optional)
npm install react-native-paper
# or
npm install @rneui/themed
```

## Troubleshooting

### Metro Bundler Issues

```bash
# Clear cache and restart
npm start -- --clear
```

### iOS Build Issues

```bash
# Clean iOS build
cd ios && pod install && cd ..
npm run ios
```

### Expo Go Not Connecting

- Ensure your phone and computer are on the same network
- Check firewall settings
- Try using tunnel mode: `npm start -- --tunnel`

## Resources

- [Expo Documentation](https://docs.expo.dev/)
- [React Native Documentation](https://reactnative.dev/)
- [React Navigation](https://reactnavigation.org/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)

## Contributing

This is a personal learning project. Feedback and suggestions are welcome!
