def adjacency_list(graph_str):
    isDirected = False
    lines = graph_str.splitlines()
    graphProps = lines[0].split()
    if graphProps[0] == 'D':
        isDirected = True
    numVertices = int(graphProps[1])
    result = [[] for _ in range(numVertices)]
    for line in lines[1:len(lines)]:
        edge = line.split()
        if len(edge) > 0:
            index = int(edge[0]) 
            value = int(edge[1]), int(edge[2])
            result[index].append(value)
            if not isDirected:
                index = int(edge[1])
                value = int(edge[0]), int(edge[2])
                result[index].append(value)
    return result

def dijkstra(adj, start):
    n = len(adj)
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    distance[start] = 0
    print(distance)
    print(parent)
    print(in_tree)
    print()
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v,weight in adj[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
        print(distance)
        print(parent)
        print(in_tree)
        print()
    return parent, distance

def next_vertex(in_tree, distance):
    max_distance = float('inf')
    next_vertex = 0
    for i in range(len(in_tree)):
        if in_tree[i] == False and distance[i] < max_distance:
            max_distance = distance[i]
            next_vertex = i
    return next_vertex

if __name__ == "__main__":

    graph4 = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

graph5 = """\
U 5 W
0 1 1
0 2 4
1 2 2
2 3 1
2 4 3
4 0 8
4 3 2
"""

#print(next_vertex([False, True, True, False, False], [float('inf'), 0, 3, 12, 5]))

#print(next_vertex([False, True, True, False, False, False], [float('inf'), 2, 0, 9, 8, 12]))

#print(next_vertex([False, True, False, False, True, False], [6, 0, float('inf'), float('inf'), 4, 12]))

graph6 = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""


print(dijkstra(adjacency_list(graph6), 0))




