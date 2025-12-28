#Chocolate Pickup II

from functools import lru_cache
from typing import List

class Solution:
    def chocolatePickup(self, mat: List[List[int]]) -> int:
        n = len(mat)

        # Use memoization to store results of subproblems
        # state: (r1, c1, r2)
        memo = {}

        def solve(r1, c1, r2):
            # Calculate c2 based on the "same step" rule
            c2 = r1 + c1 - r2

            # Check if this state is in memo
            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]

            # Base Case: Out of bounds
            if not (0 <= r1 < n and 0 <= c1 < n and 0 <= r2 < n and 0 <= c2 < n):
                return float('-inf')

            # Base Case: Blocked cell
            if mat[r1][c1] == -1 or mat[r2][c2] == -1:
                return float('-inf')

            # Base Case: Destination reached
            if r1 == n - 1 and c1 == n - 1:
                # (This implies r2 == n-1 and c2 == n-1 as well)
                return mat[r1][c1]

            # Calculate chocolates collected at this step
            chocolates = 0
            if r1 == r2: # Both robots on the same cell
                chocolates = mat[r1][c1]
            else: # Robots on different cells
                chocolates = mat[r1][c1] + mat[r2][c2]

            # Recursive calls for all 4 possible next moves
            res = chocolates + max(
                solve(r1 + 1, c1, r2 + 1),  # Down, Down
                solve(r1 + 1, c1, r2),      # Down, Right
                solve(r1, c1 + 1, r2 + 1),  # Right, Down
                solve(r1, c1 + 1, r2)       # Right, Right
            )

            memo[(r1, c1, r2)] = res
            return res

        # Start the DP from the beginning
        final_answer = solve(0, 0, 0)
        
        # If no path exists, solve() will return -inf. We must return 0.
        return max(0, final_answer)
    
# Time Complexity: O(n^3) where n is the number of rows (or columns) in the matrix.
# Space Complexity: O(n^3) for the memoization table and recursion stack.