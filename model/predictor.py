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
    games = pd.read_csv('data/games-raw/Games2021.csv')
    games_week = games.loc[games['week'] == week]
    return games_week


def grep_stats():
    return True



data, labels = load_data()
model = keras.models.load_model('model/nfl_predictor_model')

predict_on_data = 

games = pd.read_csv("data/combined_games.csv").to_numpy()
predictions = model.predict_on_batch(predict_on_data)