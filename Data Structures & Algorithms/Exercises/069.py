#
# Heap: Insert
#
# Your task is to implement the insert method.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5923288
#


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        index = len(self.heap) - 1
        while index > 0 and self.heap[self._parent(index)] < self.heap[index]:
            self._swap(self._parent(index), index)
            index = self._parent(index)
