#Minimum Cost to Cut a Stick of length N

from typing import List

class Solution:
    def minCutCost(self, n: int, cuts: List[int]) -> int:
        
        # 1. Augment the cuts array with the stick boundaries
        A = [0] + sorted(cuts) + [n]
        m = len(A)
        
        # 2. Initialize DP table
        # dp[i][j] = min cost to cut the stick from A[i] to A[j]
        # We use a dictionary for sparse storage (or a 2D array)
        dp = {}

        # We can solve this with a top-down recursive helper
        def solve(i, j):
            # i and j are indices into the augmented A array
            
            # 3. Base Case: If there are no cuts between i and j (j=i+1)
            if j <= i + 1:
                return 0
            
            # Check memoization
            if (i, j) in dp:
                return dp[(i, j)]
            
            # 4. Cost of the *first* cut on this piece
            current_stick_cost = A[j] - A[i]
            
            min_sub_cost = float('inf')
            
            # 5. Try every possible first cut 'k'
            for k in range(i + 1, j):
                min_sub_cost = min(min_sub_cost, solve(i, k) + solve(k, j))
                
            dp[(i, j)] = current_stick_cost + min_sub_cost
            return dp[(i, j)]

        # 6. Solve for the entire stick (from A[0] to A[m-1])
        return solve(0, m - 1) 

# Time Complexity: O(m^3) where m is the number of cuts + 2 (for the boundaries).
# Space Complexity: O(m^2) for the DP table.