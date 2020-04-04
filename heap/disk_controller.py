# calculate min avg task time of jobs in disk
import heapq


def solution(jobs):
    # now time, previous work done time, disk
    time, end, queue = 0, -1, []

    cnt, ans = 0, 0
    while cnt < len(jobs):
        for job in jobs:  # loop jobs
            s, w = job  # inputted time, working time
            # check work is inputted during previous job is working
            if end < s <= time:
                ans += time - s  # add delayed time
                heapq.heappush(queue, w)  # put que

        if len(queue) > 0:  # if work is remain
            ans += len(queue) * queue[0]  # working time and delayed other jobs
            end = time  # previous job started
            time += heapq.heappop(queue)  # previous job done
            cnt += 1  # complete job
        else:  # if work is not remain, plus 1 time
            time += 1

    return ans // cnt
