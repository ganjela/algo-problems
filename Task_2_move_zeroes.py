from typing import List
def move_zeroes(nums: List[int]) -> None:
    i = 0
    length = len(nums)
    for j in range(length):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1