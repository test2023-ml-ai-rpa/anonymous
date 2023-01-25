import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('headbrain.csv')
print("Dimensions:", data.shape)
print("First 5 rows:", data.head())

X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

mean_x = np.mean(X)
mean_y = np.mean(Y)

n = len(X)

numer = 0
denom = 0
for i in range(n):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
m = numer / denom
c = mean_y - (m * mean_x)
print("Coefficients")
print(m, c)
