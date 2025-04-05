"""
To check each if each number is valid we get every digit of a number.
and check if the digit is equal to 3, 4 or 7 because they can not be rotated,
so we set flag to False, break the while loop and don't increase count.

On the other hand, if digit is equal to 2, 5, 6, or 9 it means that a number
is valid because after rotation it will be different from the original.
"""
def count_valid_rotated_digits(n):
    count = 0
    for num in range(1, n + 1):
        temp_num = num
        valid = False
        while temp_num > 0:
            digit = temp_num % 10
            if digit in (3, 4, 7):
                valid = False
                break
            if digit in (2, 5, 6, 9):
                valid = True
            temp_num //= 10
        if valid:
            count += 1
    return count