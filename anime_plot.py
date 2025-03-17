import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from anime_analysis import anime, rating, calculate_wathing_time



if __name__ == "__main__":
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)

    anime['watch_time'] = anime['episodes'].apply(calculate_wathing_time)

    anime_list = anime['type'].unique().tolist() # ['Movie' 'TV' 'OVA' 'Special' 'Music' 'ONA' nan]

    anime_graph = pd.DataFrame()

    for anime_type in anime_list:
        df = anime[anime['type'] == anime_type][['type', 'watch_time']]
        anime_graph = pd.concat([anime_graph, df], ignore_index=True)

    print(anime_graph.dtypes)
    print(f'---------------')

    anime_graph['watch_time_minutes'] = anime_graph['watch_time'].dt.total_seconds() / 60

    anime_watch_time_sum = []
    for anime_type in anime_list:
        anime_watch_time_sum.append(anime_graph[anime_graph['type'] == anime_type]['watch_time_minutes'].sum())

    print(anime_watch_time_sum)

    anime_watch_time_sum = [float(i) for i in anime_watch_time_sum]

    print(anime_list[:-1])
    print(anime_watch_time_sum)

    plt.bar(anime_list[:-1], anime_watch_time_sum[:-1], color='blue')
    plt.xlabel('Anime type')
    plt.ylabel('Watch time')
    plt.title('The most views Anime type')

    plt.show()



