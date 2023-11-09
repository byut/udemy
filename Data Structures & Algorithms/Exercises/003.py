#
# LL: Constructor
#
# You are tasked with implementing a basic data structure: a
# singly linked list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793222
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head: Node | None = node
        self.tail: Node | None = node
        self.length = 1
