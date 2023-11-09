#
# LL: Get
#
# Implement the get method for the LinkedList class.
#
# The get method should take an integer index as a parameter
# and return a pointer to the node at the specified index in the
# linked list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793326
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
