#Travelling Salesman Problem

import sys

class Solution:
    def tsp(self, cost):
        n = len(cost)
        
        # Memoization table: (mask, current_city) -> min_cost
        # Mask ranges from 0 to 2^n - 1
        # current_city ranges from 0 to n - 1
        memo = {}
        
        # ALL_VISITED is a mask with all n bits set to 1
        ALL_VISITED = (1 << n) - 1
        
        def solve(mask, pos):
            # Base Case: If all cities have been visited
            if mask == ALL_VISITED:
                # Return cost to go back to start (city 0)
                return cost[pos][0]
            
            # Check memoization table
            state = (mask, pos)
            if state in memo:
                return memo[state]
            
            min_cost = float('inf')
            
            # Try to visit every other city
            for city in range(n):
                # If city is not visited yet (check if bit is 0)
                if (mask & (1 << city)) == 0:
                    new_cost = cost[pos][city] + solve(mask | (1 << city), city)
                    if new_cost < min_cost:
                        min_cost = new_cost
            
            memo[state] = min_cost
            return min_cost

        # Start from city 0, with mask indicating city 0 is visited (bit 0 set)
        return solve(1, 0)
    
# Time Complexity: O(n^2 * 2^n), where n is the number of cities.
# Space Complexity: O(n * 2^n), for memoization table.