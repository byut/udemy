#
# Stack: Push
#
# Implement the push method for the Stack class that adds a
# new node with a given value to the top of the stack.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796196
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

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.height += 1
