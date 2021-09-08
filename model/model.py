import keras
import pandas as pd
from keras.layers import Dense, Dropout, BatchNormalization
from keras import Sequential
from keras.losses import sparse_categorical_crossentropy
from keras.optimizers import Adam
from sklearn.model_selection import KFold
import numpy as np
np.set_printoptions(suppress=True)




# Model configuration
batch_size = 32
no_epochs = 25 
verbosity = 1
num_folds = 10
input_shape = (96,)

def load_data():
  data_path = "data/full_data.csv"
  labels_path = "data/combined_games.csv"
  data = pd.read_csv(data_path, index_col=0).to_numpy()
  labels = pd.read_csv(labels_path)
  labels = labels[['Team1Win', 'Team2Win']].to_numpy()
  return data, labels


def define_model(input_shape, layers = [], dropout = True):
  model = Sequential()
  model.add(BatchNormalization(input_shape = input_shape))
  for neurons in layers:
      model.add(Dense(neurons, activation="relu"))
      # model.add(BatchNormalization())
      if dropout:
          model.add(Dropout(0.5))

  model.add(Dense(2, activation='softmax'))
  # Compile model
  model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
  return model

# Define per-fold score containers
acc_per_fold = []
loss_per_fold = []

# Load data
data, labels = load_data()

# Define the K-fold Cross Validator
kfold = KFold(n_splits=num_folds, shuffle=True)

# K-fold Cross Validation model evaluation
fold_no = 1
for train, test in kfold.split(data, labels):

  model = define_model(input_shape=(96,), layers=[1024, 1024, 256, 32], dropout=True)

  # Generate a print
  print('------------------------------------------------------------------------')
  print(f'Training for fold {fold_no} ...')

  # Fit data to model
  history = model.fit(data[train], labels[train],
              batch_size=batch_size,
              epochs=no_epochs,
              verbose=verbosity)

  # Generate generalization metrics
  scores = model.evaluate(data[test], labels[test], verbose=0)
  print(f'Score for fold {fold_no}: {model.metrics_names[0]} of {scores[0]}; {model.metrics_names[1]} of {scores[1]*100}%')
  acc_per_fold.append(scores[1] * 100)
  loss_per_fold.append(scores[0])

  # Increase fold number
  fold_no = fold_no + 1

# == Provide average scores ==
print('------------------------------------------------------------------------')
print('Score per fold')
for i in range(0, len(acc_per_fold)):
  print('------------------------------------------------------------------------')
  print(f'> Fold {i+1} - Loss: {loss_per_fold[i]} - Accuracy: {acc_per_fold[i]}%')
print('------------------------------------------------------------------------')
print('Average scores for all folds:')
print(f'> Accuracy: {np.mean(acc_per_fold)} (+- {np.std(acc_per_fold)})')
print(f'> Loss: {np.mean(loss_per_fold)}')
print('------------------------------------------------------------------------')

# model.save('nfl_predictor_model')

