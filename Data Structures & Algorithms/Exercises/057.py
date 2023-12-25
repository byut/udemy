#
# HT: First Non-Repeating Character
#
# Write a function called first_non_repeating_char(string)
# that finds the first non-repeating character in the given string.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5804368
#


def first_non_repeating_char(string: str):
    dict = {}
    order = []
    for char in string:
        if char not in dict:
            dict[char] = 0
            order.append(char)
        dict[char] += 1
    for char in order:
        if dict[char] == 1:
            return char
    return None
