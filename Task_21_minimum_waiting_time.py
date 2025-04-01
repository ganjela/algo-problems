def find_minimum_waiting_time(queries):
    queries.sort()
    time = 0
    result = 0
    for i in range(len(queries) - 1):
        time += queries[i]
        result += time

    return result