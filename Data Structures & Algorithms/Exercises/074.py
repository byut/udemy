#
# MinHeap: Sink Down
#
# Implement the _sink_down helper method in the MinHeap
# class
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5969846
#


class MinHeap:
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
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        min_index = index
        while min_index < len(self.heap):
            current = min_index
            if (
                self._left_child(current) < len(self.heap)
                and self.heap[min_index] > self.heap[self._left_child(current)]
            ):
                min_index = self._left_child(current)
            if (
                self._right_child(current) < len(self.heap)
                and self.heap[min_index] > self.heap[self._right_child(current)]
            ):
                min_index = self._right_child(current)
            if min_index != current:
                self._swap(min_index, current)
            else:
                break
