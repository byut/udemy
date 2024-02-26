#
# Merge
#
# Write a function called merge that merges two sorted lists of integers into a
# single sorted list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796268
#


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
