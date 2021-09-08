import keras
import pandas as pd
import numpy as np
from keras import Sequential
np.set_printoptions(suppress=True)

def load_data():
  data_path = "data/full_data.csv"
  labels_path = "data/combined_games.csv"
  data = pd.read_csv(data_path, index_col=0).to_numpy()
  labels = pd.read_csv(labels_path)
  labels = labels[['Team1Win', 'Team2Win']].to_numpy()
  return data, labels

amount_games = 100
data, labels = load_data()
model = keras.models.load_model('model/nfl_predictor_model')

predict_on_data = data[-amount_games:]
games = pd.read_csv("data/combined_games.csv").to_numpy()
predictions = model.predict_on_batch(predict_on_data)

score = 0
for idx, pred in enumerate(predictions):
    game = games[-(amount_games-idx)]
    result = '✖'
    if round(pred[0], 0) == game[4]:
        score += 1
        result = '✔'
    print(game[2], 'at', game[3])
    print('Outcome: {} {} | Prediction: {}% {}% {}'.format(game[4], game[5], round(pred[0]*100), round(pred[1]*100), result))
    print('-------------------------------------')
    
print('Score: ', score, '/', amount_games)
