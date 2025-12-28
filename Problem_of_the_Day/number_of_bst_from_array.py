#Number of BST From Array

from typing import List
class Solution:
    def countBSTs(self, arr: List[int]) -> List[int]:
        # Pre-calculated Catalan numbers: C_n is the number of BSTs with n nodes.
        # Since arr size is at most 6, the max subtree size is 5.
        catalan = [1, 1, 2, 5, 14, 42, 132] 
        
        n = len(arr)
        result = []
        
        # Iterate through each element, treating it as a potential root.
        for i in range(n):
            root_val = arr[i]
            
            left_count = 0
            right_count = 0
            
            # Partition the array based on the chosen root.
            for j in range(n):
                if arr[j] < root_val:
                    left_count += 1
                elif arr[j] > root_val:
                    right_count += 1
            
            # The number of ways to form the left subtree is C_{left_count}.
            num_left_subtrees = catalan[left_count]
            
            # The number of ways to form the right subtree is C_{right_count}.
            num_right_subtrees = catalan[right_count]
            
            # The total number of BSTs is the product of the possibilities.
            total_bsts = num_left_subtrees * num_right_subtrees
            result.append(total_bsts)
            
        return result
    
# Time Complexity: O(n^2) where n is the length of arr (due to nested loops).
# Space Complexity: O(1) since we use a fixed amount of extra space.