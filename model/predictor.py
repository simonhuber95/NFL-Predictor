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
    offense = pd.read_csv('data/offense/OffensePerGame2021csv')
    defense = pd.read_csv('data/defense/DefensePerGame2021csv')
    return True



games = grep_games(2)
print(games)
# model = keras.models.load_model('model/nfl_predictor_model')

# predict_on_data = 

# games = pd.read_csv("data/combined_games.csv").to_numpy()
# predictions = model.predict_on_batch(predict_on_data)