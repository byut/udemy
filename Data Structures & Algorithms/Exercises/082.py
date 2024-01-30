#
# Invert Binary Tree
#
# Write a method to invert (or mirror) a binary tree. This means that for every
# node in the binary tree, you will swap its left and right children.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/6221378
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def invert(self):
        self.root = self.__invert_tree(self.root)

    def __invert_tree(self, node):
        if node is None:
            return None
        left, right = node.left, node.right
        node.left = self.__invert_tree(right)
        node.right = self.__invert_tree(left)
        return node
