#
# Stack: Reverse String
#
# The reverse_string function takes a single parameter
# string, which is the string you want to reverse.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5800246
#


class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()


def reverse_string(string: str):
    stack = Stack()
    for char in string:
        stack.push(char)
    nstring = ""
    while len(stack.stack_list) != 0:
        nstring += stack.pop()  # type: ignore
    return nstring
