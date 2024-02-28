#
# List: Find Longest String
#
# Write a Python function called find_longest_string that takes a list of
# strings as an input and returns the longest string in the list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5836040
#


def find_longest_string(arr):
    longest = ""
    for i in range(0, len(arr)):
        longest = arr[i] if len(arr[i]) > len(longest) else longest
    return longest
