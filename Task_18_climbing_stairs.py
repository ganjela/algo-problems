"""
    This problem is much like the fibonacci problem.

    But for base cases are 1 and 1 because we have one way to reach step 1 (By starting from there)
    and 1 way to reach step 2 (By starting from step 1 and going one step).

    And the relation to reach n steps is f(n) = f(n-1) + f(n-2).
"""
def climb_stairs(n):
    a = 1
    b = 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b