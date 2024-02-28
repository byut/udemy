#
# Pivot
#
# Write a function called pivot that helps in partitioning a list of integers
# during the quick sort algorithm.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796238
#


def pivot(arr, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if arr[i] < arr[pivot_index]:
            swap_index += 1
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
    arr[swap_index], arr[pivot_index] = arr[pivot_index], arr[swap_index]
    return swap_index
