#Remove BST keys outside given range

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def removekeys(self, root, l, r):
        # Base case: If the current node is null, there's nothing to do.
        if not root:
            return None

        # If the node's value is too small, the entire left subtree is also too small.
        # The correct tree must be the trimmed version of the right subtree.
        if root.data < l:
            return self.removekeys(root.right, l, r)

        # If the node's value is too large, the entire right subtree is also too large.
        # The correct tree must be the trimmed version of the left subtree.
        if root.data > r:
            return self.removekeys(root.left, l, r)

        # If the node's value is within the range, it's a keeper.
        # We recursively trim its left and right children.
        root.left = self.removekeys(root.left, l, r)
        root.right = self.removekeys(root.right, l, r)
        
        # Return the valid node.
        return root
    
# Time Complexity: O(N) where N is the number of nodes in the tree. In the worst case, we might have to visit all nodes.
# Space Complexity: O(H) due to the recursion stack in the worst case (unbalanced tree). In a balanced tree, the height H is log(N).