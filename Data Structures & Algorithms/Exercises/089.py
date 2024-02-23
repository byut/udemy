#
# Bubble Sort
#
# Write a function called bubble_sort that sorts a list of integers in ascending
# order using the Bubble Sort algorithm.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796280
#


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
