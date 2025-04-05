"""
O(n^2) solution.

For each interval end, find closest greater or equal interval start in the right part of the intervals list,
by iterating through the list.
"""

def find_closest_right_interval(intervals):
    result = []
    for i in range(len(intervals)):
        result.append(get_right_interval(i, intervals[i][1], intervals))
    return result


def get_right_interval(index, end, intervals):
    """helper function to get right closest start index"""
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