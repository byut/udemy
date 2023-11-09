#
# LL: Reverse Between
#
# You are given a singly linked list and two integers
# start_index and end_index.
#
# Your task is to write a method reverse_between within the
# LinkedList class that reverses the nodes of the linked list
# from start_index to  end_index (inclusive using 0-based
# indexing) in one pass and in-place.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5836708
#


class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def reverse_between(self, start, end):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(start):
            if prev and prev.next:
                prev = prev.next
        curr = prev.next

        for _ in range(end - start):
            if curr and curr.next:
                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp

        self.head = dummy.next
