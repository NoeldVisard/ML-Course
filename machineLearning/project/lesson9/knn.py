import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn import datasets

from collections import Counter

import warnings
warnings.filterwarnings("ignore")

iris = datasets.load_iris()
iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                       columns=iris['feature_names'] + ['target'])



def get_euclidean_distance(x_train, x_test_point):
    """
    Метод высчитывает расстояние от тестовой точки до каждой точки в тестовом наборе
    :param x_train:
    :param x_test_point:
    :return:
    """
    distances = []
    # рассчитываю расстояния до каждой точки в наборе обучающих данных
    for row in range(len(x_train)):
        current_train_point = x_train[row]
        # current_distance - среднеквадратическое отклонение
        current_distance = 0

        for col in range(len(current_train_point)):
            current_distance += (current_train_point[col] - x_test_point[col]) ** 2
        current_distance = np.sqrt(current_distance)
        distances.append(current_distance)

    distances = pd.DataFrame(data=distances, columns=['dist'])
    return distances


def get_nearest_neighbors(distance_point, k):
    """
    Метод находит k ближайших соседей для каждой тестовой точки
    :param distance_point:
    :param k:
    :return:
    """
    knearests = distance_point.sort_values(by=['dist'], axis=0)

    knearests = knearests[:k]
    return knearests


def get_most_common(k_nearest, y_train):
    """
    Метод определяет наиболее часто встречающийся класс среди ближайших соседей
    :param k_nearest:
    :param y_train:
    :return:
    """
    common_types = Counter(y_train[k_nearest.index])
    prediction = common_types.most_common()[0][0]
    return prediction


def class_predict_by_knn(x_train, y_train, x_test, k):
    """
    Метод предсказывает класс для каждой тестовой точки на основе ближайших соседей
    :param x_train:
    :param y_train:
    :param x_test:
    :param k:
    :return:
    """
    prediction = []

    for x_test_point in x_test:
        distance_point = get_euclidean_distance(x_train, x_test_point)
        nearest_point = get_nearest_neighbors(distance_point, k)
        pred_point = get_most_common(nearest_point, y_train)
        prediction.append(pred_point)

    return prediction


def calculate_accuracy(y_test, y_pred):
    """
    Метод подсчитывает точность
    :param y_test:
    :param y_pred:
    :return:
    """
    correct_count = 0
    for i in range(len(y_test)):
        if y_test[i] == y_pred[i]:
            correct_count = correct_count + 1
    accuracy = correct_count / len(y_test)
    return accuracy


x = iris_df.iloc[:, :-1]
y = iris_df.iloc[:, -1]

x_train = x.sample(frac=0.8, random_state=0)
y_train = y.sample(frac=0.8, random_state=0)
x_test = x.drop(x_train.index)
y_test = y.drop(y_train.index)

x_train = np.asarray(x_train)
y_train = np.asarray(y_train)

x_test = np.asarray(x_test)
y_test = np.asarray(y_test)

current_palette = sns.color_palette()
print('x train до нормализации')
print(x_train[0:5])
di = {0.0: 'Setosa', 1.0: 'Versicolor', 2.0: 'Virginica'}

before = sns.pairplot(iris_df.replace({'target': di}), hue='target', corner=True, diag_kind=None)
before.fig.suptitle('До нормализации', y=1.08)

x_train_min = x_train.min(axis=0)
x_train_max = x_train.max(axis=0)
normalized_x_train = (x_train - x_train_min) / (x_train_max - x_train_min)

x_test_min = x_test.min(axis=0)
x_test_max = x_test.max(axis=0)
normalized_x_test = (x_test - x_test_min) / (x_test_max - x_test_min)


print('x train после нормализации')
print(normalized_x_train[0:5])

iris_df_2 = pd.DataFrame(data=np.c_[normalized_x_train, y_train],
                         columns=iris['feature_names'] + ['target'])
di = {0.0: 'Setosa', 1.0: 'Versicolor', 2.0: 'Virginica'}
after = sns.pairplot(iris_df_2.replace({'target': di}), hue='target', corner=True, diag_kind=None)
after.fig.suptitle('После нормализации', y=1.08)

accuracies = []
ks = range(1, 30)
for k in ks:
    y_pred = class_predict_by_knn(normalized_x_train, y_train, normalized_x_test, k)
    accuracy = calculate_accuracy(y_test, y_pred)
    accuracies.append(accuracy)
plt.show()

# testSet = [[5.1, 3.5, 1.4, 0.2]] # - setosa
testSet = [[6.7, 3.0, 5.2, 2.3]] #virginica
test = pd.DataFrame(testSet)
test = np.asarray(test)
test_min = test.min(axis=0)
test_max = test.max(axis=0)
test_array = (test - test_min) / (test_max - test_min)

di = {0.0: 'Setosa', 1.0: 'Versicolor', 2.0: 'Virginica'}
max_value = max(accuracies)
k = accuracies.index(max_value) + 1
predictions = class_predict_by_knn(normalized_x_train, y_train, test_array, k)
for i in predictions:
    print(di[i])