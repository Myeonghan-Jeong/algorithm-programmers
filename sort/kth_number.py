# calculate Kth number in partial array
def solution(array, commands):
    ans = [0] * len(commands)
    for c in range(len(commands)):
        s, e, t = commands[c]
        ans[c] = sorted(array[s - 1:e])[t - 1]
    return ans
