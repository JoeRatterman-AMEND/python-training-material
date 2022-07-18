# Load packages
import pandas as pd
import pickle
import autosklearn.classification
import sklearn
import numpy as np


# Load dataset
df = pd.read_csv('C:/Users/JoeRatterman/Documents/GitHub/training-material/prediction_win_df.csv')
df = df.drop("Unnamed: 0", axis=1)
df = df.dropna()
df["win"] = df["win"].astype(str)
df.head()


# Split dataset
X_train = df.drop("win", axis=1)
y_train = df[["win"]]


# Load model
with open('home/JoeRatterman/Documents/GitHub/training-material/ncaab-model-1.pickle', 'rb') as f:
    loaded_classifier = pickle.load(f)


# Lake predictions
y_pred = loaded_classifier.predict(X_train)

df = pd.DataFrame(y_pred)

df.to_csv('home/JoeRatterman/Documents/GitHub/training-material/sample_output_2021-09-30.csv')

