#
# BST: Minimum Value
#
# Implement a method called min_value that finds and
# returns the minimum value in a binary search tree (BST)
# starting from a given node.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5849598
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def min_value(self, current_node):
        while current_node.left:
            current_node = current_node.left
        return current_node.value
