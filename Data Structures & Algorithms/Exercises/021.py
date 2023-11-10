#
# DLL: Constructor
#
# Design and implement a Python program that defines two
# classes: Node and DoublyLinkedList
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5794148
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
