def cycle_length(n):
    if n == 1:
        return 1;
    if n % 2 == 0:
        n = n // 2;
    else:
        n = 3*n + 1;
    return 1 + cycle_length(n);

if __name__ == "__main__":
    for n in range(1, 11):
        print(cycle_length(n));
