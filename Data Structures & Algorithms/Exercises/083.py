#
# BFS (Breadth First Search)
#
# Write a function called BFS that performs a Breadth-First Search
# traversal on a binary tree.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796224
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def BFS(self):
        if self.root is None:
            return []
        result = []
        queue = [self.root]
        while queue:
            curr: Node = queue.pop(0)
            result.append(curr.value)
            if curr.left is not None and curr.left not in queue:
                queue.append(curr.left)
            if curr.right is not None and curr.right not in queue:
                queue.append(curr.right)
        return result
