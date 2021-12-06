from collections import defaultdict


def get_input():
    data = []
    with open("input.txt") as f:
        data = f.readlines()
    return data


def solve(commands):
    horizontal = 0
    depth = 0
    aim = 0

    for full_command in commands:
        command, value = full_command.split()
        value = int(value)

        if command == "forward":
            horizontal += value
            depth += aim * value
        elif command == "up":
            aim -= value
        elif command == "down":
            aim += value

    return horizontal * depth


print(solve(get_input()))
