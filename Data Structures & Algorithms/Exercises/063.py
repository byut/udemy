#
# Set: Find Pairs
#
# You are given two lists of integers, arr1 and arr2, and a
# target integer value, target. Your task is to find all pairs of
# numbers (one from arr1 and one from arr2) whose sum
# equals target.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5806176
#


def find_pairs(arr1, arr2, target):
    arr1 = set(arr1)
    pairs = []
    for num in arr2:
        if target - num in arr1:
            pairs.append((target - num, num))
    return pairs
