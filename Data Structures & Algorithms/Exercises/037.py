#
# Queue: Constructor
#
# Create a Queue class that represents a first-in, first-out (FIFO)
# data structure using a linked list implementation.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796230
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


class Queue:
    def __init__(self, value):
        node = Node(value)
        self.first = node
        self.last = node
        self.length = 1
