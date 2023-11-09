#
# LL: Remove Duplicates
#
# You are given a singly linked list that contains integer values,
# where some of these values may be duplicated.
#
# Your task is to implement a method called
# remove_duplicates() within the LinkedList class that
# removes all duplicate values from the list.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5793606
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

    def remove_duplicates(self):
        temp = self.head
        while temp:
            prev = temp
            curr = prev.next
            while curr:
                if curr.value is temp.value:
                    prev.next = curr.next
                    curr.next = None
                else:
                    prev = prev.next  # pyright: ignore
                curr = prev.next  # pyright: ignore
            temp = temp.next
