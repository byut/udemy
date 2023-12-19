#
# Queue Using Stacks: Dequeue
#
# You have been tasked with implementing a queue data
# structure using two stacks in Python, and you need to write
# the dequeue method.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5840454
#


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def dequeue(self):
        if not len(self.stack1):
            return None
        else:
            return self.stack1.pop()
