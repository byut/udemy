#
# HT: Subarray Sum
#
# Given an array of integers nums and a target integer
# target, write a Python function called subarray_sum that
# finds the indices of a contiguous subarray in nums that add
# up to the target sum using a hash table (dictionary).
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5804814
#


def subarray_sum(nums, target):
    dict = {}
    for i, num in enumerate(nums):
        if num == target:
            return [i, i]
        remaining = target - num
        if remaining in dict:
            return [dict[remaining], i]
        new_dict = {}
        for key in dict:
            new_dict[key + num] = dict[key]
        dict = new_dict
        dict[num] = i
    return []
