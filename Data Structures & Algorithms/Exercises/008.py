#
# LL: Pop First
#
# Implement the pop_first method for the LinkedList class.
#
# The pop_first method should remove the first node (the
# head) from the linked list, update the head attribute and the
# length attribute accordingly, and return the removed node.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793256
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
