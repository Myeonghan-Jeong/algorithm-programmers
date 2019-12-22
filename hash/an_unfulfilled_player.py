# find an unfulfilled player in participant
def solution(participant, completion):
    # sort each people list
    participant.sort()
    completion.sort()

    completion += ['']  # add blank for check the last person
    for i in range(len(completion)):
        if participant[i] != completion[i]:  # compare two list
            return participant[i]  # find unfulfilled player
