#Sum of Nodes in BST Range

"""
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def nodeSum(self, root: 'Node', l: int, r: int) -> int:
        # Initialize the sum
        total_sum = 0
        
        # Use a stack for an iterative DFS approach
        stack = [root] if root else []
        
        while stack:
            # Pop the current node
            node = stack.pop()
            
            # If the node is None, continue (shouldn't happen with the initial check, but good practice)
            if node is None:
                continue
            
            # 1. Check if the current node's value is in the range [l, r]
            if l <= node.data <= r:
                total_sum += node.data
            
            # 2. Pruning the search using the BST property
            
            # If the node's value is GREATER than l, 
            # it means the left child MIGHT be in the range, so we should explore the left subtree.
            # If node.data < l, then the left child (which is even smaller) will also be < l, so we can prune the left subtree.
            if node.data > l and node.left:
                stack.append(node.left)
            
            # If the node's value is LESS than r, 
            # it means the right child MIGHT be in the range, so we should explore the right subtree.
            # If node.data > r, then the right child (which is even larger) will also be > r, so we can prune the right subtree.
            if node.data < r and node.right:
                stack.append(node.right)
                
        return total_sum
    
# Time Complexity: O(N) in the worst case where N is the number of nodes in the BST.
# In a balanced BST, the average time complexity is O(H + K) where H is the height of the tree and K is the number of nodes in the range [l, r].
# Space Complexity: O(H) where H is the height of the tree due to the stack used for DFS traversal.