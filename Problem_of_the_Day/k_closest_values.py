#K closest Values

import bisect
from typing import List

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getKClosest(self, root, target, k):
        # Step 1: Perform in-order traversal to get a sorted list of values.
        inorder_list = []
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            inorder_list.append(node.data)
            traverse(node.right)
        
        traverse(root)
        
        n = len(inorder_list)
        if k == n:
            return inorder_list

        # Step 2: Find the starting point for the two-pointer search.
        # 'right' will be the index of the first element >= target.
        right = bisect.bisect_left(inorder_list, target)
        left = right - 1
        
        result = []
        
        # Step 3: Use two pointers to expand outwards and find the k closest elements.
        while len(result) < k:
            # Handle cases where one pointer goes out of bounds.
            if left < 0:
                result.append(inorder_list[right])
                right += 1
            elif right >= n:
                result.append(inorder_list[left])
                left -= 1
            # Compare the elements at both pointers.
            elif abs(inorder_list[left] - target) <= abs(inorder_list[right] - target):
                # The left element is closer or equally close.
                # The '<=' handles the tie-breaker correctly by choosing the smaller value (left).
                result.append(inorder_list[left])
                left -= 1
            else:
                # The right element is closer.
                result.append(inorder_list[right])
                right += 1
                
        return result
    
# Time Complexity: O(N) where N is the number of nodes in the BST.
# Space Complexity: O(N) for storing the inorder traversal list.