"""
This problem can be easily solved using O(n^2) solution, but
more efficient way would be using stack which runs in O(n) time.

We push temperatures on to the stack paired with indices until a top temperature of the stack is
less than current temperature,which means we have found warmer day. And save days between these two days in result.

e.g, [73,74,75,71,69,72,76,73]

push 73 - stack: [(73, 0)]
check if 73 < 74, pop the stack, save the result.

push 74 - stack: [(74, 1)]
check if 74 < 75, pop the stack, save the result.

push 75 - stack: [(75, 2)]
check if 75 < 71, continue.

After this we push till we encounter 72.
[(75, 2), (71, 3), (69, 4)]

Then we encounter 72. Now, we start popping the stack.
69 < 72 save result.
71 < 72 save result.

75 < 72 not true in which case we continue
...

and if we have remaining temperatures in the stack it means there is no warmer day.
"""

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