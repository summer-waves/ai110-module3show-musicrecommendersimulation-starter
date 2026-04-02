import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class Song:
    """Represents a song and its attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represents a user's taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """OOP implementation of the recommendation logic."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns top k songs scored against the user profile."""
        scored = []
        for song in self.songs:
            score, _ = self._score(user, song)
            scored.append((song, score))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable explanation for why a song was recommended."""
        _, reasons = self._score(user, song)
        return " | ".join(reasons)

    def _score(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        """Scores a single song against user preferences."""
        score = 0.0
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
            reasons.append("genre match (+2.0)")

        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
            reasons.append("mood match (+1.0)")

        energy_similarity = 1.0 - abs(user.target_energy - song.energy)
        score += energy_similarity * 1.5
        reasons.append(f"energy similarity (+{energy_similarity * 1.5:.2f})")

        if user.likes_acoustic and song.acousticness > 0.5:
            score += 0.5
            reasons.append("acoustic match (+0.5)")

        return score, reasons


def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns a list of dictionaries."""
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    print(f"Loaded songs: {len(songs)}")
    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song dict against user preference dict."""
    score = 0.0
    reasons = []

    if song['genre'].lower() == user_prefs['favorite_genre'].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song['mood'].lower() == user_prefs['favorite_mood'].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_similarity = 1.0 - abs(user_prefs['target_energy'] - song['energy'])
    score += energy_similarity * 1.5
    reasons.append(f"energy similarity (+{energy_similarity * 1.5:.2f})")

    if user_prefs.get('likes_acoustic') and song['acousticness'] > 0.5:
        score += 0.5
        reasons.append("acoustic match (+0.5)")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Returns top k recommended songs with scores and explanations."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " | ".join(reasons)
        scored.append((song, score, explanation))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]