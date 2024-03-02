from stacksintro import Stack


def is_balanced(expression):
    stack = Stack()
    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty():
                return False
            top_char = stack.pop()
            if (top_char == '(' and char != ')') or \
                    (top_char == '[' and char != ']') or \
                    (top_char == '{' and char != '}'):
                return False
    return stack.is_empty()


print(is_balanced("({[]})"))
print(is_balanced("({[})"))
