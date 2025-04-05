from collections import defaultdict

"""
Anagram is valid if both strings have same characters with same counts.
"""
def is_anagram(s, t):
    sdict = defaultdict(int)
    tdict = defaultdict(int)

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        sdict[s[i]] += 1
        tdict[t[i]] += 1

    return sdict == tdict