#
# List: Rotate
#
# You are given a list of n integers and a non-negative integer k.
#
# Your task is to write a function called rotate that takes the list of
# integers and an integer k as input and rotates the list to the right by k steps.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5850790
#


def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
