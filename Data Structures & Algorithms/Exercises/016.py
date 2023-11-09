#
# LL: Find Kth Node From End
#
# Implement the find_kth_from_end function, which takes
# the LinkedList (ll) and an integer k as input, and returns the
# k-th node from the end of the linked list WITHOUT USING
# LENGTH.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5795286
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


def find_kth_from_end(list, kth):
    slow = list.head
    fast = list.head
    for _ in range(kth):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow
