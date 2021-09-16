import keras
import pandas as pd
import numpy as np
from collections import Counter

from tensorflow.python.keras.saving.save import load_model
np.set_printoptions(suppress=True)

def load_data():
  data_path = "data/full_data.csv"
  labels_path = "data/combined_games.csv"
  data = pd.read_csv(data_path, index_col=0).to_numpy()
  labels = pd.read_csv(labels_path)
  labels = labels[['Team1Win', 'Team2Win']].to_numpy()
  return data, labels

amount_games = 255

data, labels = load_data()
model = keras.models.load_model('model/nfl_predictor_model')
# rndm_choice = random.choices(range(len(labels)), k = amount_games)
predict_on_data = data[-amount_games:]

games = pd.read_csv("data/combined_games.csv").to_numpy()
predictions = model.predict_on_batch(predict_on_data)

win_fails =[] # Team was predicted to lose but won
los_fails =[] # Team was predicted to win bot lost
tot_fails = []
score = 0
for idx, pred in enumerate(predictions):
    game = games[-(amount_games-idx)]
    
    if round(pred[0], 0) == game[4]:
        score += 1
        result = '✔'
    else:
        result = '✖'
        tot_fails.append(game[2])
        tot_fails.append(game[3])
        if round(pred[0]) == 0:
            win_fails.append(game[2])
            los_fails.append(game[3])
        else:
            win_fails.append(game[3])
            los_fails.append(game[2])

    print(game[2], 'at', game[3])
    print('Outcome: {} {} | Prediction: {}% {}% {}'.format(game[4], game[5], round(pred[0]*100), round(pred[1]*100), result))
    print('-------------------------------------')
    
print('Score: ', score, '/', amount_games)
win_fails = dict((x,win_fails.count(x)) for x in set(win_fails))
los_fails = dict((x,los_fails.count(x)) for x in set(los_fails))
tot_fails = dict((x,tot_fails.count(x)) for x in set(tot_fails))

print('Team was predicted to lose but won')
print(sorted(win_fails.items(), key=lambda x: x[1], reverse=True))
print('Team was predicted to win but lost')
print(sorted(los_fails.items(), key=lambda x: x[1], reverse=True))
print('Total')
print(sorted(tot_fails.items(), key=lambda x: x[1], reverse=True))

