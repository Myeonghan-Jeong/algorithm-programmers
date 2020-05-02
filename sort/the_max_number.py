# find the max number can made by numbers
def solution(numbers):
    numbers = list(map(str, numbers))
    # in str, '3' > '24' == True, '3' * 4 > '1000' * 4 == True
    numbers.sort(key=lambda x: 4 * x, reverse=True)  # max len of number is 4
    return str(int(''.join(numbers)))
