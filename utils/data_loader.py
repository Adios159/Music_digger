import pandas as pd

def load_song_data(csv_path='data/sample_songs.csv'):
    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"[ERROR] 음악 데이터를 불러오는데 실패했습니다: {e}")
        return pd.DataFrame()