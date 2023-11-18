#
# Stack: Pop
#
# Implement the pop method for the Stack class that removes
# the top node from the stack and returns it.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796218
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

    def pop(self):
        if not self.top:
            return None
        node = self.top
        self.top = self.top.next
        self.height -= 1
        node.next = None
        return node
