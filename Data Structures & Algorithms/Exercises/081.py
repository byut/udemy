#
# Convert Sorted List to Balanced BST
#
# The task is to develop a method that takes a
# sorted list of integers as input and constructs
# a height-balanced BST.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/6221386
#


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = Node(nums[mid])
        node.left = self.__sorted_list_to_bst(nums, left, mid - 1)
        node.right = self.__sorted_list_to_bst(nums, mid + 1, right)
        return node
