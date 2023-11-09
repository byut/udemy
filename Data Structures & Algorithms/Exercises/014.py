#
# LL: Find Middle Node
#
# Implement the find_middle_node method for the LinkedList class.
#
# The find_middle_node method should return the middle
# node in the linked list WITHOUT using the length attribute.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793526
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

    def find_middle_node(self):
        if not self.head:
            return None
        elif not self.head.next:
            return self.head
        turtle = self.head
        rabbit = self.head
        while rabbit and rabbit.next:
            turtle = turtle.next  # pyright: ignore
            rabbit = rabbit.next.next
        return turtle
