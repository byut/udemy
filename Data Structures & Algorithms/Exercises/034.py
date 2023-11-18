#
# Stack: Constructor
#
# Create a Stack class that represents a last-in, first-out
# (LIFO) data structure using a linked list implementation.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796182
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


class Stack:
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self.height = 1
