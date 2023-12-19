#
# Stack: Push for Stack That Uses List
#
# Add a method to push a value onto the Stack
# implementation that we began in the last Coding Exercise.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5799374
#


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)
