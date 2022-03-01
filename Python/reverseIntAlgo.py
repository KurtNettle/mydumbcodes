def reverseIntAlgo(number, reversed_number):
    return number // 10, reversed_number * 10 + number % 10


def reverseInt(given_number):
    reversed_number = 0
    if given_number < 0:
        while (given_number < 0):
            given_number = given_number * -1
            given_number, reversed_number = reverseIntAlgo(given_number, reversed_number)
            given_number = given_number * -1
        return reversed_number * -1
    else:
        while (given_number > 0):
            given_number, reversed_number = reverseIntAlgo(given_number, reversed_number)
        return reversed_number
    
