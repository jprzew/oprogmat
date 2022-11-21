def factorial2(number):
    if number == 0:
        return 1

    return factorial2(number - 1) * number


factorial2(4)
