#
# HT: Item In Common
#
# Write a function item_in_common(list1, list2) that
# takes two lists as input and returns True if there is at least
# one common item between the two lists, False otherwise.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796296
#


def item_in_common(list1, list2):
    dic = {}
    for i in range(len(list1)):
        if list1[i] not in dic:
            dic[list1[i]] = True
    for j in range(len(list2)):
        if list2[j] in dic:
            return True
    return False


item_in_common([1, 2, 3, 4, 5], [8, 9, 5])
