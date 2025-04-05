"""
Create dict of last occurrences of each character.

Expand the current partition by updating end to the farthest last index of encountered characters.

When the current index reaches end it means partition is found.
"""
def partition_string(s):
    last_index = {}
    for i, char in enumerate(s):
        last_index[char] = i

    result = []
    length = 0
    end = 0

    for i, char in enumerate(s):
        length += 1
        end = max(end, last_index[char])

        if i == end:
            result.append(length)
            length = 0

    return result
