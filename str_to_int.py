def str_to_int(str):
    n = len(str)
    factor = 1
    total = 0
    for i in range(n - 1, -1, -1):
        value = ord(str[i]) - ord('0')
        total = value * factor + total
        factor *= 10
    return total

if __name__ == "__main__":
    print(type(str_to_int("12309")))