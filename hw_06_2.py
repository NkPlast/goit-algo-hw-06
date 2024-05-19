import networkx as nx

# Використання графа з першого завдання
G = nx.Graph()
routes = [
    ('Station 1', 'Station 2'), ('Station 2', 'Station 3'), ('Station 3', 'Station 4'),
    ('Station 4', 'Station 5'), ('Station 5', 'Station 6'), ('Station 6', 'Station 7'),
    ('Station 7', 'Station 8'), ('Station 8', 'Station 9'), ('Station 9', 'Station 10'),
    ('Station 10', 'Station 11'), ('Station 11', 'Station 12'), ('Station 12', 'Station 13'),
    ('Station 13', 'Station 14'), ('Station 14', 'Station 15'), ('Station 15', 'Station 1'),
    ('Station 1', 'Station 6'), ('Station 2', 'Station 7'), ('Station 3', 'Station 8'),
    ('Station 4', 'Station 9'), ('Station 5', 'Station 10')
]
G.add_edges_from(routes)

# Функція для BFS
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))

# Функція для DFS
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for next in set(graph.neighbors(start)) - set(path):
        res_path = dfs_path(graph, next, goal, path + [next])
        if res_path:
            return res_path

# Виконання BFS і DFS
start, goal = 'Station 1', 'Station 10'
bfs_result = bfs_path(G, start, goal)
dfs_result = dfs_path(G, start, goal)

print("BFS path:", bfs_result)
print("DFS path:", dfs_result)
