#
# Bubble Sort of a Linked List
#
# Write a bubble_sort() method in the LinkedList class
# that will sort the elements of a linked list in ascending order
# using the bubble sort algorithm.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5834922
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

    def bubble_sort(self):
        if self.length < 2:
            return
        dirty = True
        while dirty:
            dirty = False
            curr, next = self.head, self.head.next
            while next:
                if curr.value > next.value:
                    curr.value, next.value = next.value, curr.value
                    dirty = True
                curr, next = next, next.next
