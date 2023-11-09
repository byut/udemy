#
# LL: Insert
#
# Implement the insert method for the LinkedList class.
#
# The insert method should take an integer index and a value
# as parameters and insert a new node with the given value at
# the specified index in the linked list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793378
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

    def append(self, value):
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        if self.length == 0:
            self.tail = self.head
        self.length += 1
        return True

    def get(self, index):
        if index < 0:
            return None
        temp = self.head
        for _ in range(index):
            if temp:
                temp = temp.next
            else:
                return None
        return temp

    def insert(self, index, value):
        if index < 0:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        temp = self.get(index - 1)
        node = Node(value)
        if temp:
            node.next = temp.next
            temp.next = node
            self.length += 1
            return True
        return False
