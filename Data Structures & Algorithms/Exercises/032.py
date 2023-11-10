#
# DLL: Palindrome Checker
#
# Write a method to determine whether a given doubly linked
# list reads the same forwards and backwards.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5798536
#


class Node:
    def __init__(self, value):
        self.value = value
        self.prev: Node | None = None
        self.next: Node | None = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length = 1

    def is_palindrome(self):
        if not self.head or not self.tail:
            return True
        left = self.head
        right = self.tail
        while left and right and (left != right or left.prev != right.next):
            if left.value != right.value:
                return False
            left = left.next
            right = right.prev
        return True
