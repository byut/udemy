#
# Queue Using Stacks: Enqueue
#
# You are given a class MyQueue which implements a queue
# using two stacks. Your task is to implement the enqueue
# method which should add an element to the back of the
# queue.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5840442
#


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, value):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1 = [value]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
