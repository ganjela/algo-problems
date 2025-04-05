"""
The number needed to reach the target is calculated.
If this complement is already in the dictionary, it means the two numbers that
add up to the target have been found, and their indices are returned.
Otherwise, the current number is added to the dictionary for future lookups.
"""

def two_sum(nums, target):

    num_dict = dict()
    for i, num in enumerate(nums):
        second_num = target - num
        if second_num in num_dict:
            return [i, num_dict[second_num]]
        else:
            num_dict[num] = i