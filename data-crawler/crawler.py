import pandas as pd
from pandas.io.json import json_normalize
import requests
from bs4 import BeautifulSoup
import json

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


url = "https://www.pro-football-reference.com/years/2020/#team_stats"
res = requests.get(url, verify=False)
soup = BeautifulSoup(res.content, 'html.parser')

soup = soup.find_all(id="team_stats")
print(len(soup), type(soup))
print(soup)
soup = soup[0].find_all('table')
print(len(soup))
# print(soup.prettify())
# table = soup.find('table')
# print(table)
# df = pd.read_html(str(soup))[0]
# print(df)
# playerstats = load_data("offense", 2020)
# print(playerstats)
