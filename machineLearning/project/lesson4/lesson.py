# from sklearn.datasets import make_blobs
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def generate_points(points_amount=100):
    '''
    X - массив массивов, внутренние массивы - координаты
    y_true - набор точек, принадлежащих определённым классам (индекс - номер точки, значение - номер кластера)
    :param points_amount:
    :return:
    '''
    # X, y_true = make_blobs(n_samples=points_amount, centers=4, cluster_std=0.6, random_state=2)
    # return X, y_true
    iris = load_iris()
    X = iris.data
    y_true = iris.target
    return X, y_true

def visualize_points(X, y_true):
    plt.scatter(X[:,0], X[:, 1], c=y_true, cmap="summer")
    # plt.scatter(X[:,0], X[:, 2], c=y_true)
    # plt.scatter(X[:,0], X[:, 3], c=y_true)
    # plt.scatter(X[:,2], X[:, 3], c=y_true)
    plt.show()
    return

def use_kmeans(points):
    # После выбора кластеров сюда запишем расстояния от точек до центроидов
    wcss = []
    for i in range(1, 20):
        kmeans = KMeans(n_clusters=i, init='k-means++', n_init=5, max_iter=20)
        kmeans.fit(points)
        wcss.append(kmeans.inertia_)

    plt.plot(range(1, 20), wcss)
    plt.show()
    kmeans = KMeans(n_clusters=3)
    y = kmeans.fit_predict(points)
    plt.scatter(points[:,0], points[:, 1], c = y, cmap="summer")
    # centroids = kmeans.cluster_centers_
    # plt.scatter(centroids[:, 0], centroids[:, 1], c='r')
    plt.show()

points, y_true = generate_points()
visualize_points(points, y_true)
use_kmeans(points)