def find_warmer_days(temperatures):
    length = len(temperatures)
    result = [0] * length
    stack = []

    for i, temperature in enumerate(temperatures):
        while stack and stack[-1][0] < temperature:
            stack_t, stack_i = stack.pop()
            result[stack_i] = i - stack_i
        stack.append((temperature, i))

    return result