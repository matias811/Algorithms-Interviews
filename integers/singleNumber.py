"""
SINGLE NUMBER
In this challenge you receive an array of numbers.
All numbers are repeated twice except for one, the task is to find that number and print it.
"""


def find_single_number(nums):
    if len(nums) == 0:
        return nums[0]
    empty_set = set()
    for num in nums:
        if empty_set.__contains__(num):
            empty_set.remove(num)
        else:
            empty_set.add(num)

    print(empty_set)


find_single_number([4, 1, 2, 1, 2])
find_single_number([2, 2, 1])
find_single_number([1])

"""
Even though the problem is solved above, we can improve the efficiency of the program
by using XOR, the idea is to not have to loop through the whole array, but
instead eliminate repeated numbers with XOR.
How it works:
1 ^ 1 = 0
2 ^ 2 = 0

4 ^ 1 ^ 2 ^ 1 ^ 2
4 ^ 1 ^ 1 ^ 2 ^ 2
4 ^ (1 ^ 1) ^ (2 ^ 2)
4 ^ 0 ^ 0
4
"""

def single_number_xor(nums):
    single_number = 0
    for num in nums:
        single_number = single_number ^ num

    print(single_number)


single_number_xor([4, 1, 2, 1, 2])
single_number_xor([2, 2, 1])
single_number_xor([1])