#
# LL: Remove
#
# Implement the remove method for the LinkedList class.
#
# The remove method should take an integer index as a
# parameter and remove the node at the specified index in the
# linked list, returning the removed node.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793390
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

    def pop(self):
        if not self.head:
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            node = self.tail
            temp = self.head
            while temp.next and temp.next is not node:
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.length -= 1
            return node

    def pop_first(self):
        if not self.head:
            return None
        node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            node.next = None
        self.length -= 1
        return node

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

    def remove(self, index):
        if index < 0:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        temp = self.get(index - 1)
        if temp and temp.next:
            node = temp.next
            temp.next = temp.next.next
            node.next = None
            return node
        return None
