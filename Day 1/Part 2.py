from math import inf


def get_input():
    data = []
    with open("depths.txt") as f:
        data = f.readlines()
    return [int(line) for line in data]


def solve(depths):
    prev = inf
    count = 0
    n = len(depths)
    for i in range(2, n):
        window = sum(depths[i - 2 : i + 1])
        if window > prev:
            count += 1
        prev = window
    return count


print(solve(get_input()))
