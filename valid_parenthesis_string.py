def check_valid_string(s):
    stack = []
    stars = []
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == '*':
            stars.append(i)
        else:
            if stack:
                stack.pop()
            elif stars:
                stars.pop()
            else:
                return False
    while stack and stars:
        if stack[-1] > stars[-1]:
            return False
        stack.pop()
        stars.pop()
    return not stack


print(check_valid_string("((*)"))
print(check_valid_string(")*("))
