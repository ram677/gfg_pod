#Number of paths in a matrix with k coins

from typing import List

class Solution:
    def numberOfPath(self, mat: List[List[int]], k: int) -> int:
        n = len(mat)
        m = len(mat[0])
        
        # memo[r][c][k_left] stores the result for the subproblem
        # We use -1 to indicate "not computed yet"
        memo = [[[-1 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

        def solve(r, c, k_left):
            # 1. Base case: Out of bounds
            if r >= n or c >= m:
                return 0
            
            # 2. Calculate remaining coins needed
            coins_needed = k_left - mat[r][c]
            
            # 3. Pruning: If coins_needed is negative, this path is invalid
            if coins_needed < 0:
                return 0
            
            # 4. Base case: Reached the destination
            if r == n - 1 and c == m - 1:
                # Return 1 if we hit the target k exactly, 0 otherwise
                return 1 if coins_needed == 0 else 0
            
            # 5. Check memoization table
            if memo[r][c][k_left] != -1:
                return memo[r][c][k_left]
            
            # 6. Recursive calls for moving down and right
            paths_down = solve(r + 1, c, coins_needed)
            paths_right = solve(r, c + 1, coins_needed)
            
            # 7. Store result in memo and return
            memo[r][c][k_left] = paths_down + paths_right
            return memo[r][c][k_left]

        # Start the recursion from (0, 0) needing k coins in total
        return solve(0, 0, k)
    
# Time Complexity: O(n * m * k) where n is number of rows, m is number of columns, and k is the target coins.
# Space Complexity: O(n * m * k) for the memoization table and recursion stack.