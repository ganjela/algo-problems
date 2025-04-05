"""
To get the minimum waiting time, we need to exclude maximum query, so we sort the queries
and sum the execution times of all queries except the last one, because other queries won't wait for it in this way.
"""

def find_minimum_waiting_time(queries):
    queries.sort()
    time = 0
    result = 0
    for i in range(len(queries) - 1):
        time += queries[i]
        result += time

    return result