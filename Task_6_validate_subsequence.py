"""
A subsequence is derived by deleting some or no characters from `t` without changing
the order of the remaining characters. We check this by iterating through `t`.
"""
def validate_subsequence(s, t):
    len_s = len(s)
    if len_s > len(t):
        return False

    index_s = 0
    for char in t:
        if index_s == len_s:
            return True
        if s[index_s] == char:
            index_s += 1

    return index_s == len_s