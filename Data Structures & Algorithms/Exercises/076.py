#
# Heap: Maximum Element in a Stream
#
# Write a function named stream_max that takes returns a list,
# where each element is the maximum number seen so far in the input list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5972148
#


def stream_max(nums):
    if len(nums) == 0:
        return []
    max_value = nums[0]
    res = []
    for num in nums:
        if num > max_value:
            max_value = num
        res.append(max_value)
    return res
