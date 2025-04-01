from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:

    num_dict = dict()
    for i, num in enumerate(nums):
        second_num = target - num
        if second_num in num_dict:
            return [i, num_dict[second_num]]
        else:
            num_dict[num] = i