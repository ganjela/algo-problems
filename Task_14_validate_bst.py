def is_valid(root, min, max):
    if root is None:
        return True
    if root.value < min or root.value >= max:
        return False

    return (is_valid(root.left, min, root.value)
            and is_valid(root.right, root.value, max))