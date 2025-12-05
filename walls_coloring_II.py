#Walls Coloring II
from typing import List
class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        if not costs or not costs[0]:
            return 0
            
        n = len(costs)
        k = len(costs[0])
        
        # Optimization: If there's more than 1 wall but only 1 color,
        # it's impossible to paint adjacent walls differently.
        if n > 1 and k == 1:
            return -1
        
        min1, min2 = float('inf'), float('inf')
        min1_idx = -1
        
        # Process first row
        for j in range(k):
            cost = costs[0][j]
            if cost < min1:
                min2 = min1
                min1 = cost
                min1_idx = j
            elif cost < min2:
                min2 = cost
                
        # Process remaining rows
        for i in range(1, n):
            curr_min1, curr_min2 = float('inf'), float('inf')
            curr_min1_idx = -1
            
            for j in range(k):
                if j == min1_idx:
                    current_cost = costs[i][j] + min2
                else:
                    current_cost = costs[i][j] + min1
                
                if current_cost < curr_min1:
                    curr_min2 = curr_min1
                    curr_min1 = current_cost
                    curr_min1_idx = j
                elif current_cost < curr_min2:
                    curr_min2 = current_cost
            
            min1, min2, min1_idx = curr_min1, curr_min2, curr_min1_idx
            
        # If min1 is still infinity, it means no solution exists
        return min1 if min1 != float('inf') else -1
    
# Time Complexity: O(n * k), where n is the number of walls and k is the number of colors.
# Space Complexity: O(1), since we only use a few variables for tracking minimums.