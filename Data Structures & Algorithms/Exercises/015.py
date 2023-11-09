#
# LL: Has Loop
#
# Write a method called has_loop that is part of the linked list
# class.
#
# The method should be able to detect if there is a cycle or loop
# present in the linked list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793574
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

    def has_loop(self):
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next  # pyright: ignore
            fast = fast.next.next
            if slow is fast:
                return True
        return False
