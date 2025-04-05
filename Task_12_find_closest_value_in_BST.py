
"""
Iteratively traversing the tree, comparing node values with the target to determine the closest value.
"""
def find_closest_value_in_bst(root, target):

    closest = float('inf')
    result = root.value

    while root:
        if abs(root.value - target) < closest:
            closest = abs(root.value - target)
            result = root.value

        if root.value > target:
            root = root.left
        elif root.value < target:
            root = root.right
        else:
            return root.value

    return result