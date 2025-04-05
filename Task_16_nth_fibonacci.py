"""
This could be solved using recursion but more efficient way is to use dynamic programming,
where instead of storing values in the array, we store the previous two values.
"""
def find_nth_fibonacci(n):
    if n == 0:
        return 0
    a = 0
    b = 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b