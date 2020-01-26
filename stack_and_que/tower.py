# check which tower can recieve signal from anoter tower
def solution(heights):
    answer = [0] * len(heights)
    while heights:
        idx, h = len(heights) - 1, heights.pop()  # pop tower info
        for i in range(len(heights) - 1, -1, -1):
            # check tower is more higher than org tower
            if heights[i] > h:
                answer[idx] = i + 1
                break

    return answer
