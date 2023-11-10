#
# DLL: Swap Nodes in Pairs
#
# You are given a doubly linked list.
#
# Implement a method called swap_pairs within the class
# that swaps the values of adjacent nodes in the linked list. The
# method should not take any input parameters.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5838944
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
        self.length = 1

    def swap_pairs(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while self.head and self.head.next:
            first = self.head
            second = self.head.next

            prev.next = second
            first.next = second.next
            second.next = first

            second.prev = prev
            first.prev = second

            if first.next:
                first.next.prev = first

            self.head = first.next
            prev = first

        self.head = dummy.next
        if self.head:
            self.head.prev = None
