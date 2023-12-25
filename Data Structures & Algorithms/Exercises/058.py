#
# HT: Group Anagrams
#
# You have been given an array of strings, where each string
# may contain only lowercase English letters. You need to write
# a function group_anagrams(strings) that groups the
# anagrams in the array together using a hash table (dictionary).
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5804402
#


def group_anagrams(arr):
    dict = {}
    for word in arr:
        key = "".join(sorted(word))
        if key not in dict:
            dict[key] = []
        dict[key].append(word)
    return [x for x in dict.values()]
