#
# Queue: Enqueue
#
# Implement the enqueue method for the Queue class that
# adds a new node with a given value to the end of the queue.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796256
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

    def enqueue(self, value):
        node = Node(value)
        if not self.last:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
        return True
