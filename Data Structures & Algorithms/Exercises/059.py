#
# HT: Two Sum
#
# Given an array of integers nums and a target integer
# target, find the indices of two numbers in the array that add
# up to the target.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5804460
#


def two_sum(list, num):
    dict = {}
    for i, n in enumerate(list):
        if num - n in dict:
            return [dict[num - n], i]
        dict[n] = i
    return []


print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))
