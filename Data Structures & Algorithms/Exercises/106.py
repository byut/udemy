#
# List: Max Sub Array
#
# Given an array of integers nums, write a function max_subarray(nums) that
# finds the contiguous subarray (containing at least one number) with the
# largest sum and returns its sum.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5858472
#


def max_subarray(nums):
    if len(nums) == 0:
        return 0
    maxsum = float("-inf")
    for i in range(len(nums)):
        curr = nums[i]
        maxsum = curr if curr > maxsum else maxsum
        for j in range(i + 1, len(nums)):
            curr += nums[j]
            maxsum = curr if curr > maxsum else maxsum
    return maxsum
