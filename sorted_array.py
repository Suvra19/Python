import operator

def key_positions(seq, key):
    k = max([key(a) for a in seq])
    c = [0] * (k + 1)
    for a in seq:
        index = key(a)
        c[index] = c[index] + 1
    sum = 0
    for i in range(k + 1):
        c[i], sum = sum, sum + c[i]
    return c

def sorted_array(seq, key, positions):
    n = len(seq)
    b = [0] * n
    for a in seq:
        index = positions[key(a)]
        b[index] = a
        positions[key(a)] += 1
    return b

def counting_sort(iterable, key):
    positions = key_positions(iterable, key)
    return sorted_array(iterable, key, positions)

if __name__ == "__main__":
    print(counting_sort([2, -2, 1], lambda x: x*x))
    #print(sorted_array([3, 1, 2], lambda x: x, [0, 0, 1, 2]))
    #print(sorted_array([3, 2, 2, 1, 2], lambda x: x, [0, 0, 1, 4]))
    #print(sorted_array([100], lambda x: x, [0]*101))
    
    # objects = [("a", 88), ("b", 17), ("c", 17), ("d", 7)]
    # key = operator.itemgetter(1)
    # print(", ".join(object[0] for object in counting_sort(objects, key)))
