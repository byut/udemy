#
# DLL: Pop First
#
# Implement the pop_first method that removes the first
# node from the list and returns it.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5794294
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

    def pop_first(self):
        if not self.head:
            return None
        node = self.head
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
            node.next = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return node
