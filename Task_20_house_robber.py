"""
Robber can't rob two adjacent houses at the same time. So, he has two choose between
Robbing the first house or skipping and robbing the second house.
"""
def rob_house(nums):
    a = 0
    b = 0
    for num in nums:
        a, b = b, max(a + num, b)

    return b