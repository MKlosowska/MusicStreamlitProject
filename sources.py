import requests
from decorators import timer

class Track:
    def __init__(self, track, artist, album=None, genre=None, release_date=None, duration_ms=None):
        self.track = track
        self.artist = artist
        self.album = album
        self.genre = genre
        self.release_date = release_date
        self.duration_ms = duration_ms

class ITunesSource:
    @timer
    def fetch(self, query, country="PL", limit=100, attribute=None):
        url = "https://itunes.apple.com/search"
        params = {"term": query, "entity": "song", "country": country, "limit": int(limit)}
        if attribute:
            params["attribute"] = attribute

        r = requests.get(url, params=params, timeout=20)
        r.raise_for_status()
        data = r.json()

        tracks = []
        for item in data.get("results", []):
            tracks.append(Track(
                track=item.get("trackName") or "",
                artist=item.get("artistName") or "",
                album=item.get("collectionName"),
                genre=item.get("primaryGenreName"),
                release_date=item.get("releaseDate"),
                duration_ms=item.get("trackTimeMillis"),
            ))
        return tracks
