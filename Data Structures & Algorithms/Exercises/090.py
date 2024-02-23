#
# Selection Sort
#
# Write a function called selection_sort that sorts a list of integers in
# ascending order using the Selection Sort algorithm.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796278
#


def selection_sort(arr):
    for i in range(len(arr) - 1):
        minindex = i
        for j in range(i + 1, len(arr)):
            minindex = j if arr[minindex] > arr[j] else minindex
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr
