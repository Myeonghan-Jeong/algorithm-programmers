# find person who got the most questions right with sepcial answer patterns
def solution(answers):
    # answer patterns
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # count got questions right
    i, j, k = 0, 0, 0
    for a in range(len(answers)):
        if answers[a] == p1[a % len(p1)]:
            i += 1
        if answers[a] == p2[a % len(p2)]:
            j += 1
        if answers[a] == p3[a % len(p3)]:
            k += 1

    ans = []
    if i == max(i, j, k):
        ans.append(1)
    if j == max(i, j, k):
        ans.append(2)
    if k == max(i, j, k):
        ans.append(3)

    return ans
