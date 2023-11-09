#
# LL: Pop
#
# Your task is to implement the pop method for the LinkedList
# class.
#
# The pop method should remove the last node (tail) from the
# linked list and return the removed node. If the list is empty,
# the method should return None.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793232
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
