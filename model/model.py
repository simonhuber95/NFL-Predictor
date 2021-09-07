import keras
import pandas as pd


data_path = "data/team/TeamPerGame{}.csv".format(2020)
df = pd.read_csv(data_path)
df = df.drop(['Team','Year'], axis = 1)
input_shape = len(df.columns)*2 + 2 
print(df.columns, input_shape)
