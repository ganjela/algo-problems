def find_occurrences(nums, queries, x):
    occurrence = {}

    count_x = 0
    for i, num in enumerate(nums):
        if num == x:
            count_x += 1
            occurrence[count_x] = i

    result = []
    for q in queries:
        if q > count_x:
            result.append(-1)
        else:
            result.append(occurrence[q])
    return result
