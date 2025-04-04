"""
If substring is palindrome, we add it to partitions list and when
we find valid palindrome substring, we recursively process the
remaining string.

Base case is when index reaches the end.
"""
def partition(s):

    length = len(s)
    result = []

    def find_partition(i, partitions_list):
        if i == length:
            result.append(partitions_list)
            return

        for j in range(i, length):
            if s[i:j+1] == s[i:j+1][::-1]:
                find_partition(j+1, partitions_list + [s[i:j+1]])

    find_partition(0, [])

    return result
