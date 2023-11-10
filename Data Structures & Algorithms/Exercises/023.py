#
# DLL: Pop
#
# Further extend the DoublyLinkedList class by adding a pop
# method that removes the last node from the list and returns
# it.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5794184
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

    def pop(self):
        if not self.tail:
            return None
        node = self.tail
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return node
