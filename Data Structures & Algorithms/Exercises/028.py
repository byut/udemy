#
# DLL: Insert
#
# Implement the insert method for the DoublyLinkedList
# class that inserts a new node with a given value at a specific
# index in the list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5795144
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

    def append(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length or not self.head:
            return False
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            node = Node(value)
            prev: Node | None = None
            curr = self.head
            for _ in range(index):
                if curr.next:
                    prev = curr
                    curr = curr.next
            prev.next = node  # pyright: ignore
            node.prev = prev
            node.next = curr
            curr.prev = node
            self.length += 1
        return True
