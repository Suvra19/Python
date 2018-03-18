from enum import Enum
from queue import Queue

class State(Enum):
    UNDISCOVERED = "U"
    DISCOVERED = "D"
    PROCESSED = "P"

def adjacency_list(graph_str):
    isDirected = False
    isWeighted = False
    lines = graph_str.splitlines()
    graphProps = lines[0].split()
    if graphProps[0] == 'D':
        isDirected = True
    if len(graphProps) > 2:
        isWeighted = True
    numVertices = int(graphProps[1])
    result = [[] for _ in range(numVertices)]
    for line in lines[1:len(lines) - 1]:
        edge = line.split()
        index = int(edge[0]) 
        value = int(edge[1]), int(edge[2]) if isWeighted else None
        result[index].append(value)
        if not isDirected:
            index = int(edge[1])
            value = int(edge[0]), int(edge[2]) if isWeighted else None
            result[index].append(value)
    print(result)
    return result

def bfs_tree(adj_list, start):
  vertices = len(adj_list)
  state = [State.UNDISCOVERED] * vertices
  parent = [None] * vertices
  vertextQueue = Queue()
  state[start] = State.DISCOVERED
  vertextQueue.put(start)
  return bfs_loop(adj_list, vertextQueue, state, parent)

def bfs_loop(adj_list, vertextQueue, state, parent):
    while not vertextQueue.empty():
        u = vertextQueue.get()
        print(adj_list[u])
        for v in adj_list[u]:
            currentVertex = int(v[0])
            if state[currentVertex] == State.UNDISCOVERED:
                state[currentVertex] = State.DISCOVERED
                parent[currentVertex] = u
                vertextQueue.put(currentVertex)
        state[u] = State.PROCESSED
    return parent

if __name__ == "__main__":
    adj_list1 = [
        [(1, None)],
        [(0, None), (2, None)],
        [(1, None)]
    ]

    adj_list2 = [
        [(1, None)],
        []
    ]

    graph_string1 = """\
    D 2
    0 1
    1 0
    """
    graph_string2 = """\
    U 7
    1 2
    1 5
    1 6
    2 3
    2 5
    3 4
    4 5
    """

    graph_string3 = """\
    D 2 W
    0 1 99
    """

    graph_string4 = """\
    U 6
    0 4
    5 4
    4 2
    2 3
    3 0
    3 4
    """

    graph_string5 = """\
    U 4
    0 1
    0 2
    0 3
    1 2
    1 3
    """

    safe_map = """\
    U 7
    1 2
    1 5
    1 6
    2 3
    2 5
    3 4
    4 5
    """
    
    print(bfs_tree(adjacency_list(safe_map), 0))