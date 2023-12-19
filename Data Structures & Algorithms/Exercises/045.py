#
# Stack: Sort Stack
#
# The sort_stack function takes a single argument, a Stack
# object. The function should sort the elements in the stack in
# ascending order (the lowest value will be at the top of the
# stack) using only one additional stack.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5799520
#


class Stack:
    def __init__(self):
        self.stack_list = []

    def peek(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list[len(self.stack_list) - 1]

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()


def sort_stack(stack: Stack):
    sorted_stack = Stack()
    while len(stack.stack_list):
        temp = stack.pop()
        while len(sorted_stack.stack_list) and sorted_stack.peek() > temp:  # type: ignore
            stack.push(sorted_stack.pop())
        sorted_stack.push(temp)
    while len(sorted_stack.stack_list):
        stack.push(sorted_stack.pop())
    return stack
