import networkx as nx
import matplotlib.pyplot as plt
import random

# Створення пустого графу
G = nx.Graph()

# Додавання станцій
stations = ['Station ' + str(i) for i in range(1, 16)]  # 15 унікальних станцій
G.add_nodes_from(stations)

# Додавання маршрутів
routes = [
    ('Station 1', 'Station 2'), ('Station 2', 'Station 3'), ('Station 3', 'Station 4'),
    ('Station 4', 'Station 5'), ('Station 5', 'Station 6'), ('Station 6', 'Station 7'),
    ('Station 7', 'Station 8'), ('Station 8', 'Station 9'), ('Station 9', 'Station 10'),
    ('Station 10', 'Station 11'), ('Station 11', 'Station 12'), ('Station 12', 'Station 13'),
    ('Station 13', 'Station 14'), ('Station 14', 'Station 15'), ('Station 15', 'Station 1')
]
G.add_edges_from(routes)

# Додаткові зв'язки для створення циклів та перетинів
extra_connections = [
    ('Station 1', 'Station 6'), ('Station 2', 'Station 7'), ('Station 3', 'Station 8'),
    ('Station 4', 'Station 9'), ('Station 5', 'Station 10')
]
G.add_edges_from(extra_connections)

# Візуалізація графу
pos = nx.spring_layout(G)  # Розташування вершин графа
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10, font_weight='bold')
plt.title("Граф моделі транспортної мережі міста")
plt.show()

# Аналіз основних характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступені вершин:", dict(G.degree()))
