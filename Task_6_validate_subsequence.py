def validate_subsequence(s: str, t: str) -> bool:
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