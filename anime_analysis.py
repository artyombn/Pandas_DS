import pandas as pd
import numpy as np

from pathlib import Path
from datetime import timedelta


BASE_DIR = Path(__file__).resolve().parent
ANIME_DIR = BASE_DIR / "anime-recommendations-database"


anime = pd.read_csv(ANIME_DIR / "anime.csv")
rating = pd.read_csv(ANIME_DIR / "rating.csv")

anime_modified = anime.set_index('name')

anime_copy = anime.copy(deep=True)


def calculate_wathing_time(value):
    # 1 episod ~ 40 min
    try:
        time = int(value) * 40
        return timedelta(minutes=time)
    except ValueError:
        return None

def qualitative(value):
    if value <= 5:
        return False
    else:
        return True


if __name__ == "__main__":
    print(anime_copy)

    rating[:10].to_csv(ANIME_DIR / 'saved_ratings.csv', index=False)

    print(anime.head(3))
    print(rating.tail(2))
    print(f"----------")

    print(len(rating['user_id'].unique()))
    print(rating['user_id'].value_counts())

    print(anime.info())
    print(anime.describe())
    print(f"----------")

    anime_list = anime['genre'].tolist()
    print(anime_list[:10])

    print(anime_modified.index.tolist()[:10])
    print(anime.columns.tolist())

    anime['quality'] = anime['rating'].apply(qualitative)

    print(anime[['name', 'rating', 'quality']])
    print(anime['rating'].mean()) # 6.473901690981432
    print(anime['rating'].median()) # 6.57
    print(f"----------")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)

    print(anime.head(5))

    print(f"----------")
    pd.reset_option("display.max_columns")
    pd.reset_option("display.expand_frame_repr")


    print(anime.head(5))
    print(anime['episodes'].unique())

    anime['watch_time'] = anime['episodes'].apply(calculate_wathing_time)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)

    print(anime.loc[anime["watch_time"] == timedelta(minutes=40)])
    print(anime.loc[anime["watch_time"] == "Uncertain"])
    print(anime[anime['watch_time'].isin([timedelta(minutes=40), timedelta(minutes=80)])])
    print(anime[(anime['type'] == 'TV') & (anime['watch_time'] == timedelta(minutes=80))])


    anime_copy = anime_copy.drop(['type', 'genre', 'members', 'episodes'], axis=1)
    print(f'--------------')
    print(anime_copy.head(5))
    print(f'--------------')
    print(anime.sample(frac=0.25))
    print(f'--------------')


    for idx, row in anime[:2].iterrows():
        print(idx, row)





