#Frog Jump

from typing import List

class Solution:
    def minCost(self, height: List[int]) -> int:
        n = len(height)
        
        # If there's only one stair, the cost is 0.
        if n == 1:
            return 0
            
        # Initialize costs for the first two stairs
        prev2 = 0                         # Cost to reach stair 0 (dp[0])
        prev1 = abs(height[1] - height[0]) # Cost to reach stair 1 (dp[1])
        
        # Iterate from the 3rd stair (index 2) to the end
        for i in range(2, n):
            # Cost via one-step jump (from i-1)
            cost_one_step = prev1 + abs(height[i] - height[i-1])
            
            # Cost via two-step jump (from i-2)
            cost_two_steps = prev2 + abs(height[i] - height[i-2])
            
            # The min cost to reach stair i
            current = min(cost_one_step, cost_two_steps)
            
            # Update pointers for the next iteration
            prev2 = prev1
            prev1 = current
            
        # The final answer is the min cost to reach the last stair (n-1)
        return prev1
    
# Time Complexity: O(n) where n is the number of stairs.
# Space Complexity: O(1) since we are using only a constant amount of extra space