#
# Quick Sort
#
# Write a function called quick_sort_helper that performs the quick sort
# algorithm recursively on a list of integers.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796232
#


def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
    arr[swap_index], arr[pivot_index] = arr[pivot_index], arr[swap_index]
    return swap_index


def quick_sort_helper(arr, start, end):
    if start < end:
        pivot_index = pivot(arr, start, end)
        quick_sort_helper(arr, start, pivot_index - 1)
        quick_sort_helper(arr, pivot_index + 1, end)
    return arr


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
