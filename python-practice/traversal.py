class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

inOrderresult = []
preOrderresult = []
postOrderresult = []

def inOrderTraversal(root):
    if root is None:
        return []
    inOrderTraversal(root.left)
    inOrderresult.append(root.value)
    inOrderTraversal(root.right)
    return inOrderresult

def preOrderTraversal(root):
    if root is None:
        return []
    preOrderresult.append(root.value)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    return preOrderresult

def postOrderTraversal(root):
    if root is None:
        return []
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    postOrderresult.append(root.value)
    return postOrderresult

# Create the tree
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3, TreeNode(5), TreeNode(6))

# Perform traversals
print("In-Order Traversal:", inOrderTraversal(root))  # Output: [4, 2, 1, 5, 3, 6]
print("Pre-Order Traversal:", preOrderTraversal(root))  # Output: [1, 2, 4, 3, 5, 6]
print("Post-Order Traversal:", postOrderTraversal(root))  # Output: [4, 2, 5, 6, 3, 1]
