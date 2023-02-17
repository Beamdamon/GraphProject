import networkx

#networkx functions (Dijksra's, A*, Breadth-first search)
def dijkstra(graph, start,end):
    path = networkx.dijkstra_path(graph,start,end)
    print(f'Dijkstra shortest path from {start} -> {end}: {path}')
def astar(graph,start,end):
    path = networkx.dijkstra_path(graph,start,end)
    print(f'A* shortest path from {start} -> {end}: {path}')
def bfs(graph, start):
    bfs_edges = networkx.bfs_edges(graph, start)
    print(f' Breadth-first search from {start}:{list(bfs_edges)}')

#Creates an empty directional graph
graph = networkx.DiGraph()

#Directional edges with weights from graph.png
edges = [
    ('A', 'B', 2), ('A', 'H', 4),
    ('B', 'C', 4),
    ('C', 'D', 3),
    ('D', 'E', 2),
    ('E', 'M', 3), ('E', 'F', 2),
    ('F', 'L', 4), ('F', 'K', 3),
    ('K', 'L', 2),
    ('L', 'M', 1),
    ('M', 'N', 4),
    ('N', 'O', 1),
    ('O', 'P', 1),
    ('P', 'Q', 1), ('P', 'T', 2),
    ('Q', 'R', 4),
    ('T', 'S', 1),
    ('A', 'H', 4),
    ('H', 'I', 1),
    ('I', 'J', 2),
    ('J', 'G', 1),
    ('G', 'F', 3)
]

#Creates nodes and graph based on edges with weights
graph.add_weighted_edges_from(edges)

#Shortest path using Dijkstra's Algorithm
dijkstra(graph, 'A', 'S')
dijkstra(graph, 'A', 'R')
dijkstra(graph, 'A', 'K')

#Shortest path using a* algorithm
astar(graph, 'A', 'S')
astar(graph, 'A', 'R')
astar(graph, 'A', 'K')

# Breadth-first sorting, list of possible paths from the starting node
bfs(graph,'A')
bfs(graph,'S')
bfs(graph,'F')
bfs(graph,'K')