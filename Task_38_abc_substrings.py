"""
Used sliding window approach for this solution.

Track counts of a, b, c in the current window
and move the end pointer,updating character counts.

When all three characters are present, every substring ending at end and starting from start to end is valid.
Add len(s) - end to the result, then shrink the window by moving start.
"""
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