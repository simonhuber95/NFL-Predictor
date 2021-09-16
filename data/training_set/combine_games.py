import pandas as pd
import math
import numpy as np
np.set_printoptions(suppress=True)


list_of_games = []
for year in range(2001,2021):
    path = "data/games/Games{}.csv".format(year)
    df=pd.read_csv(path, index_col=0)
    list_of_games.append(df)


result = pd.concat(list_of_games)
print(result.shape)
print(result)
result.to_csv('data/combined_games.csv')