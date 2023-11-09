#
# LL: Binary to Decimal
#
# Your task is to implement the binary_to_decimal method
# for the LinkedList class. This method should convert a binary
# number, represented as a linked list, to its decimal equivalent.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5981018
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def binary_to_decimal(self):
        num = 0
        curr = self.head
        while curr:
            num = (num << 1) + curr.value
            curr = curr.next
        return num
