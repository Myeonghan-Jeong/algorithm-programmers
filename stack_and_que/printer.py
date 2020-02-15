# find print order of target document
from collections import deque


def solution(priorities, location):
    prints = deque()
    for i in range(len(priorities)):
        prints.append([priorities[i], i])  # check priority and index

    answer = 1
    while True:
        priority, idx = prints.popleft()
        for i in range(len(prints)):
            if prints[i][0] > priority:  # find more important doc
                prints.append([priority, idx])  # if find, append doc
                break
        else:
            if idx == location:  # check it is target doc
                return answer
            answer += 1
