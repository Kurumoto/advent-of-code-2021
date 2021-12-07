def get_input():
    data = []
    with open("input.txt") as f:
        data = f.readlines()
    return data


def solve(data):
    # only the first line of the input file has the relevant data
    current_timers = list(map(int, data[0].split(',')))
    TIMER_START = 6
    for _ in range(80):
        # for all the new fishes that have spawned
        new_timers = []
        for i, timer in enumerate(current_timers):
            if timer == 0:
                # when timer 0, reset the current timer
                current_timers[i] = TIMER_START
                # and spawn new timers, and set their own reference
                # starting timers
                new_timers.append(TIMER_START+2)
            else:
                current_timers[i] = timer - 1
        current_timers.extend(new_timers)
    return len(current_timers)

print(solve(get_input()))
