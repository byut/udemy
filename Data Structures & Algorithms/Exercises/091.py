#
# Insertion Sort
#
# Write a function called insertion_sort that sorts a list of integers in
# ascending order using the Insertion Sort algorithm.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796276
#


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp, j = arr[i], i - 1
        while temp < arr[j] and j >= 0:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr
