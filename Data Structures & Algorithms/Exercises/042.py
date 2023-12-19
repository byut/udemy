#
# Stack: Pop for Stack That Uses List
#
# Add a method to pop a value from the Stack implementation
# that we began in the last two Coding Exercises.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5799376
#


class Stack:
    def __init__(self):
        self.stack_list = []

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()
