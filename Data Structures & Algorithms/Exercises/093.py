#
# Selection Sort of LL
#
# Write a selection_sort() method in the LinkedList class that will sort the
# elements of a linked list in ascending order using the selection sort
# algorithm.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5834924
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

    def selection_sort(self):
        if self.length < 2:
            return
        current = self.head
        while current.next is not None:
            min_node = current
            node = current.next
            while node is not None:
                if node.value < min_node.value:
                    min_node = node
                node = node.next
            current.value, min_node.value = min_node.value, current.value
            current = current.next
