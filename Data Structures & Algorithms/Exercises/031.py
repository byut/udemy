#
# DLL: Reverse
#
# Create a new method called reverse that reverses the order
# of the nodes in the list, i.e., the first node becomes the last
# node, the second node becomes the second-to-last node,
# and so on.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5797480
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

    def reverse(self):
        if not self.head or self.head == self.tail:
            return True
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = curr.prev
            curr.prev = temp
            curr = temp
        temp = self.head
        self.head = self.tail
        self.tail = temp
        return True
