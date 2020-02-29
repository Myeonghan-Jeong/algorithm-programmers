# count how many days passed when stock price lower than original price
from collections import deque


def solution(prices):
    ln = len(prices)

    answer = deque()
    for i in range(ln - 1):
        price = prices[i]
        for j in range(i + 1, ln):
            if prices[j] < price:
                answer.append(j - i)
                break
        else:
            answer.append(ln - i - 1)
    answer.append(0)

    return list(answer)
