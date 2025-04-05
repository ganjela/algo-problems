"""
At first, we are tempted to try greedy approach in which case we quickly
discover that it is not valid solution for the problem. For example:

n = 12
if we choose closest square number to n, we get:
n = 3^3 + 1 + 1 + 1 this means we need to use 4 numbers.
Instead, we could write n = 2^2 + 2^2 + 2^2 in which case
we are using only 3 numbers.

The solution for this problem is written using bottom up dp approach,
where we are choosing minimum between current number of squares and
the solution for remaining n plus one for the current square.

"""

def calculate_number_of_squares(n):
    cache = [float('inf')] * (n + 1)
    cache[0] = 0
    count = 1
    while count * count <= n:
        square = count * count
        for i in range(square, n + 1):
            cache[i] = min(cache[i - square] + 1, cache[i])
        count += 1
    return cache[n]