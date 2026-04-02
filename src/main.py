"""
Command line runner for the Music Recommender Simulation.
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    # --- User Profiles ---

    print("\n=== Profile 1: Happy Pop Fan ===")
    user1 = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False
    }
    for song, score, explanation in recommend_songs(user1, songs, k=5):
        print(f"  {song['title']} by {song['artist']} | Score: {score:.2f}")
        print(f"  Because: {explanation}\n")

    print("\n=== Profile 2: Chill Acoustic Listener ===")
    user2 = {
        "favorite_genre": "acoustic",
        "favorite_mood": "chill",
        "target_energy": 0.2,
        "likes_acoustic": True
    }
    for song, score, explanation in recommend_songs(user2, songs, k=5):
        print(f"  {song['title']} by {song['artist']} | Score: {score:.2f}")
        print(f"  Because: {explanation}\n")

    print("\n=== Profile 3: High Energy Rock Fan ===")
    user3 = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.95,
        "likes_acoustic": False
    }
    for song, score, explanation in recommend_songs(user3, songs, k=5):
        print(f"  {song['title']} by {song['artist']} | Score: {score:.2f}")
        print(f"  Because: {explanation}\n")


if __name__ == "__main__":
    main()