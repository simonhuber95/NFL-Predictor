import keras
import pandas as pd
from keras.layers import Dense, Dropout
from keras import Sequential

data_path = "data/team/TeamPerGame{}.csv".format(2020)
df = pd.read_csv(data_path)
df = df.drop(['Team','Year'], axis = 1)
input_shape = len(df.columns)*2 + 2 
print(df.columns, input_shape)


define_model(input_shape, layers = [], dropout = True):

    model = Sequential
    model.add(BatchNormalization(input_shape=input_shape))
    for neurons in layers:
        model.add(Dense(neurons, activation="relu"))
        if dropout:
            model.add(Dropout(0.5))