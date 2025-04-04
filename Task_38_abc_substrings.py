def calculate_number_of_substrings(s):
    start = 0
    char_count = [0, 0, 0]
    count = 0

    for end in range(len(s)):
        char_count[ord(s[end]) - ord('a')] += 1

        while char_count[0] > 0 and char_count[1] > 0 and char_count[2] > 0:
            count += len(s) - end
            char_count[ord(s[start]) - ord('a')] -= 1
            start += 1

    return count