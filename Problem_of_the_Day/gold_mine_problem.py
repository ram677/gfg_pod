#Gold Mine Problem

class Solution:
    def maxGold(self, mat):
        if not mat or not mat[0]:
            return 0

        n = len(mat)      # number of rows
        m = len(mat[0])   # number of columns

        # Create a DP table initialized with 0
        dp = [[0] * m for _ in range(n)]

        # Fill the last column of dp with the gold values from mat
        for i in range(n):
            dp[i][m-1] = mat[i][m-1]

        # Fill the dp table from second last column to the first
        for j in range(m-2, -1, -1):
            for i in range(n):
                # Check the possible moves
                right = dp[i][j+1]
                right_up = dp[i-1][j+1] if i > 0 else 0
                right_down = dp[i+1][j+1] if i < n-1 else 0

                # Update dp[i][j]
                dp[i][j] = mat[i][j] + max(right, right_up, right_down)

        # Find the maximum value in the first column
        max_gold = max(dp[i][0] for i in range(n))
        return max_gold

#Time Complexity: O(n * m) where n is the number of rows and m is the number of columns.
#Space Complexity: O(n * m) for the DP table.