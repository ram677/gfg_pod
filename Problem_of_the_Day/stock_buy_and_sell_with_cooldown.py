#Stock Buy and Sell with Cooldown

from typing import List
from itertools import accumulate
from bisect import bisect_left

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # Sort the array to enable binary search and efficient calculation
        nums.sort()
      
        # Create prefix sum array with initial 0 for easier indexing
        # prefix_sums[i] = sum of nums[0] to nums[i-1]
        prefix_sums = list(accumulate(nums, initial=0))
      
        result = []
      
        for target in queries:
            # Find the first index where nums[index] > target
            # All elements from this index need to be decreased to target
            right_index = bisect_left(nums, target + 1)
          
            # Calculate operations needed to decrease all elements > target
            # Sum of (nums[i] - target) for all i where nums[i] > target
            decrease_operations = (prefix_sums[-1] - prefix_sums[right_index]) - (len(nums) - right_index) * target
          
            # Find the first index where nums[index] >= target
            # All elements before this index need to be increased to target
            left_index = bisect_left(nums, target)
          
            # Calculate operations needed to increase all elements < target
            # Sum of (target - nums[i]) for all i where nums[i] < target
            increase_operations = target * left_index - prefix_sums[left_index]
          
            # Total operations is sum of increases and decreases
            total_operations = increase_operations + decrease_operations
            result.append(total_operations)
      
        return result
    
# Time Complexity: O(m log n) where m is the number of queries and n is the length of nums.
# Space Complexity: O(n) for the prefix sums array.