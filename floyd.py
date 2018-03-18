from pprint import pprint
def adjacency_matrix(graph_str):
    isDirected = False
    lines = graph_str.splitlines()
    graphProps = lines[0].split()
    if graphProps[0] == 'D':
        isDirected = True
    numVertices = int(graphProps[1])
    result = [[float('inf')] * numVertices for _ in range(numVertices)]
    for i in range(numVertices):
        result[i][i] = 0
    for line in lines[1:len(lines)]:
        edge = line.split()
        if len(edge) > 0:
            row = int(edge[0]) 
            col = int(edge[1])
            value = int(edge[2])
            result[row][col] = value
            if not isDirected:
               result[col][row] = value
    return result

def floyd(adjacency_matrix):
    n = len(adjacency_matrix[0])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                adjacency_matrix[i][j] = min((adjacency_matrix[i][k] + adjacency_matrix[k][j]), adjacency_matrix[i][j])
    return adjacency_matrix

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
    graph_str7 = """\
    U 3 W
    0 1 5
    2 1 7
    """
    graph_str8 = """\
    D 2 W
    0 1 4
    """

    graph_str9 = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""
graph_str10 = """\
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

graph_str11 = """\
U 5 W
0 1 1
0 2 4
1 2 2
2 3 1
2 4 3
4 0 8
4 3 2
"""


pprint(floyd(adjacency_matrix(graph_str11)))