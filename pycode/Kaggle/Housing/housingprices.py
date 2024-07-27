import pandas as pd
from sklearn import model_selection

train = pd.read_csv("train.csv")
# pred = pd.read_csv("test.csv")

train, test = model_selection.train_test_split(0.3, )