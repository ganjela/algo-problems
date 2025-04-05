"""
Standard binary search algorithm using while loop.
"""
def binary_search(list, target):
    l =  0
    r = len(list) - 1
    while l <= r:
        mid = (l + r) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1