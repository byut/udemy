#
# Big O: O(n^2)
#
# In this task, you are required to implement a function called
# print_items(n)
#
# This function takes one integer argument, n, and prints out a
# pair of numbers (i, j) for every possible combination of i
# and j in the range of 0 up to but not including n.
#
# Each pair (i, j) is printed on a new line. i and j iterate
# over the range independently, so every combination of i and
# j in the range should be printed.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5972218
#


def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
