from collections import Counter


def get_input():
    data = []
    with open("input.txt") as f:
        data = f.readlines()
    return data


def solve(data):
    data = get_input()
    i = 0
    while len(data) > 1:
        val = ""
        c = Counter([bits[i] for bits in data])
        val = "1" if c["1"] >= c["0"] else "0"
        data = [bits for bits in data if bits[i] == val]
        i += 1
    oxy = data[0]

    data = get_input()
    i = 0
    while len(data) > 1:
        val = ""
        c = Counter([bits[i] for bits in data])
        val = "0" if c["0"] <= c["1"] else "1"
        data = [bits for bits in data if bits[i] == val]
        i += 1
    co2 = data[0]

    return int(oxy, 2) * int(co2, 2)


print(solve(get_input()))
