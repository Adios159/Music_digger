def generate_playlist(mood, genre, era, tempo):
    # 더미 데이터베이스 (나중에 DB 대체)
    songs = [
        {"title": "비처럼 음악처럼", "artist": "김현식", "year": "1986", "genre": "발라드", "tempo": "느림", "mood": "슬픔"},
        {"title": "나는 나비", "artist": "YB", "year": "2005", "genre": "록", "tempo": "중간", "mood": "희망"},
        {"title": "Dynamite", "artist": "BTS", "year": "2020", "genre": "팝", "tempo": "빠름", "mood": "기쁨"},
        {"title": "너의 의미", "artist": "아이유", "year": "2014", "genre": "발라드", "tempo": "느림", "mood": "평온"},
        {"title": "거짓말", "artist": "BIGBANG", "year": "2007", "genre": "힙합", "tempo": "빠름", "mood": "분노"},
    ]

    # 필터링
    filtered = []
    for song in songs:
        if (
            song["genre"] == genre
            and song["tempo"] == tempo
            and song["mood"] == mood
            and era[:3] in song["year"]  # 예: "2000s" → "200"
        ):
            filtered.append(song)

    # 결과가 없으면 비슷한 템포 곡이라도 줌 (예시용)
    if not filtered:
        filtered = [s for s in songs if s["tempo"] == tempo]

    return filtered[:15]  # 최대 15곡
