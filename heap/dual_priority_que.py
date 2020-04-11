# do all operations and return result of que
def solution(operations):
    ans = []
    for op in operations:
        cd, n = op.split(' ')
        if cd == 'I':  # insert
            ans.append(int(n))
        elif cd == 'D' and len(ans) > 0:  # delete when len of list > 0
            if n == '1':  # delete max number
                ans.pop()
            else:  # delete min number
                ans.pop(0)
        ans.sort()  # sort ASC

    if len(ans) == 0:
        return [0, 0]
    else:
        return [ans[-1], ans[0]]
