"""
First, convert words list to set for O(1) look up.

After, in solution dp is used where we have to choose between minimum result
from choosing substring from i up to length of s and from skipping current character.

Base case of dp is when index reaches end of the string and returns 0.
"""
def find_min_extra_chars(s, dictionary):
    words = set(dictionary)
    cache = {}

    def rec(i):
        if i == len(s):
            return 0
        if i in cache:
            return cache[i]

        result = 1 + rec(i + 1)
        for j in range(i, len(s)):
            if s[i:j + 1] in words:
                result = min(result, rec(j + 1))
        cache[i] = result
        return result

    return rec(0)