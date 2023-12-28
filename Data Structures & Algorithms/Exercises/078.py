#
# rBST: Insert
#
# Implement a recursive method called r_insert to insert
# value into a binary search tree (BST)
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5849594
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current, value):
        if current is None:
            current = Node(value)
        if value < current.value:
            current.left = self.__r_insert(current.left, value)
        elif value > current.value:
            current.right = self.__r_insert(current.right, value)
        return current

    def r_insert(self, value):
        self.root = self.__r_insert(self.root, value)
