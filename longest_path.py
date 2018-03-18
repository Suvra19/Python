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
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        print("Next vertex ", u)
        in_tree[u] = True
        for v,weight in adj[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance

def next_vertex(in_tree, distance):
    max_distance = float('inf')
    next_vertex = -1
    n = len(in_tree)
    for i in range(n):
        if in_tree[i] == False and distance[i] < max_distance:
            max_distance = distance[i]
            next_vertex = i
    if (next_vertex == -1):
        candidate_vertices = [i for i in range(n) if in_tree[i] == False]
        next_vertex = candidate_vertices[0]
    return next_vertex

def longest_path(map, start):
    adj_list = adjacency_list(map)
    parent, distance = dijkstra(adj_list, start)
    print("Parent ", parent)
    print("Distance ", distance)
    maxVal = max([i for i in distance if i != float('inf')])
    destination = distance.index(maxVal)
    curentVertex = destination
    result = [curentVertex]
    while (curentVertex != start):
        curentVertex = parent[curentVertex]
        result.append(curentVertex)
    result.reverse()
    return result

if __name__ == "__main__":

    map = """\
    U 4 W
    0 2 5
    0 3 2
    3 2 2
    """

    map2 = """\
    U 5 W
    0 2 5
    0 3 2
    3 2 2
    """
    city_map = """\
U 5 W
0 1 100
0 2 100
1 2 100
2 3 2000
3 4 2000
2 4 5000
"""

print(longest_path(city_map, 0))
print(longest_path(city_map, 1))
print(longest_path(city_map, 2))

#print(longest_path(city_map, 0))

    #print(longest_path(map, 0))
    #print(dijkstra(adjacency_list(graph6), 3) in [[3, 0], [3, 2]])




