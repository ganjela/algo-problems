MINIMUM = float('-inf')
def find_three_largest_numbers(numbers):
    largest_nums = [MINIMUM] * 3
    minimum = min(largest_nums)
    for num in numbers:
        if len(largest_nums) <= 3 and num > minimum:
            largest_nums.remove(minimum)
            largest_nums.append(num)
            minimum = min(largest_nums)

    largest_nums.sort()