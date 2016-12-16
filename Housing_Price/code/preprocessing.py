import pandas as pd

path2data = "../data/"
train_file = "train.csv"
test_file = "test.csv"

train = pd.read_csv(path2data + train_file)

print train.count()
