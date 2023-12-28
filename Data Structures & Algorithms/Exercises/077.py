#
# rBST: Contains
#
# Implement the r_contains method of the
# BinarySearchTree class. This method should recursively
# search the binary search tree for a given value, starting from
# the root node, and return True if the value is found, and
# False otherwise.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5849590
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root: Node = None

    def __r_contains(self, current: Node, target):
        if current is None:
            return False
        if current.value == target:
            return True
        return self.__r_contains(current.left, target) or self.__r_contains(
            current.right, target
        )

    def r_contains(self, node):
        return self.__r_contains(self.root, node)
