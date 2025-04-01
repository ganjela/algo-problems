from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    num_set = set(nums)
    return len(num_set) < len(nums)