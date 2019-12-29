# check number start with another number
def solution(phone_book):
    phone_book.sort()

    for i in range(len(phone_book)):
        li = len(phone_book[i])
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] == phone_book[j][:li]:
                return False  # if there is target number
    return True  # or not
