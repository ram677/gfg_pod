#Replace O's with X's

from typing import List

class Solution:
    def fill(self, grid: List[List[str]]):
        if not grid or not grid[0]:
            return grid
            
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # Boundary checks and base cases for recursion
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 'O':
                return
            
            # Mark the current cell as safe
            grid[r][c] = 'S'
            
            # Explore neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Start DFS from all 'O's on the vertical borders
        for r in range(rows):
            if grid[r][0] == 'O':
                dfs(r, 0)
            if grid[r][cols - 1] == 'O':
                dfs(r, cols - 1)
        
        # 2. Start DFS from all 'O's on the horizontal borders
        for c in range(cols):
            if grid[0][c] == 'O':
                dfs(0, c)
            if grid[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        # 3. Final sweep to flip the remaining 'O's and restore the safe 'S's
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'O':
                    grid[r][c] = 'X' # This 'O' is surrounded
                elif grid[r][c] == 'S':
                    grid[r][c] = 'O' # This was a safe 'O'
                    
        return grid
    
# Time Complexity: O(M * N) where M is the number of rows and N is the number of columns.
# Space Complexity: O(M * N) in the worst case for the recursion stack.