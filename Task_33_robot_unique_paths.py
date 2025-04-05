"""
Robot has two choices for each move, either to go down or go right.

So, we are using dp to store unique paths.

Base case is 1.
"""

def calculate_unique_paths(m, n):
    current_row = [1] * n
    previous_row = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            current_row[j] = current_row[j - 1] + previous_row[j]
        current_row, previous_row = previous_row, current_row

    return previous_row[-1]