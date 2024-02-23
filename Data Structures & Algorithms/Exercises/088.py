#
# Kth Smallest Node
#
# Given a binary search tree, find the kth smallest element in the tree.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5801020
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def kth_smallest(self, k):
        stack = []
        curr = self.root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.value

            curr = curr.right

        return None
