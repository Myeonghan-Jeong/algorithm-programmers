# make the best album with given rules
from collections import deque


def solution(genres, plays):
    albums, genres_dict = {}, {}
    for g in range(len(genres)):
        name, num = genres[g], plays[g]  # get name and num of each song
        if genres[g] in albums:
            albums[name].append([num, g])
            genres_dict[name] += num
        else:
            albums[name] = deque([[num, g]])  # save each songs info
            genres_dict[name] = num  # calculate total plays in each genre

    # sort DESC about total plays of each genre
    genres_list = sorted(genres_dict.items(), key=lambda genre: -genre[1])

    answer = []
    for info in genres_list:
        name = info[0]
        # sort DESC about plays of each song and ASC about idx num of each song
        avails = sorted(albums[name], key=lambda album: (-album[0], album[1]))
        for avail in avails[:2]:  # add two songs to answer
            answer += [avail[1]]

    return answer
