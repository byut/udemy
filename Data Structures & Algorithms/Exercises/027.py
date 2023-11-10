#
# DLL: Set
#
# Implement the set_value method for the DoublyLinkedList
# class that updates the value of a node at a specific index in
# the list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5794420
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

    def set_value(self, index, value):
        if index < 0 or index >= self.length or not self.head:
            return False
        curr = self.head
        for _ in range(index):
            if curr.next:
                curr = curr.next
        curr.value = value
        return True
