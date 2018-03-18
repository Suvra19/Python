from pprint import pprint
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
    for line in lines[1:len(lines)]:
        edge = line.split()
        if len(edge) > 0:
            index = int(edge[0]) 
            value = int(edge[1]), int(edge[2]) if isWeighted else None
            result[index].append(value)
            if not isDirected:
                index = int(edge[1])
                value = int(edge[0]), int(edge[2]) if isWeighted else None
                result[index].append(value)
    return result

if __name__ == "__main__":
    graph_str1 = """\
    D 3
    0 1
    1 0
    0 2
    """
    graph_str2 = """\
    D 3 W
    0 1 7
    1 0 -2
    0 2 0
    """

    graph_str3 = """\
    D 7
    1 6
    1 2
    1 5
    2 5
    2 3
    5 4
    3 4
    """

    graph_str4 = """\
    U 7
    1 2
    1 5
    1 6
    2 3
    2 5
    3 4
    4 5
    """

    graph_str5 = """\
    U 12 W
    0 1 1
    1 9 12
    1 10 3
    1 11 -4
    10 11 25
    """

    graph_string6 = """\
    U 4
    0 1
    0 2
    0 3
    1 2
    1 3
    """

    graph_str6 = """\
    D 5 W
0 1 1
0 2 4
1 2 2
2 3 1
2 4 3
4 0 8
4 3 2
"""
graph6 = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

pprint(adjacency_list(graph6))