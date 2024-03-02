from stacksintro import Stack


def decimal_to_binary(decimal):
    stack = Stack()
    while decimal > 0:
        remainder = decimal % 2
        stack.push(remainder)
        decimal //= 2
    binary = ''
    while not stack.is_empty():
        binary += str(stack.pop())
    return binary


print(decimal_to_binary(10))
print(decimal_to_binary(21))
