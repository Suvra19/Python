def key_positions(seq, key):
    k = max([key(a) for a in seq])
    print("Max: ", k)
    c = [0] * (k + 1)
    print("C lenght ", len(c))
    for a in seq:
        index = key(a)
        c[index] = c[index] + 1
    print("First loop: ",c)
    sum = 0
    for i in range(k + 1):
        c[i], sum = sum, sum + c[i]
    print("O/P ", c)
    return c 

if __name__ == "__main__":
    # print(key_positions([0, 1, 2], lambda x: x))
    # print(key_positions([2, 1, 0], lambda x: x))
    # print(key_positions([1, 2, 3, 2], lambda x: x))
    # print(key_positions([5], lambda x: x))
    # print(key_positions(range(-3,3), lambda x: x**2))
    # print(key_positions(range(1000), lambda x: 4))
    # print(key_positions([1] + [0] * 100, lambda x: x))
    # print(key_positions([3, 1, 2], lambda x: x))
    print(key_positions([2, -2, 1], lambda x: x * x))