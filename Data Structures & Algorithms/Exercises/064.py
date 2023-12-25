#
# Set: Longest Consecutive Sequence
#
# Given an unsorted array of integers, write a function that finds
# the length of the  longest_consecutive_sequence
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5807022
#


def longest_consecutive_sequence(arr):
    arr_set = set(arr)
    result = 0
    for num in arr:
        if num - 1 not in arr_set:
            current = 1
            while num + 1 in arr_set:
                current += 1
                num += 1
            result = max(result, current)
    return result
