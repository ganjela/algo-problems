"""
assuming that
Elements of "pushed" are unique.
And popped.length == pushed.length.

This function simulates pushing elements to the stack until a top of the stack
equals an element from the "popped" list.

If every element is popped from the stack, sequence is valid.
"""
def validate_stack_sequences(pushed, popped):
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and stack[-1] == popped[j]:
            j += 1
            stack.pop()
    return len(stack) == 0