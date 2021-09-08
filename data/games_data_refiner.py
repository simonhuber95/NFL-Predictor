import pandas as pd
import math

columns = ['Week','Day','Date','Time','Team1','Home','Team2','Boxscore', 'PtsW','PtsL','YdsW','TOW','YdsL','TOL']

def refine_games(year):
    game_path = "data\games_raw\Games{}.csv".format(year)
    df = pd.read_csv(game_path, skiprows=1, names = columns, engine = 'python')
    df = df.drop(['Boxscore', 'Day', 'Date', 'Time', 'Boxscore', 'PtsW','PtsL','YdsW','TOW','YdsL','TOL'], axis = 1)

    # Check if Winner is also home team by checking for NaN
    m = df['Home'] != df['Home']
    # Swap Teams if Winner is Home
    df.loc[m, ['Team1', 'Team2']] = (df.loc[m, ['Team2', 'Team1']].values)
    # Drop the Home Column
    df = df.drop('Home', axis = 1)
    #Convert Booleans into ints
    df['Team1Win'] = (~m).astype(int)
    df['Team2Win'] = m.astype(int)
    print(df)

    return df


for year in range(2001,2021):
    path = "data/games_raw/Games{}.csv".format(year)
    df = refine_games(year)
    df.to_csv(path)