# import pandas as pd
# from pandas.io.json import json_normalize
# import requests
import os
# import json

# Games
# https://www.pro-football-reference.com/years/2020/games.htm#games
#
years = list(range(1990,2021))
weeks = list(range(1,17))
data_sources = {"defense": "https://www.pro-football-reference.com/years/<year>/opp.htm#team_stats",
                "game": "https://www.pro-football-reference.com/years/<year>/games.htm#games",
                "offense": "https://www.pro-football-reference.com/years/<year>/#team_stats",
                "rushing": "https://www.pro-football-reference.com/years/2020/#rushing"
}

def load_data(type, year):
    url = data_sources.get(type)
    url = url.replace("<year>", str(year))
    print(url)
    html = pd.read_html(url, header = 0, match= "Team Offense Table")
    print(html)
    df = html[0]
    # raw = df.drop(df[df.Age == 'Age'].index) # Deletes repeating headers in content
    # raw = raw.fillna(0)
    # playerstats = raw.drop(['Rk'], axis=1)
    #return playerstats
    return df
par = "C:/Users/HUBERS/OneDrive - FUJITSU/Projects/NFL-Predictor/data/games/"

for i in range(2001,2019):
    file = "Games{}.csv".format(i)
    filename = os.path.join(par,file)
    f = open(filename, "w")
