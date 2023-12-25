#
# Set: Has Unique Chars
#
# Write a function called has_unique_chars that takes a
# string as input and returns True if all the characters in the
# string are unique, and False otherwise.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5806154
#


def has_unique_chars(string):
    return len(set(string)) == len(string)
