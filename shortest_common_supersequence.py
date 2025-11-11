#Shortest Common Supersequence

from typing import List

class Solution:
    def minSuperSeq(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        
        # dp[i][j] will store the length of the LCS of
        # s1[0...i-1] and s2[0...j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the DP table to find the length of the LCS
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    # Characters match
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Characters don't match
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the LCS is in the bottom-right corner
        lcs_length = dp[m][n]
        
        # Apply the formula for the Shortest Common Supersequence
        return m + n - lcs_length

# Time Complexity: O(m * n) where m and n are the lengths of s1 and s2 respectively.
# Space Complexity: O(m * n) for the DP table.