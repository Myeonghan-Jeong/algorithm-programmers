# count how many progress can development each day
from math import ceil


def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):  # check taken time for develop each progress
        progresses[i] = ceil((100 - progresses[i]) / speeds[i])

    cnt, stand = 1, progresses[0]
    for i in range(1, len(progresses)):  # check how many progress will develop eah day
        if progresses[i] <= stand:
            cnt += 1
        else:
            answer.append(cnt)
            cnt, stand = 1, progresses[i]

    answer.append(cnt)  # add left progresses
    return answer
