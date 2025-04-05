"""
Inorder - traverses the left subtree, then the root, and finally the right subtree.
Preorder - traverses the root first, then the left subtree, and finally the right subtree.
Postorder -traverses the left subtree, then the right subtree, and finally the root.
"""
def traverse_bst_inorder(root, traversed_values = []):
    if root:
        traverse_bst_inorder(root.left, traversed_values)

        traversed_values.append(root.value)

        traverse_bst_inorder(root.right, traversed_values)

    return traversed_values


def traverse_bst_preorder(root, traversed_values = []):
    if root:
        traversed_values.append(root.value)

        traverse_bst_inorder(root.left, traversed_values)

        traverse_bst_inorder(root.right, traversed_values)

    return traversed_values

def traverse_bst_postorder(root, traversed_values = []):
    if root:
        traverse_bst_inorder(root.left, traversed_values)

        traverse_bst_inorder(root.right, traversed_values)

        traversed_values.append(root.value)

    return traversed_values