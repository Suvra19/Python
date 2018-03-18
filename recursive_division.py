def recursive_divide(x, y):
    if x < y:
        return 0
    else:
        return 1 + recursive_divide(x - y, y)

if __name__ == "__main__":
    print(recursive_divide(0, 2))