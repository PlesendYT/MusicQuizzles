# MusicQuizzles 🎵

A fun music guessing game powered by the **Deezer API**. Listen to song previews and test your music knowledge across multiple game modes.

## ✨ Features

### 🎮 Game Modes
| Mode | Description |
|------|-------------|
| **Easy** | Yes/No — is this a song by the selected artist? |
| **Medium** | Multiple choice — pick the correct song title |
| **Hard** | Type the song name — fuzzy matching (70% threshold) |
| **Year** | Guess the release year of the song |
| **Mixed** | Random question types every round |
| **Lives** | 3 hearts — wrong answer costs a life. Game Over at 0 |

### ⚙️ Options
- **Round count** — 5 / 10 / 15 / 20 / ∞ Endless
- **Timer** — optional countdown with bonus points
- **Playlist** — select multiple artists for a mixed track pool
- **Hints** — blur reduction in 3 stages (5 points each)
- **Skip** — skip a question for -2 points
- **Auto-Advance** — automatically proceed after a correct answer

### 🏆 Achievements
Unlockable badges: First Game, 10 Games, 100 Songs, Perfect Game, Streak 5, Endless Hero, All Modes

### 📊 Statistics
Persisted in localStorage: total games, points, accuracy, best scores

### 🎨 Other
- Streak system (🔥 multiplier for consecutive correct answers)
- Album art blur / hint system
- Audio visualizer (CSS-based)
- Keyboard navigation (search suggestions)
- Swipe gestures (Easy mode on mobile)
- Dark & Light theme
- Fullscreen support
- Haptic feedback (vibration, adjustable intensity)
- Sound effects (Web Audio API)
- Volume control (persisted)
- Share results (Web Share API / clipboard)

## 🚀 Getting Started

### Prerequisites
- Python 3

### Installation
```bash
git clone https://github.com/YOUR_USER/MusicQuizzles.git
cd MusicQuizzles
```

### Running
```bash
python3 server.py
```

Open **http://localhost:3001** in your browser.

The server proxies requests to the [Deezer API](https://developers.deezer.com/api) to avoid CORS issues.

## 🏗️ Architecture

```
MusicQuizzles/
├── index.html     # Single-file frontend (HTML + CSS + JS)
├── server.py      # Python HTTP server with caching + retry logic
└── github data    # GitHub metadata file
```

- **Frontend**: Single HTML file (~75 KB) — no build tools, no dependencies
- **Backend**: Lightweight Python HTTP server with in-memory caching (300s TTL) and retry logic (3 attempts, exponential backoff)

## 🎯 How to Play

1. **Search** for an artist (or multiple for a playlist)
2. **Configure** game mode and options
3. **Listen** to the 30-second Deezer preview
4. **Answer** — points are awarded based on mode and speed
5. **Review** wrong answers and track your progress

## 🛠️ Tech Stack

- **Frontend**: Vanilla JavaScript, CSS (with custom properties), HTML
- **Backend**: Python 3 (`http.server` module)
- **API**: [Deezer API](https://developers.deezer.com/api) (free, no key required)
- **Storage**: `localStorage` (settings, statistics, achievements)
- **Audio**: Web Audio API (sound effects), CSS visualizer (audio animations)

## 📝 License

MIT

---

*Powered by Deezer — this project is not affiliated with or endorsed by Deezer.*
