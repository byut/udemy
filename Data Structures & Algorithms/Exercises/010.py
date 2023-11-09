#
# LL: Set
#
# Implement the set_value method for the LinkedList class.
#
# The set_value method should take an integer index and a
# value as parameters and update the value of the node at the ]
# specified index in the linked list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793340
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

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        else:
            return False
