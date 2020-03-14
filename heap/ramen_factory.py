# calculate min supply for make ramen without shortage of flour
import heapq


def solution(stock, dates, supplies, k):
    heap, answer = [], 0

    idx = 0
    while stock < k:
        for i in range(idx, len(dates)):
            if dates[i] <= stock:  # if stock is enough when dates[i]
                heapq.heappush(heap, (-supplies[i], supplies[i]))  # max heap
                idx = i + 1  # increase index
            else:
                break
        stock += heapq.heappop(heap)[1]  # store max flour
        answer += 1

    return answer
