# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a content-based music recommender system. It loads a catalog of songs from a CSV file, compares each song against a user's taste profile, and returns a ranked list of personalized recommendations with explanations. The system scores songs based on genre, mood, energy similarity, and acousticness preference — no user behavior data is needed, just the song's attributes and the user's stated preferences.

---

## How The System Works

Each `Song` in the system has these features:
- `genre` — musical category (pop, rock, lofi, etc.)
- `mood` — emotional tone (happy, chill, intense, etc.)
- `energy` — a 0.0–1.0 scale of how energetic the track feels
- `acousticness` — a 0.0–1.0 scale of how acoustic (vs. electronic) it sounds
- `tempo_bpm`, `valence`, `danceability` — additional numerical attributes

Each `UserProfile` stores:
- `favorite_genre` — the genre they prefer most
- `favorite_mood` — the mood they're looking for
- `target_energy` — their ideal energy level (0.0–1.0)
- `likes_acoustic` — whether they prefer acoustic tracks

**Scoring recipe:**
- Genre match → +2.0 points
- Mood match → +1.0 point
- Energy similarity → up to +1.5 points (calculated as `(1 - |user_energy - song_energy|) × 1.5`)
- Acoustic match (if user prefers acoustic and song acousticness > 0.5) → +0.5 points

Songs are ranked from highest to lowest score and the top k are returned with explanations.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):
```bash
python -m venv .venv
source .venv/bin/activate      # Mac or Linux
.venv\Scripts\activate         # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python3 -m src.main
```

### Running Tests
```bash
pytest
```

---

## Experiments You Tried

- **Profile 1 (Happy Pop Fan, energy 0.8):** "Sunrise City" ranked first with a 4.47 score — it matched genre, mood, and had close energy. "Gym Hero" ranked second at 3.30 with a genre match but no mood match.
- **Profile 2 (Chill Acoustic Listener, energy 0.2):** No songs matched the "acoustic" genre exactly, so mood and acousticness carried the rankings. "Spacewalk Thoughts" topped the list at 2.88.
- **Profile 3 (High Energy Rock Fan, energy 0.95):** "Storm Runner" ranked first at 4.44 due to genre match and high energy — but no rock songs matched the intense mood, showing a gap in the dataset.

---

## Limitations and Risks

- The catalog only has 10 songs, so results repeat across very different profiles.
- The system has no "acoustic" genre songs, so the Chill Acoustic profile never gets a genre match.
- Genre is weighted highest (+2.0), which can dominate results even when mood and energy are a better fit.
- The system cannot learn or adapt — it only uses what the user explicitly tells it.

---

## Reflection

Building this recommender made it clear how much a simple scoring rule shapes what a user sees. A genre weight of 2.0 means the system will almost always favor songs from the preferred genre, even if a song from a different genre fits the mood and energy much better. This is exactly how filter bubbles form in real platforms — the algorithm keeps reinforcing one dimension of taste. Real systems like Spotify use collaborative filtering on top of content features, which introduces its own biases by pushing users toward whatever is already popular with similar listeners. Human judgment still matters when deciding what to weight, what features to include, and who the system is actually being built for.

---

## Model Card

See [model_card.md](model_card.md) for full documentation of the system's intended use, limitations, and future improvements.