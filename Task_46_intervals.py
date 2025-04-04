def find_closest_right_interval(intervals):
    result = []
    for i in range(len(intervals)):
        result.append(get_right_interval(i, intervals[i][1], intervals))
    return result


def get_right_interval(index, end, intervals):
    result = -1
    closest = float('inf')
    for i in range(len(intervals)):
        if i == index:
            continue
        start = intervals[i][0]
        if end <= start < closest:
            closest = start
            result = i
    return result