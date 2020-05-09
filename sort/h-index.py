# find max h-index in list
def solution(citations):
    for c in range(max(citations), -1, -1):  # find from max index
        cnt = len([1 for i in citations if c <= i])  # count letters over c
        if c <= cnt:  # if number of letter is bigger than h-index
            return c
