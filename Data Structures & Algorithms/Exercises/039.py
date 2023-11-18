#
# Queue: Dequeue
#
# Implement the dequeue method for the Queue class that
# removes the first node from the queue and returns it.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5796266
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

    def dequeue(self):
        if not self.first:
            return None
        node = self.first
        if self.first is self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            node.next = None
        self.length -= 1
        return node
