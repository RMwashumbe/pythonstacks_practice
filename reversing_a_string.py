from stacksintro import Stack


def reverse_string(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()
    return


print(reverse_string("hello"))
