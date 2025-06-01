# app/routes.py
from flask import Blueprint, render_template, request
from utils.data_loader import load_song_data
import random
from utils.data_loader import load_song_data


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/playlist', methods=['POST'])
def playlist():
    mood = request.form['mood']
    genre = request.form['genre']
    era = request.form['era']
    tempo = request.form['tempo']

    # 🔽 여기부터 새로 작성한 코드 🔽
    df = load_song_data()

    # 필터링 조건
    filtered = df[
        (df['mood'] == mood) &
        (df['genre'] == genre) &
        (df['era'] == era) &
        (df['tempo'] == tempo)
    ]

    # 조건이 너무 빡세면 일부 완화
    if len(filtered) < 15:
        filtered = df[
            (df['genre'] == genre) &
            (df['era'] == era)
        ]

    # 15~20곡 무작위 추출
    playlist = filtered.sample(n=min(20, len(filtered))).to_dict(orient='records')

    return render_template(
        'playlist.html',
        mood=mood,
        genre=genre,
        era=era,
        tempo=tempo,
        playlist=playlist
    )
