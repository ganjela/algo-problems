"""
We determine this by comparing the length of the list to the length of a
set created from the list (which removes duplicates).
"""
def contains_duplicate(nums):
    num_set = set(nums)
    return len(num_set) < len(nums)