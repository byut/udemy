#
# LL: Reverse
#
# Implement the reverse method for the LinkedList class.
#
# The reverse method should reverse the order of the nodes in
# the linked list so that the head becomes the tail and the tail
# becomes the head.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793448
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

    def reverse(self):
        if not self.head:
            return
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before: Node | None = None
        while temp:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
