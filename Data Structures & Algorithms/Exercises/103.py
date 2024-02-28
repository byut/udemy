#
# List: Remove Duplicates
#
# Given a sorted list of integers, rearrange the list in-place such that all
# unique elements appear at the beginning of the list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5850736
#


def remove_duplicates(arr):
    i = 1
    while i < len(arr):
        if arr[i - 1] == arr[i]:
            arr.pop(i - 1)
        else:
            i += 1
    return len(arr)
