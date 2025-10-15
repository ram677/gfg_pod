#k-th Smallest in BST

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def kthSmallest(self, root, k):
        # Use instance variables to track the count and the result
        # across recursive calls.
        self.count = k
        self.result = -1

        self.inorder_traversal(root)
        return self.result

    def inorder_traversal(self, node):
        # Base case or if we have already found the element.
        if not node or self.count == 0:
            return

        # 1. Traverse the left subtree.
        self.inorder_traversal(node.left)

        # After visiting the left subtree, this node is the next smallest.
        # Check if we have already found the result in the left subtree.
        if self.count == 0:
            return

        # 2. Visit the current node.
        self.count -= 1
        if self.count == 0:
            self.result = node.data
            return

        # 3. Traverse the right subtree.
        self.inorder_traversal(node.right)

# Time Complexity: O(H + k) where H is the height of the tree. In the worst case, we might have to traverse H nodes to reach the leftmost node and then k nodes to find the k-th smallest.
# Space Complexity: O(H) due to the recursion stack in the worst case (unbalanced tree). In a balanced tree, the height H is log(N).