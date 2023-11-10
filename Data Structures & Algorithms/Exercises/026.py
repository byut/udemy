#
# DLL: Get
#
# Implement the get method for the DoublyLinkedList class
# that retrieves a node at a specific index in the list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5794300
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

    def get(self, index):
        if index < 0 or index >= self.length or not self.head:
            return None
        curr = self.head
        for _ in range(index):
            if curr.next:
                curr = curr.next
        return curr
