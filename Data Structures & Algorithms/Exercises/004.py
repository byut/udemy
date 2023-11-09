#
# LL: Print List
#
# Implement a method print_list(self) that prints the
# linked list's elements, one per line.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5858220
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

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
