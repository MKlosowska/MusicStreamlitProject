from analysis import to_df, filter_by_artist, kpi, newest_tracks, top_genres
from sources import Track
import pandas as pd

def run_tests():
    # Przykładowe utwory
    tracks = [
        Track(track="Utwór A", artist="Artysta1", album="Album1", genre="Rock", release_date="2024-01-01", duration_ms=180000),
        Track(track="Utwór B", artist="Artysta1", album="Album1", genre="Pop", release_date="2023-05-10", duration_ms=210000),
        Track(track="Utwór C", artist="Artysta2", album="Album2", genre="Rock", release_date="2024-06-20", duration_ms=200000),
    ]

    df = to_df(tracks)

    # Test 1: filter_by_artist
    df_artist = filter_by_artist(df, "Artysta1")
    assert len(df_artist) == 2, "Błąd: filter_by_artist"

    # Test 2: kpi (podstawowe statystyki)
    metrics = kpi(df)
    assert metrics["utwory"] == 3, "Błąd: kpi - liczba utworów"
    assert metrics["albumy"] == 2, "Błąd: kpi - liczba albumów"
    assert metrics["gatunki"] == 2, "Błąd: kpi - liczba gatunków"

    # Test 3: newest_tracks
    newest = newest_tracks(df, n=2)
    assert newest.iloc[0]["track"] == "Utwór C", "Błąd: newest_tracks - pierwszy najnowszy"
    assert newest.iloc[1]["track"] == "Utwór A", "Błąd: newest_tracks - drugi najnowszy"

    # Test 4: top_genres
    top = top_genres(df)
    assert "Rock" in top["genre"].values, "Błąd: top_genres - brak Rock"
    assert "Pop" in top["genre"].values, "Błąd: top_genres - brak Pop"

    print("Wszystkie testy poprawne!")

if __name__ == "__main__":
    run_tests()
