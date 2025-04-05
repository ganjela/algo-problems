"""
To get the optimal task assignment, which we will get if longest pair of tasks are minimal.
We need to sort tasks and pair maximum and minimum remaining tasks in the list.

for example: k = 2 and tasks = [1,2,3,4]

We could pair 1, 2 and 3,4 but we would get that the total time taken for work is 3 + 4 = 7.
which is not optimal. instead we should pair 1 - 4 and 2 - 3. which will give us 5 total hours.
"""
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