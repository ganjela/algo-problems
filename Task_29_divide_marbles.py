"""
If we have list [1, 2, 3, 4, 5] and k = 2, then we have to split after 1 for minimum score and after 4 for maximum score:

min score - [1 | 2, 3, 4, 5] here in each sublist the cost is first element + last element, so the score for the first sublist is 1 + 1 = 2
and for the second sublist is 2 + 5 = 7. 7 + 2 = 9

max score - [1, 2, 3, 4 | 5] score for the first sublist is 1 + 4 = 5
and for the second sublist is 5 + 5 = 10. 10 + 5 = 15

first and last elements can be ignored because when subtracting max_score - min_score they cancel each other out.

So, we care for the adjacent values after the splits, because they are the ones that will contribute to the final score:

[1 ,2, 3, 4, 5] k = 3 max score -> [1, 2, 3 | 4 | 5] 5 + 4 + 4 + 3 = 16
min score -> [1 | 2 | 3, 4, 5] 1 + 2 + 2 + 3 = 8

However, list might not be sorted so we firstly calculate values of adjacent sublists and then sort them.
In this way we will easily choose maximum and minimum values.
"""
def divide_marbles(k, weights):
    if k == 1:
        return 0
    splits = []

    for i in range(len(weights) - 1):
        splits.append(weights[i] + weights[i + 1])

    splits.sort()

    i = k - 1

    max_score = sum(splits[-i:])
    min_score = sum(splits[:i])
    return max_score - min_score