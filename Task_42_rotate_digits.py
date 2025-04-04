def count_valid_rotated_digits(n):
    map = {0: 0,
           1: 1,
           2: 5,
           5: 2,
           6: 9,
           8: 8,
           9: 6}

    count = 0
    for num in range(1, n + 1):
        temp = 0
        temp_num = num
        multiplier = 1
        valid = True
        while temp_num != 0:
            digit = temp_num % 10
            if digit in (3, 4, 7):
                valid = False
                break
            temp += map[digit] * multiplier
            multiplier *= 10
            temp_num //= 10
        if valid and temp != num:
            count += 1

    return count