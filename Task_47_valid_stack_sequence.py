def validate_stack_sequences(pushed, popped):
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[j]:
            j += 1
            stack.pop()
    return len(stack) == 0