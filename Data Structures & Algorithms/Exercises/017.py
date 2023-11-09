#
# LL: Partition List
#
# Implement the partitionList member function for the
# LinkedList class, which partitions the list such that all nodes
# with values less than x come before nodes with values greater
# than or equal to x.
#
# Note:  This linked list class does NOT have a tail which
# will make this method easier to implement.
#
# The original relative order of the nodes should be preserved.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5836830
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

    def partition_list(self, x):
        curr = self.head
        lchain = Node(0)
        gchain = Node(0)
        lnode = lchain
        gnode = gchain
        while curr:
            if curr.value < x:
                lnode.next = curr  # pyright: ignore
                lnode = curr
            else:
                gnode.next = curr  # pyright: ignore
                gnode = curr
            curr = curr.next
        gnode.next = None
        lnode.next = gchain.next
        self.head = lchain.next
