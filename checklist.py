from enum import Enum

class State(Enum):
    UNDISCOVERED = "U"
    DISCOVERED = "D"
    PROCESSED = "P"

def adjacency_list(graph_str):
    isDirected = False
    lines = graph_str.splitlines()
    graphProps = lines[0].split()
    if graphProps[0] == 'U':
        return []
    numVertices = int(graphProps[1])
    result = [[] for _ in range(numVertices)]
    for line in lines[1:len(lines)]:
        edge = line.split()
        if len(edge) > 0:
            index = int(edge[0]) 
            value = int(edge[1])
            result[index].append(value)
    return result

def dfs_tree(adj_list):
    vertices = len(adj_list)
    state = [State.UNDISCOVERED] * vertices
    parent = [None] * vertices
    ordering = []
    for i in range(vertices):
        if state[i] == State.UNDISCOVERED:
            state[i] = State.DISCOVERED
            if not dfs_loop(adj_list, i, state, parent, ordering):
                ordering.clear()
                break
    ordering.reverse()
    return ordering

def dfs_loop(adj_list, vertex, state, parent, ordering):
    for v in adj_list[vertex]:
        currentVertex = v
        if state[currentVertex] == State.UNDISCOVERED:
            state[currentVertex] = State.DISCOVERED
            parent[currentVertex] = vertex
            if not dfs_loop(adj_list, currentVertex, state, parent, ordering):
                return False
        elif state[currentVertex] == State.DISCOVERED and parent[currentVertex] != vertex:
            return False
    state[vertex] = State.PROCESSED
    ordering.append(vertex)
    return True

def checklist(conditions):
    check_list = dfs_tree(adjacency_list(conditions))
    return None if len(check_list) == 0 else check_list
    
if __name__ == "__main__":
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
    0 2
    1 2
    2 3
    2 4
    """

    print(checklist(conditions1))
    #print(checklist(conditions5) in [[0, 1, 2, 3, 4],
                               # [0, 1, 2, 4, 3],
                                #[1, 0, 2, 3, 4],
                                #[1, 0, 2, 4, 3]])
    print(checklist(conditions2) in [[0, 1, 2], [1, 0, 2]])
    # ordering = dfs_tree(adjacency_list(graph_string5))
    # print(ordering)
    # for i in range(len(ordering)):
    #     print(ordering.pop())


    #print(dfs_tree(adjacency_list(graph_string4), 3))
    #print(dfs_tree(adjacency_list(graph_string2), 1))