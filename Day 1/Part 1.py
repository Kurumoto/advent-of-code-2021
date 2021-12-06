from math import inf


def get_input():
    data = []
    with open("depths.txt") as f:
        data = f.readlines()
    return [int(line) for line in data]


def solve(depths):
    prev = inf
    count = 0
    for depth in depths:
        if depth > prev:
            count += 1
        prev = depth
    return count


print(solve(get_input()))
