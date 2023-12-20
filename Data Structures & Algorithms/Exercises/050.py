#
# BST: Contains
#
# Implement the contains method for the BinarySearchTree
# class that checks if a node with a given value exists in the
# binary search tree.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796292
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while True:
            if value == temp.value:
                return True
            elif value < temp.value:
                if temp.left is None:
                    return False
                else:
                    temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    return False
                else:
                    temp = temp.right
