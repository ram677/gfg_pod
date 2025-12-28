#Maximum Non-Adjacent Nodes Sum

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getMaxSum(self, root):
        
        def solve(node):
            """
            Returns a pair: (max_sum_including_node, max_sum_excluding_node)
            for the subtree rooted at 'node'.
            """
            # Base case: A null node contributes nothing.
            if not node:
                return (0, 0)

            # Recursively get sums from left and right children.
            left_included, left_excluded = solve(node.left)
            right_included, right_excluded = solve(node.right)
            
            # Case 1: We include the current node.
            # We must exclude its immediate children.
            sum_including_node = node.data + left_excluded + right_excluded
            
            # Case 2: We exclude the current node.
            # We can take the best possible sum from both children's subtrees.
            sum_excluding_node = max(left_included, left_excluded) + max(right_included, right_excluded)
            
            return (sum_including_node, sum_excluding_node)

        # The final answer is the best we can do starting from the root.
        included_root, excluded_root = solve(root)
        return max(included_root, excluded_root)
    
# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Space Complexity: O(H) where H is the height of the binary tree (due to recursion stack).