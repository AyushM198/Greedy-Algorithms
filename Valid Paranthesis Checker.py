def is_valid_parentheses(s):
    # Dictionary to hold matching pairs
    matching_parenthesis = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in matching_parenthesis.values():
            # Push the opening parenthesis onto the stack
            stack.append(char)
        elif char in matching_parenthesis:
            # If the stack is empty or top of the stack does not match
            if not stack or stack[-1] != matching_parenthesis[char]:
                return False
            # Pop the top of the stack
            stack.pop()

    # If the stack is empty, all opening parentheses were matched
    return not stack


# Example usage
print(is_valid_parentheses("()"))  # True
print(is_valid_parentheses("()[]{}"))  # True
print(is_valid_parentheses("(]"))  # False
print(is_valid_parentheses("([)]"))  # False
print(is_valid_parentheses("{[]}"))  # True
