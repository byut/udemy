#
# DLL: Remove
#
# Implement the remove method for the DoublyLinkedList
# class that removes a node at a specific index in the list and
# returns it.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5795154
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

    def get(self, index):
        if index < 0 or index >= self.length or not self.head:
            return None
        curr = self.head
        for _ in range(index):
            if curr.next:
                curr = curr.next
        return curr

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            node = self.get(index)
            if not node:
                return None
            prev = node.prev
            next = node.next
            node.next = None
            node.prev = None
            prev.next = next  # pyright: ignore
            next.prev = prev  # pyright: ignore
            self.length -= 1
            return node
