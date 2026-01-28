#Count Subset With Target Sum II

from collections import Counter
from typing import List

class Solution:
    def countSubset(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        # Split the array into two halves
        mid = n // 2
        left_part = arr[:mid]
        right_part = arr[mid:]
        
        # Helper function to generate all subset sums for a given list
        def get_subset_sums(nums):
            sums = [0]
            for num in nums:
                # For every existing sum, add the current number to create new sums
                # We append these new sums to the list
                sums += [s + num for s in sums]
            return sums

        # 1. Generate all subset sums for the left half
        left_sums = get_subset_sums(left_part)
        
        # 2. Generate all subset sums for the right half
        right_sums = get_subset_sums(right_part)
        
        # 3. Store right sums frequencies in a hash map for O(1) lookup
        right_counts = Counter(right_sums)
        
        count = 0
        # 4. Iterate through left sums and look for the complement in right sums
        for s in left_sums:
            target = k - s
            if target in right_counts:
                count += right_counts[target]
                
        return count
    
# Time Complexity: O(2^(n/2)) due to generating all subset sums for both halves.
# Space Complexity: O(2^(n/2)) for storing the subset sums of both halves.