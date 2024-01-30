#
# DFS InOrder
#
# Write a function called dfs_in_order that performs a
# Depth-First Search (DFS) traversal on a binary tree using the
# In-Order approach.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796194
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dfs_in_order(self):
        result = []

        def traverse(curr):
            if curr.left is not None:
                traverse(curr.left)
            result.append(curr.value)
            if curr.right is not None:
                traverse(curr.right)

        traverse(self.root)
        return result
