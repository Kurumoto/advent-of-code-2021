def get_input():
    data = []
    with open("input.txt") as f:
        data = f.readlines()
    return data

def solve(data):
    gamma, epsilon = "", ""
    for i in range(12):
        if sum(bits[i] == "1" for bits in data) > len(data)//2:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2) * int(epsilon, 2)

print(solve(get_input()))
