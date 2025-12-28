#Unique Paths in a Grid

class Solution:
    def uniquePaths(self, grid):
        n = len(grid)
        m = len(grid[0])
        
        dp = [0] * m

        if grid[0][0] == 0:
            dp[0] = 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dp[j] = 0
                else:
                    if j > 0:
                        dp[j] += dp[j - 1]

        return dp[m - 1]

#Time Complexity: O(n * m) where n is the number of rows and m is the number of columns
#Space Complexity: O(m) for the dp array