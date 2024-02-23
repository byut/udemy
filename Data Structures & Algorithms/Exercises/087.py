#
# Validate BST
#
# You are tasked with writing a method called is_valid_bst in the
# BinarySearchTree class that checks whether a binary search tree is a valid
# binary search tree.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5840648
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
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results

    def is_valid_bst(self):
        nodes = self.dfs_in_order()
        for i in range(len(nodes) - 1):
            if nodes[i] >= nodes[i + 1]:
                return False
        return True
