"""
Given an integer n, return the number of trailing 0s in n! (Factorial of n)
"""


def trailing_zeroes(num):
    if num == 0:
        return 0
    else:
        factorial = 1
        for i in range(1, num):
            factorial = factorial * i

    factorial = factorial * num
    zeroes_count = 0
    while factorial % 10 == 0:
        zeroes_count = zeroes_count + 1
        factorial = factorial // 10

    print('Number of trailing zeroes: ' + str(zeroes_count))


trailing_zeroes(125)

"""
More efficient way?
"""


def trailing_zeroes_efficient(num):
    curr_power_of_five = 5
    counter = 0
    while num >= curr_power_of_five:
        counter = counter + (num // curr_power_of_five)
        curr_power_of_five = curr_power_of_five * 5

    return counter


print('Number of trailing zeroes in a more efficient way: ' + str(trailing_zeroes_efficient(125)))