import pandas as pd
import math
import numpy as np
np.set_printoptions(suppress=True)

for year in range(2001,2002):
    teams_path = "data/team/TeamPerGame{}.csv".format(year)
    games_path = "data/games/Games{}.csv".format(year)
    teams_df = pd.read_csv(teams_path, index_col=0)
    games_df = pd.read_csv(games_path, index_col=0)
    games_arr = games_df.to_numpy()

    stats_arr=None
    for game in games_arr:
        t1 = game[1]
        t2 = game[2]
        t1_stats = teams_df.loc[t1].to_numpy()[:-1]
        t2_stats = teams_df.loc[t2].to_numpy()[:-1]
        comb_arr = np.append(t1_stats, t2_stats)
        
        if isinstance(stats_arr, (np.ndarray, np.generic) ):
            stats_arr = np.vstack([stats_arr, comb_arr])
        else:
            stats_arr = comb_arr
        

    print(stats_arr.shape)
    df = pd.DataFrame(stats_arr, columns=[list(teams_df.columns[:-1]) + list(teams_df.columns[:-1])])
    print(df)
    # print(games_arr)
    # new_arr = np.concatenate((games_arr, stats_arr), axis = 1)
    # print(new_arr)
    

    # print(new_arr)