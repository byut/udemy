#
# Heap: Kth Smallest Element in an Array
#
# Your task is to write a function find_kth_smallest(nums, k)
# to find the kth smallest number in the list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5970924
#

import heapq


def find_kth_smallest(nums, k):
    heapq.heapify(nums)
    for _ in range(1, k):
        heapq.heappop(nums)
    return heapq.heappop(nums)
