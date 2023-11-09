#
# LL: Prepend
#
# Implement the prepend method for the LinkedList class.
#
# The prepend method should add a new node with a given
# value to the beginning of the linked list, updating the head
# attribute and the length attribute accordingly.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793234
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head: Node | None = new_node
        self.tail: Node | None = new_node
        self.length = 1

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.length == 0:
            self.tail = self.head
        self.length += 1
