# count how many sticks will cutted by lazers
from collections import deque


def solution(arrangement):
    answer = 0

    sticks = deque()
    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            sticks.append(i)
        else:
            if i == sticks[-1] + 1:  # () means lazer
                sticks.pop()
                answer += len(sticks)  # cut left sticks
            else:  # (....) means stick
                sticks.pop()
                answer += 1  # add left stick

    return answer
