#
# Insertion Sort of LL
#
# Write an insertion_sort() method in the LinkedList class that will sort the
# elements of a linked list in ascending order using the insertion sort
# algorithm.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5808958
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

    def insertion_sort(self):
        if self.length < 2:
            return

        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None

        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next

            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current
            else:
                search_pointer = sorted_list_head
                while (
                    search_pointer.next is not None
                    and current.value > search_pointer.next.value
                ):
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current

        self.head = sorted_list_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        self.tail = temp
