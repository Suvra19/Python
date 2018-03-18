from enum import Enum
from queue import Queue

class State(Enum):
    UNDISCOVERED = "U"
    DISCOVERED = "D"
    PROCESSED = "P"

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
            value = int(edge[1])
            result[index].append(value)
            if not isDirected:
                index = int(edge[1])
                value = int(edge[0])
                result[index].append(value)
    return result

def bfs_tree(adj_list):
    vertices = len(adj_list)
    state = [State.UNDISCOVERED] * vertices
    parent = [None] * vertices
    vertextQueue = Queue()
    result = []
    for i in range(vertices):
        newComponent = []
        if state[i] == State.UNDISCOVERED:
            state[i] = State.DISCOVERED
            vertextQueue.put(i)
            newComponent.append(i)
            bfs_loop(adj_list, vertextQueue, state, newComponent)
            result.append(newComponent)
    return result

def bfs_loop(adj_list, vertextQueue, state, newComponent):
    while not vertextQueue.empty():
        u = vertextQueue.get()
        for v in adj_list[u]:
            currentVertex = v
            if state[currentVertex] == State.UNDISCOVERED:
                state[currentVertex] = State.DISCOVERED
                newComponent.append(currentVertex)
                vertextQueue.put(currentVertex)
        state[u] = State.PROCESSED

def possible_locations(safe_map):
    adj_list = adjacency_list(safe_map)
    return bfs_tree(adj_list)

if __name__ == "__main__":
    safe_map1 = """\
    U 7
    1 2
    1 5
    1 6
    2 3
    2 5
    3 4
    4 5
    """
    safe_map2 = """\
    U 2
    0 1
    """
    safe_map3 = """\
    U 2
    """
    safe_map4 = """\
    U 0
    """

    safe_map5 = """\
    U 1
    """

    safe_map6 = """\
    U 7
    1 2
    1 5
    2 3
    2 5
    3 4
    4 5
    """
    
    print(sorted(sorted(areas) for areas in possible_locations(safe_map6)))