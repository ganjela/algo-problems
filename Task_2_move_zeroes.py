"""
Instead of moving zeroes to the end, we can move non-zero elements to the beginning of the list,
which will automatically moves zeros to the end.

So, if we encounter a non-zero element, we swap it with zero.
"""
def move_zeroes(nums):
    i = 0
    length = len(nums)
    for j in range(length):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1