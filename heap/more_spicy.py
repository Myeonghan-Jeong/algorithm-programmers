# make all food have more than scoville K
import heapq  # use heapq for min heap


def solution(scoville, K):
    heap = []
    for food in scoville:  # add foods
        heapq.heappush(heap, food)

    answer = 0
    while True:
        base = heapq.heappop(heap)
        if base >= K:  # if min scoville is more than K, return answer
            return answer
        else:
            if len(heap) == 0:  # if there is no food more than K, return -1
                return -1
            else:
                add = heapq.heappop(heap)
                new = base + add * 2  # make new food
                heapq.heappush(heap, new)
                answer += 1
