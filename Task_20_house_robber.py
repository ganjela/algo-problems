from typing import List

def rob_house(nums: List[int]) -> int:
    a = 0
    b = 0
    for num in nums:
        a, b = b, max(a + num, b)

    return b