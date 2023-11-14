# Алгоритм кратчайшего незамкнутого пути

# 1. Случайным образом заполнить матрицу весов в будущем графе.
# 2. Вывести граф целиком в виде рисунка (можно сделать его неполным, неориентированным),
# вывод можно осуществить при помощи какой-либо из библиотек, например networkx.
# 3. Найти минимальное остовное дерево (код написать самим) и вывести его в виде рисунка.
# 4. Разбить на кластеры и вывести итоговое множество.

import random

import matplotlib.pyplot as plt
import networkx as nx
import sys


def add_edge(edges, i_node, j_node):
    """
    Метод добавляет к массиву edges грань от i_node к j_node со случайным весом
    :param edges: Массив граней
    :param i_node: Первый узел
    :param j_node: Второй узел
    :return:
    """
    weight = random.randint(1, 9)
    edges.append([i_node, j_node, weight])


def add_random_edges(edges, nodes):
    """
    Метод случайным образом генерирует грани и записывает их в edges
    :param edges:
    :param nodes:
    :return:
    """
    for i_node in range(len(nodes)):
        edge_count = 0
        for j_node in range(i_node + 1, len(nodes)):
            if random.randint(0, 1) == 0:
                edge_count += 1
                add_edge(edges, i_node, j_node)
        if edge_count == 0:
            j_node = random.randint(i_node + 1, len(nodes))
            add_edge(edges, i_node, j_node)


def is_edge_in_edges(edges, edge):
    """
    Метод проверяет, находится ли грань edge в массиве edges
    :param edges:
    :param edge:
    :return:
    """
    for i_node, j_node, weight in edges:
        if i_node == edge[0] and j_node == edge[1]:
            return True

    return False


def display_graph(nodes_amount, edges, min_edges=False):
    # Создаем пустой неориентированный граф
    G_graph_data = nx.Graph()
    # Добавляем узлы в граф из последовательности чисел
    G_graph_data.add_nodes_from(range(nodes_amount))

    for i_node, j_node, weight in edges:
        if min_edges:
            if not is_edge_in_edges(min_edges, [i_node, j_node]):
                G_graph_data.add_edge(i_node, j_node, weight=weight, color='b')
            else:
                G_graph_data.add_edge(i_node, j_node, weight=weight, color='r')
        else:
            G_graph_data.add_edge(i_node, j_node, weight=weight, color='b')

    weights = nx.get_edge_attributes(G_graph_data, 'weight')
    pos = nx.spring_layout(G_graph_data)

    nx.draw(
        G_graph_data,
        pos,
        with_labels=True,
        edge_color=[G_graph_data[u][v]['color'] for u, v in G_graph_data.edges()],
        width=[4 if G_graph_data[u][v]['color'] == 'r' else 1 for u, v in G_graph_data.edges()],
        node_color='orange'
    )
    nx.draw_networkx_edge_labels(G_graph_data, pos, edge_labels=weights)
    plt.show()


def min_edges_recursive(min_edges, edges, cluster_nodes):
    """
    Метод рекурсивно ищет грани с минимальным весом для узлов, которые ещё не находятся в кластере min_edges
    :param min_edges:
    :param edges:
    :param cluster_nodes:
    :return:
    """
    min_weight = sys.maxsize
    for i_node, j_node, weight in edges:
        if (weight < min_weight and
                ((i_node not in cluster_nodes and j_node in cluster_nodes) or
                 (i_node in cluster_nodes and j_node not in cluster_nodes))):
            min_weight = weight
            i_node_min = i_node
            j_node_min = j_node
    if min_weight < sys.maxsize:
        min_edges.append([i_node_min, j_node_min, min_weight])
        cluster_nodes.update({i_node_min, j_node_min})
        min_edges_recursive(min_edges, edges, cluster_nodes)
    else: return


def init_min_edges(min_edges, edges):
    """
    Метод сохраняет в min_edges минимальные грани для графа так, чтобы граф был минимальным и связным
    :param min_edges:
    :param edges:
    :return:
    """
    min_weight = sys.maxsize
    i_node_min = j_node_min = 0
    cluster_nodes = set()
    for i_node, j_node, weight in edges:
        if weight < min_weight:
            min_weight = weight
            i_node_min = i_node
            j_node_min = j_node
    min_edges.append([i_node_min, j_node_min, min_weight])
    new_edge = {i_node_min, j_node_min}
    cluster_nodes.update(new_edge)

    min_edges_recursive(min_edges, edges, cluster_nodes)
    # print(min_edges, cluster_nodes)


def delete_edge(edges, delete_edge):
    for i_node, j_node, weight in edges:
        if i_node == delete_edge[0] and j_node == delete_edge[1]:
            edges.remove([i_node, j_node, weight])


def split_into_clusters(edges, clusters_amount):
    """
    Метод разбивает целый кластер edges на clusters_amount кластеров
    :param edges:
    :param clusters_amount:
    :return:
    """
    if clusters_amount > 1:
        max_weight = -1
        for i_node, j_node, weight in edges:
            if weight > max_weight:
                max_weight = weight
                i_node_max_weight = i_node
                j_node_max_weight = j_node
        delete_edge(edges, [i_node_max_weight, j_node_max_weight])
        clusters_amount -= 1
        split_into_clusters(edges, clusters_amount)
    else: return


nodes_amount = 4
clusters_amount = 3
# Создаём последовательность чисел от 0 до points_amount - 1
nodes = range(nodes_amount)

edges = []
add_random_edges(edges, nodes)
display_graph(nodes_amount, edges)

# print(edges)

min_edges = []
init_min_edges(min_edges, edges)
display_graph(nodes_amount, edges, min_edges)

split_into_clusters(min_edges, clusters_amount)
display_graph(nodes_amount, edges, min_edges)
