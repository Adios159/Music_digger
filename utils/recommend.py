# utils/recommend.py

def generate_playlist(mood, genre, era, tempo):
    playlist = []

    for i in range(15):
        song = {
            "title": f"{genre} Song {i+1}",
            "artist": f"Artist {i+1}",
            "year": era,
            "genre": genre,
            "tempo": tempo
        }
        playlist.append(song)

    return playlist
