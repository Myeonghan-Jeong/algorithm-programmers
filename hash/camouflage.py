# count methods for camoflage with change at least one cloth
def solution(clothes):
    can_wear = {}
    for cloth in clothes:
        if cloth[1] in can_wear:
            can_wear[cloth[1]].append(cloth[0])
        else:
            can_wear[cloth[1]] = [cloth[0]]

    cnt = 1
    for key in can_wear:
        # method: wear or not each clothes, so plus 1
        cnt *= len(can_wear[key]) + 1

    # cannot camoflage with nude, so minus 1
    return cnt - 1
