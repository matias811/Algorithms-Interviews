"""
Given an integer x, return true if x is a palindrome
A palindrome number is a number that when you reverse it, it will be the same.
Examples:
    121
    12321
    444
    7
"""


def is_palindrome(x):
    if x < 0:
        return False

    num = str(x)

    if num[-1] == '0':
        return False

    reversed_num = num[::-1]

    if num == reversed_num:
        return True
    else:
        return False


print(is_palindrome(121))
print(is_palindrome(12321))
print(is_palindrome(4342))
print(is_palindrome(-123))
print(is_palindrome(1230))

"""
Let's solve the same problem, but without converting our integer into a string
"""


def is_palindrome_extra(num):
    if num < 0:
        return False
    elif num != 0 and num % 10 == 0:
        return False
    else:
        reverse = 0
        while num > reverse:
            last_digit = num % 10
            reverse = reverse * 10 + last_digit
            num = num // 10

    return (num == reverse) or (num == reverse // 10)


print('Here are the results of palindrome without converting to string: ')
print(is_palindrome_extra(12321))
print(is_palindrome_extra(1221))
print(is_palindrome_extra(1241))