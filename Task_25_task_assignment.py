def assign_tasks(k, tasks):
    indexed_tasks = []
    for i, task in enumerate(tasks):
        indexed_tasks.append((task, i))
    indexed_tasks.sort()
    result = []
    j = 0
    i = len(tasks) - 1
    while k > 0:
        result.append((indexed_tasks[j][1], indexed_tasks[i][1]))
        k -= 1
        i -= 1
        j += 1