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