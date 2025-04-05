"""
We calculate the miles balance at each city by subtracting the
distance from the fuel available (converted to miles using mpg).

We track a running total of the miles balance:
If the total drops below zero, it means the route starting from the current
starting city is not possible.

So, we reset the total to 0 and update the starting city to the next one i + 1.

Assuming that the solution exists, if we reach the end of the list without
resetting the total, then the solution must be valid.
"""
def find_valid_starting_city(distances, fuel, mpg):
    n = len(distances)
    total = 0
    starting_city = 0

    for i in range(n):
        miles = (fuel[i] * mpg) - distances[i]
        total += miles

        if total < 0:
            total = 0
            starting_city = i + 1

    return starting_city