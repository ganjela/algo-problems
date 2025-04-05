"""
Using two sets to track unique and non-unique characters and return
the index of the first character that appears only once. If no unique character
exists, it returns -1.
"""
def find_first_unique_character(s):
    uniques = set()
    not_uniques = set()
    l = []

    for i, char in enumerate(s):
        if char in not_uniques:
            if char in uniques:
                uniques.remove(char)
        else:
            uniques.add(char)
            not_uniques.add(char)
            l.append((char, i))

    for char, i in l:
        if char in uniques:
            return i
    return -1