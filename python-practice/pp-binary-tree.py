class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:  # value >= node.value
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp_val = self._find_min(node.right)
                node.value = temp_val
                node.right = self._delete_recursive(node.right, temp_val)
        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value
    
    def inorder_traversal(self):
        """Perform an in-order traversal of the tree and print node values."""
        self._inorder_helper(self.root)
        print()  # Newline for cleaner output
    
    def _inorder_helper(self, node):
        """Helper method for in-order traversal."""
        if node is not None:
            self._inorder_helper(node.left)
            print(node.value, end=' ')
            self._inorder_helper(node.right)

    def pre_order_traversal(self):
        self._pre_order_helper(self.root)
        print()

    def _pre_order_helper(self, node):
        if node:
            print(node.value, end=' ')
            self._pre_order_helper(node.left)
            self._pre_order_helper(node.right)

    def post_order_traversal(self):
        self._post_order_helper(self.root)
        print()

    def _post_order_helper(self, node):
        if node:
            self._post_order_helper(node.left)
            self._post_order_helper(node.right)
            print(node.value, end=' ')

# Example Usage
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(6)
bt.insert(8)

print("In-order Traversal:")
bt.inorder_traversal()  # Output: 5 3 2 4 7 6 8

print("Pre-order Traversal:")
bt.pre_order_traversal()  # Output: 5 3 2 4 7 6 8

print("Post-order Traversal:")
bt.post_order_traversal()  # Output: 2 4 3 6 8 7 5

if bt.search(4):
    print("Element 4 found in the tree")
else:
    print("Element 4 not found in the tree")

bt.delete(7)
print("After deleting 7:")
bt.pre_order_traversal()  # Output may vary based on the tree's structure after deletion