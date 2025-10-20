#BST to greater sum tree

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def transformTree(self, root):
        # We use an instance variable to maintain the running sum
        # across the recursive calls.
        self.current_sum = 0
        
        self._transform_helper(root)
        return root

    def _transform_helper(self, node):
        """
        Performs a reverse in-order traversal to update node values.
        """
        # Base case: do nothing for a null node.
        if not node:
            return

        # 1. Traverse the right subtree first (all larger values).
        self._transform_helper(node.right)
        
        # 2. Process the current node.
        # Store the original value before we modify it.
        original_value = node.data
        
        # The new value is the sum of all nodes visited so far (which are all greater).
        node.data = self.current_sum
        
        # Update the running sum by adding the original value of the current node.
        self.current_sum += original_value
        
        # 3. Traverse the left subtree (all smaller values).
        self._transform_helper(node.left)

# Time Complexity: O(N) where N is the number of nodes in the tree. Each node is visited exactly once.
# Space Complexity: O(H) due to the recursion stack in the worst case (unbalanced tree). In a balanced tree, the height H is log(N).