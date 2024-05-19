import networkx as nx

# Створення графу з вагами
G = nx.Graph()

# Додавання вершин та ребер з вагами
edges_with_weights = [
    ('Station 1', 'Station 2', 7), ('Station 2', 'Station 3', 10), ('Station 3', 'Station 4', 3),
    ('Station 4', 'Station 5', 4), ('Station 5', 'Station 6', 2), ('Station 6', 'Station 7', 1),
    ('Station 7', 'Station 8', 3), ('Station 8', 'Station 9', 4), ('Station 9', 'Station 10', 5),
    ('Station 10', 'Station 11', 6), ('Station 11', 'Station 12', 7), ('Station 12', 'Station 13', 8),
    ('Station 13', 'Station 14', 9), ('Station 14', 'Station 15', 10), ('Station 15', 'Station 1', 8),
    ('Station 1', 'Station 6', 12), ('Station 2', 'Station 7', 11), ('Station 3', 'Station 8', 5),
    ('Station 4', 'Station 9', 9), ('Station 5', 'Station 10', 2)
]
G.add_weighted_edges_from(edges_with_weights)

# Використання алгоритму Дейкстри для знаходження найкоротших шляхів
def dijkstra_all_pairs(graph):
    path_lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    return path_lengths

# Знаходження найкоротших шляхів від усіх до усіх
all_pairs_shortest_paths = dijkstra_all_pairs(G)

# Вивід результатів
for source, paths in all_pairs_shortest_paths.items():
    print(f"Найкоротші шляхи від {source}:")
    for target, length in paths.items():
        print(f"  до {target}: {length} км")
