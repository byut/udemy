#
# BST: Constructor
#
# Create a BinarySearchTree class. The BinarySearchTree class should have an
# __init__ method that initializes an empty binary
# search tree.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796272
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
