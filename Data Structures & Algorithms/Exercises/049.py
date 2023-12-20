#
# BST: Insert
#
# Implement the insert method for the BinarySearchTree
# class that inserts a new node with a given value into the
# binary search tree.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796286
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value == temp.value:
                return False
            elif value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            elif value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
