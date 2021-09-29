import pandas as pd


columns = ['Rk', 'Team', 'Games', 'Points', 'Yds', 'Playes', 'Y/P', 'Turnovers', 'Fumbles', '1stD', 'PassCmp',
       'PassAtt', 'PassYds', 'PassTD', 'PassInt', 'PassNY/A', 'Pass1stD', 'RushAtt', 'RushYds', 'RushTD',
       'RushY/A', 'Rush1stD', 'Penalties', 'PenYds', '1stPy', 'Sc%', 'Turnover%', 'EXP']

off_columns =  list(map(lambda x: 'Off' + x if x not in ['Team', 'Games', 'Rk', 'EXP'] else x, columns))
def_columns =  list(map(lambda x: 'Def' + x if x not in ['Team', 'Games', 'Rk', 'EXP'] else x, columns))

def combine_stats(year):
    def_path = "data\defense\DefensePerGame{}.csv".format(year)
    off_path = "data\offense\OffensePerGame{}.csv".format(year)
    def_df = pd.read_csv(def_path, skiprows=2, skipfooter=3, names = def_columns, engine = 'python', index_col = 'Team')
    def_df = def_df.drop(['Games', 'Rk', 'EXP'], axis = 1)

    off_df = pd.read_csv(off_path, skiprows=2, skipfooter=3, names = off_columns, engine = 'python', index_col = 'Team')
    off_df = off_df.drop(['Games','Rk', 'EXP'], axis = 1)

    team_df = pd.concat([off_df, def_df], axis=1)
    team_df['Year'] = year
    print(team_df)
    return team_df

for year in range(2021,2022):
    path = "data/team/TeamPerGame{}.csv".format(year)
    team_df = combine_stats(year)
    team_df.to_csv(path)