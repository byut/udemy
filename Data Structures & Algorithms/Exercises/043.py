#
# Stack: Parentheses Balanced
#
# Check to see if a string of parentheses is balanced or not.
#
# Exercise: https://ua.udemy.com/course/data-structures-algorithms-python/learn/quiz/5800144
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


def is_balanced_parentheses(parentheses):
    stack = Stack()
    for i in range(len(parentheses)):
        if parentheses[i] == "(":
            stack.push(0)
        elif parentheses[i] == ")":
            if len(stack.stack_list) > 0:
                stack.pop()
            else:
                return False
    return len(stack.stack_list) == 0
