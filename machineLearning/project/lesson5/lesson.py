import random
import numpy as np
# Библиотека для рисования
import pygame
# Для вычисления расстояния между точками
from math import dist

def scatter(point):
    radius_for_points = 5
    points_amount = random.randint(3, 5)
    points = []

    for i in range(points_amount):
        radius = random.randint(radius_for_points, 3 * radius_for_points)
        angle = random.randint(0, 360)
        x_coordinate = radius * np.cos(2 * np.pi * angle / 360) + point[0]
        y_coordinate = radius * np.sin(2 * np.pi * angle / 360) + point[1]
        points.append([x_coordinate, y_coordinate])
    return points

pygame.init()
screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)

# Покрасим экран в белый
screen.fill('white')
pygame.display.update()

# Флаг для закрытия paint
is_paint_opened = True

# Радиус шаров для отрисовки
circle_radius = 5

mouse_button_down = False
points = []

# Количество соседей для того, чтобы считать точку зелёной
required_neighbor_amount = 3

# is_paint_opened = False
while is_paint_opened:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.WINDOWCLOSE:
            is_paint_opened = False

        # В консоли можно увидеть все действия, которые вызываются мышкой (либо клавиатурой)
        # print(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_button_down = True

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_button_down = False

        if event.type == pygame.WINDOWEXPOSED:
            screen.fill('white')
            for point in points:
                pygame.draw.circle(screen, color='black', center=point, radius=circle_radius)

        if mouse_button_down:
            new_circle_coordinates = event.pos
            if len(points):
                if dist(new_circle_coordinates, points[-1]) > 5 * circle_radius:
                    points.append(new_circle_coordinates)
                    pygame.draw.circle(screen, color='black', center=new_circle_coordinates, radius=circle_radius)
            else:
                points.append(new_circle_coordinates)
                pygame.draw.circle(screen, color='black', center=new_circle_coordinates, radius=circle_radius)

        pygame.display.update()

        # if event.type == pygame.KEYDOWN and event.unicode == '1':
        #     # Искусственное добавление точек, удалить после выполнения
        #     points = [[162, 40], [141, 54], [119, 67], [99, 83], [80, 100], [63, 119], [49, 140], [39, 163], [32, 188], [30, 213], [30, 239], [35, 264], [43, 288], [55, 310], [71, 330], [91, 346], [114, 356], [139, 362], [164, 368], [189, 371], [214, 375], [239, 380], [264, 382], [289, 383], [314, 385], [340, 388], [365, 391], [390, 393], [415, 394], [442, 394], [468, 393], [494, 386], [516, 374], [538, 360], [556, 342], [572, 321], [586, 300], [591, 275], [593, 250], [593, 224], [589, 199], [583, 174], [574, 150], [560, 128], [543, 109], [524, 91], [502, 79], [479, 68], [455, 59], [430, 53], [404, 47], [379, 41], [354, 37], [328, 37], [303, 35], [277, 34], [252, 33], [226, 33], [200, 33], [172, 120], [164, 144], [183, 161], [207, 152], [218, 129], [199, 112], [417, 171], [438, 156], [463, 153], [484, 168], [495, 191], [476, 209], [451, 211], [426, 204], [415, 181], [133, 251], [156, 262], [180, 272], [205, 279], [228, 289], [253, 293], [278, 294], [303, 297], [328, 298], [354, 296]]
        #     # points = [[162, 40], [141, 54], [119, 67], [99, 83], [80, 100], [63, 119], [49, 140]]
        #     # points = [[1, 1], [1, 2], [1, 3], [50, 50], [50, 51], [50, 52], [51, 51], [15, 1,], [13, 2], [10, 2], [8, 5], [5, 8]]
        #     for point_index in range(len(points)):
        #         pygame.draw.circle(screen, color='black', center=points[point_index], radius=circle_radius)
        #     pygame.display.update()
        #     # Искусственное добавление точек, удалить после выполнения

        if event.type == pygame.KEYDOWN and event.unicode == '2':
            # Считаем, для какого минимального радиуса у меня будет нужное кол-во соседей (neighbor_amount)
            # suitable_radius = 0
            # for current_radius in range(1, 50):
            #     for point_enum in enumerate(points):
            #         # point_enum[0] - индекс точки; point_enum[1] - сама точка
            #         current_neighbor_amount = 0
            #         potential_neighbors = points.copy()
            #         potential_neighbors.pop(point_enum[0])
            #         for potential_neighbor in potential_neighbors:
            #             if (dist(point_enum[1], potential_neighbor)) < current_radius:
            #                 current_neighbor_amount += 1
            #
            #         if current_neighbor_amount >= required_neighbor_amount:
            #             pygame.draw.circle(screen, color='red', center=point_enum[1], radius=circle_radius)
            #             pygame.display.update()
            #             suitable_radius = current_radius + 10
            #             break
            #     if suitable_radius > 0:
            #         break

            suitable_radius = 60
            print(suitable_radius)
            # Теперь с таким радиусом надо найти "зелёные", "жёлтые" и "красные" точки и пометить их
            point_neighbors_amount = [0] * len(points)
            for current_point_enum in enumerate(points):
                # current_point_enum[0] - индекс точки; current_point_enum[1] - сама точка
                potential_neighbors = points.copy()
                potential_neighbors.pop(current_point_enum[0])
                for potential_neighbor in potential_neighbors:
                    if dist(potential_neighbor, current_point_enum[1]) <= suitable_radius:
                        point_neighbors_amount[current_point_enum[0]] += 1

            # print(point_neighbors_amount) # количество соседей у точки

            for neighbor_amount_enum in enumerate(point_neighbors_amount):
                if neighbor_amount_enum[1] == 1 or neighbor_amount_enum[1] == 2:
                    color = 'yellow'
                elif neighbor_amount_enum[1] == 0:
                    color = 'red'
                else:
                    color = 'green'
                pygame.draw.circle(screen, color=color, center=points[neighbor_amount_enum[0]], radius=circle_radius)
                pygame.display.update()

        def find_neighbors(point, points, suitable_radius):
            """
            Метод ищет соседей для точки (point) в точках (points) в радиусе (suitable_radius)
            :param point: Точка для поиска соседей
            :param points: Массив точек среди которых ищем соседей
            :param suitable_radius: Радиус в пределах которого ищем соседей
            :return: neighbors: Массив индексов соседей
            """
            neighbors = []

            for potential_neighbor_index in range(len(points)):
                distance_point_to_point = dist(points[potential_neighbor_index], point)
                if suitable_radius >= distance_point_to_point > 0:
                    neighbors.append(potential_neighbor_index)

            return neighbors

        def is_points_have_clusters(points, clusters):
            """
            Метод проверяет, какому кластеру принадлежат точки и выдаёт номер кластера
            :param points: Массив индексов точек
            :param clusters: Массив кластеров (индекс - номер кластера, значение - массив номеров точек в кластере)
            :return: Номер кластера | Массив кластеров | False
            """
            exist_cluster = []
            for cluster_index, cluster in enumerate(clusters):
                if any(point in cluster for point in points):
                    exist_cluster.append(cluster_index)

            if len(exist_cluster) == 0:
                return False
            elif len(exist_cluster) == 1:
                return exist_cluster[0]
            return exist_cluster

        def merge_clusters(clusters_to_merge, clusters):
            """
            Метод объединяет кластеры clusters_to_merge в один кластер
            :param clusters_to_merge: Массив с индексами кластеров для объединения
            :param clusters: Массив всех кластеров
            """
            for index_old_point, old_cluster_point in enumerate(clusters[clusters_to_merge[1]]):
                clusters[clusters_to_merge[0]].append(old_cluster_point)
                del clusters[clusters_to_merge[1]][index_old_point]


        if event.type == pygame.KEYDOWN and event.unicode == '3':
            # Присвоим кластер каждой точке.
            # Кластеры храним в двумерном массиве, где индекс - номер кластера, значение -
            # массив номеров точек, которые в этом кластере
            clusters = [[]]
            # Массив крайних точек, которые могли не попасть никуда
            edges_point = []
            for current_point_enum in enumerate(points):

                current_neighbors = find_neighbors(current_point_enum[1], points, suitable_radius)
                # Если эти соседи уже в кластерах, добавляем к этому же кластеру
                exist_cluster = is_points_have_clusters(current_neighbors, clusters)
                if not isinstance(exist_cluster, list) and exist_cluster:
                    clusters[exist_cluster].append(current_point_enum[0])
                # Если соседи в разных кластерах, объединяем их в один кластер
                elif isinstance(exist_cluster, list) and exist_cluster:
                    merge_clusters(exist_cluster, clusters)
                # Если соседей нет, создаём новый кластер в clusters
                elif len(current_neighbors) >= required_neighbor_amount:
                    clusters.append([])
                    clusters[len(clusters) - 1].append(current_point_enum[0])
                else:
                    edges_point.append(current_point_enum[0])

            for edge_point in edges_point:
                current_neighbors = find_neighbors(points[edge_point], points, suitable_radius)
                exist_cluster = is_points_have_clusters(current_neighbors, clusters)
                if exist_cluster:
                    clusters[exist_cluster].append(edge_point)


            # Перекрасим разные кластеры
            color = ['olive', 'darkorange', 'lightcoral', 'teal', 'violet',
                     'skyblue', 'blue', 'cyan', 'meta', 'black', 'pink', 'gray', 'lawn green', 'gainsboro', 'steel blue', 'salmon', 'maroon']
            for cluster_index, cluster in enumerate(clusters):
                for point_in_cluster in cluster:
                    pygame.draw.circle(screen, color=color[cluster_index], center=points[point_in_cluster], radius=circle_radius)
                    pygame.display.update()


