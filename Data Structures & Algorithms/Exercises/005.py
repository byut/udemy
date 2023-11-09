#
# LL: Append
#
# Implement the append method for the LinkedList class.
#
# The append method should add a new node with a given
# value to the end of the linked list, updating the tail attribute
# and the length attribute accordingly.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793228
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

    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
