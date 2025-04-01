from typing import List

def max_sub_array(self, nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    length = len(nums)
    for i in range(1, length):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum