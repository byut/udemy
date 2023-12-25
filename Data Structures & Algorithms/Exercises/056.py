#
# HT: Find Duplicates
#
# Given an array of integers nums, find all the
# duplicates in the array using a hash table (dictionary).
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5804764
#


def find_duplicates(list):
    dict = {}
    for i in range(len(list)):
        if list[i] not in dict:
            dict[list[i]] = 0
        dict[list[i]] += 1
    return [k for k in dict if dict[k] > 1]
