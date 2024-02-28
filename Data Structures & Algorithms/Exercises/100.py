#
# List: Remove Element
#
# Given a list of integers nums and an integer val, write a function
# remove_element that removes all occurrences of val in the list in-place
# and returns the new length of the modified list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5858524
#


def remove_element(arr, val):
    i = 0
    while i < len(arr):
        if arr[i] == val:
            arr.pop(i)
        else:
            i += 1
    return len(arr)
