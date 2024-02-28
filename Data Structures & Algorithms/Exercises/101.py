#
# List: Find Max Min
#
# Write a Python function that takes a list of integers as input and returns a
# tuple containing the maximum and minimum values in the list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5834720
#


def find_max_min(arr):
    length = len(arr)
    if length == 0:
        return None, None
    maxval, minval = arr[0], arr[0]
    for i in range(length):
        minval = arr[i] if arr[i] < minval else minval
        maxval = arr[i] if arr[i] > maxval else maxval
    return maxval, minval
