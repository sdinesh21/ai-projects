class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:  # val > root.val
        root.right = insertIntoBST(root.right, val)
    
    return root

# Example usage
# Let's say we're starting with a BST with root value 4, and we want to insert 2 and 7.
root = TreeNode(4)
insertIntoBST(root, 2)
insertIntoBST(root, 7)

# This would modify the original tree to have 2 as the left child and 7 as the right child of the root 4.