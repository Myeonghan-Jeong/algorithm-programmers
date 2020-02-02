# calculate total time for all trucks cross bridge
from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge, time = deque(), deque()

    i, ans = 0, 0
    while True:
        if time:  # check trucks finished crossing bridge
            if time[0] == 0:
                bridge.popleft()
                time.popleft()

        if truck_weights[i] != 0:  # check next truck can get in bridge
            if sum(bridge) + truck_weights[i] <= weight:
                bridge.append(truck_weights[i])
                time.append(bridge_length)
                truck_weights[i] = 0
                if i < len(truck_weights) - 1:
                    i += 1

        for t in range(len(time)):  # cross trucks
            time[t] -= 1

        ans += 1
        if sum(truck_weights) == 0 and not bridge:  # check all trucks crossed
            break

    return ans
