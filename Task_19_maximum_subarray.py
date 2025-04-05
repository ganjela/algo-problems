"""
This problem can be solved using nested for loops, but more efficient way is to
ignore negative prefixes that come before the current sum, because they don't
contribute to the max sum and consider only the positive ones.

For example, nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Iteration 1 - current_sum = max(1, -2 + 1) = 1`, max_sum = max(-2, 1) = 1
Iteration 3 - current_sum = max(4, 1 + 4) = 4`, max_sum = max(1, 4) = 4
Iteration 5- positive contributions like -1 + 4, +2, and +1 are accumulated.

The subarray [4, -1, 2, 1] produces the highest sum 6.
"""
def max_sub_array(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    length = len(nums)
    for i in range(1, length):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum