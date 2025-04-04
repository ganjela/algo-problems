def calculate_number_of_squares(n):
    cache = [n] * (n + 1)
    cache[0] = 0
    count = 1
    while count * count <= n:
        square = count * count
        for i in range(square, n + 1):
            cache[i] = min(cache[i - square] + 1, cache[i])
        count += 1
    return cache[n]