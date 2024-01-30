#
# DFS PostOrder
#
# Write a function called dfs_post_order that performs a Depth-
# First Search (DFS) traversal on a binary tree using the Post-Order
# approach
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5803352
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def dfs_post_order(self):
        result = []

        def traverse(curr):
            if curr.left is not None:
                traverse(curr.left)
            if curr.right is not None:
                traverse(curr.right)
            result.append(curr.value)

        traverse(self.root)
        return result
