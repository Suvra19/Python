from enum import Enum

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

def dfs_tree(adj_list, start):
  vertices = len(adj_list)
  state = [State.UNDISCOVERED] * vertices
  parent = [None] * vertices
  state[start] = State.DISCOVERED
  dfs_loop(adj_list, start, state, parent)
  return parent

def dfs_loop(adj_list, vertex, state, parent):
    print(vertex)
    for v in adj_list[vertex]:
        currentVertex = int(v[0])
        if state[currentVertex] == State.UNDISCOVERED:
            state[currentVertex] = State.DISCOVERED
            parent[currentVertex] = vertex
            dfs_loop(adj_list, currentVertex, state, parent)
    state[vertex] = State.PROCESSED

if __name__ == "__main__":
    adj_list1 = [
        [(1, None), (2, None)],
        [(0, None), (2, None)],
        [(0, None), (1, None)]
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
    U 5
    0 1
    1 2
    1 3
    3 4
    4 0
    """

    graph_string5 = """\
    U 4
    

    print(dfs_tree(adjacency_list(graph_string4), 3))
    #print(dfs_tree(adjacency_list(graph_string2), 1))