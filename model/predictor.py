import keras
import pandas as pd
import numpy as np

def load_data():
  data_path = "data/full_data.csv"
  labels_path = "data/combined_games.csv"
  data = pd.read_csv(data_path, index_col=0).to_numpy()
  labels = pd.read_csv(labels_path)
  labels = labels[['Team1Win', 'Team2Win']].to_numpy()
  return data, labels

def grep_games(week):
    games = pd.read_csv('data/games_raw/Games2021.csv')
    games_week = games.loc[games['Week'] == week]
    return games_week[['Week', 'Guest', 'Home']]


def grep_stats():
    team_stats = pd.read_csv('data/team/TeamPerGame2021.csv', index_col=0)
    return team_stats.drop(columns = ['Year'])



games = grep_games(2)
team_stats = grep_stats()
model = keras.models.load_model('model/nfl_predictor_model')


for idx, game in games.iterrows():
    guest_stats = team_stats.loc[team_stats.index == game['Guest']].to_numpy()
    home_stats = team_stats.loc[team_stats.index == game['Home']].to_numpy()

    print(game['Guest'], '@', game['Home'])
    predict_on_data = np.append(guest_stats, home_stats)
    prediction = model.predict_on_batch(np.array([predict_on_data,]))[0]
    # print(predict_on_data)
    print('Prediction: {}% {}%'.format(round(prediction[0]*100), round(prediction[1]*100)))
    print('------------------------------------------')