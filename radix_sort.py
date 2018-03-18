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

def radix_sort(numbers, d):
    n = 1
    for i in range(1, d + 1):
        numbers = counting_sort(numbers, lambda x: int((x / n) % 10))
        print(numbers)
        n *= 10
    return numbers

if __name__ == "__main__":
    #print(radix_sort([329, 457, 657, 839, 436, 720, 355], 3))
    #print(radix_sort([329, 457, 657, 839, 436, 720, 355], 1))
    #print(radix_sort([329, 457, 657, 839, 436, 720, 355], 2))
    print(radix_sort([31, 22, 131, 44], 3))