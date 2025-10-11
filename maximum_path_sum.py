#Maximum path sum

import sys

'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxSum(self, root):
        # We use a list to hold the max_sum so it can be modified
        # by the nested function (acting like a reference or global variable).
        self.max_sum = -sys.maxsize - 1
        
        self.maxPathSumHelper(root)
        return self.max_sum

    def maxPathSumHelper(self, node):
        # Base case: A null node contributes 0 to the path sum.
        if not node:
            return 0
        
        # Recursively get the max path sum from left and right subtrees.
        # We take max with 0 to ignore negative path sums.
        left_gain = max(0, self.maxPathSumHelper(node.left))
        right_gain = max(0, self.maxPathSumHelper(node.right))
        
        # 1. Update the global maximum:
        # Calculate the max path sum with the current node as the "peak".
        current_path_sum = node.data + left_gain + right_gain
        self.max_sum = max(self.max_sum, current_path_sum)
        
        # 2. Return the maximum "gain" upwards to the parent:
        # A parent can only extend one branch, so we take the better one.
        return node.data + max(left_gain, right_gain)
    
# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Space Complexity: O(H) where H is the height of the binary tree (due to recursion stack).