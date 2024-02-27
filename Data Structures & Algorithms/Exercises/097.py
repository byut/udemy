#
# Merge Two Sorted LL
#
# The merge method takes in another LinkedList as an input and merges it with
# the current LinkedList.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5835856
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def merge(self, other_list):
        other_head = other_list.head
        dummy = Node(0)
        current = dummy

        while self.head is not None and other_head is not None:
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_head
                other_head = other_head.next
            current = current.next

        if self.head is not None:
            current.next = self.head
        else:
            current.next = other_head
            self.tail = other_list.tail

        self.head = dummy.next
        self.length += other_list.length
