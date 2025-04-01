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