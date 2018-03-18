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

def dfs_tree(adj_list):
  vertices = len(adj_list)
  state = [State.UNDISCOVERED] * vertices
  parent = [None] * vertices
  ordering = [];
  for i in range(vertices):
      if state[i] == State.UNDISCOVERED:
          state[i] = State.DISCOVERED
          if not dfs_loop(adj_list, i, state, parent, ordering):
              ordering.clear()
              break
  return ordering

def dfs_loop(adj_list, vertex, state, parent, ordering):
    for v in adj_list[vertex]:
        currentVertex = int(v[0])
        if state[currentVertex] == State.UNDISCOVERED:
            state[currentVertex] = State.DISCOVERED
            parent[currentVertex] = vertex
            cycle_check = dfs_loop(adj_list, currentVertex, state, parent, ordering)
            if not cycle_check:
                return False
        elif state[currentVertex] == State.DISCOVERED and parent[currentVertex] != vertex:
            print("WARNING!! That's not a DAG!")
            return False
    state[vertex] = State.PROCESSED
    ordering.append(vertex)
    return True

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
    D 5
    0 2
    1 2
    2 4
    2 3
    """
    graph_string6 = """\
    D 4
    0 3
    """

    graph_string7 = """\
    D 3
    2 0
    """
    graph_string8 = """\
    D 3
    """

    conditions1 = """\
    D 2
    0 1
    """
    conditions2 = """\
    D 3
    1 2
    0 2
    """
    conditions3 = """\
    D 3
    """
    conditions4 = """\
    D 5
    2 3
    3 2
    """
    conditions5 = """\
    D 5
    0 1
    1 2
    1 3
    1 4
    """

    ordering = dfs_tree(adjacency_list(conditions4))
    ordering.reverse()
    print(ordering)


    #print(dfs_tree(adjacency_list(graph_string4), 3))
    #print(dfs_tree(adjacency_list(graph_string2), 1))