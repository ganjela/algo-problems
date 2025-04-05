"""
A BST is valid if,
the value of every node is greater than all values in its left subtree and
the value of every node is less than all values in its right subtree.

So, we are keeping track of min and max to compare value of current node with.
"""
def is_valid(root, min, max):
    if root is None:
        return True
    if root.value < min or root.value >= max:
        return False

    return (is_valid(root.left, min, root.value)
            and is_valid(root.right, root.value, max))