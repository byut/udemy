#
# DLL: Swap First and Last
#
# Swap the values of the first and last node
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5798320
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

    def swap_first_last(self):
        if not self.head or not self.tail:
            return False
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
        return True
