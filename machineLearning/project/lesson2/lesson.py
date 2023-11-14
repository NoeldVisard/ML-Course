import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

import numpy as np
import matplotlib as mpl

# data = pd.read_csv('train.csv')
# data2 = pd.read_csv('pima-indians-diabetes.csv')
# dataset = pd.read_csv('Sunspots.csv')

def dataset(filename):
    data = pd.read_csv(filename)
    return data['Date'], data[data.columns[-1]]

# Скользящая средняя
def rolling_mean(y):
    n = 25
    result = y.rolling(window=n).mean()
    plt.plot(result, color='r')

def exponential(y):
    alpha = 0.5
    result = [y[0]]
    for i in range(1, len(y)):
        result.append(alpha*y[i]+(1-alpha)*result[i-1])
    plt.plot(result, color='g')

def draw(x, y):
    plt.figure(figsize=(60, 30))
    # plt.plot(x, y) # Ломаная
    plt.scatter(x, y) # Отдельные точки
    # plt.xlim(10, 10) # Обрезать график
    rolling_mean(y)
    exponential(y)
    plt.show()

date, sunspots = dataset('Sunspots.csv')
draw(date, sunspots)

