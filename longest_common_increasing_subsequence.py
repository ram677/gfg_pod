#Longest Common Increasing Subsequence

from typing import List

class Solution:
    def LCIS(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        m = len(b)
        
        # dp[j] = length of LCIS of a[0...i] and b[0...j] which ends at b[j]
        dp = [0] * m
        
        for i in range(n):
            # Length of the LCIS ending before b[j] with a value < a[i]
            current_max_lcis = 0
            
            for j in range(m):
                
                # If a[i] and b[j] match, we can extend the
                # best-so-far subsequence.
                if a[i] == b[j]:
                    dp[j] = 1 + current_max_lcis
                
                # If a[i] is greater, b[j] is a potential
                # predecessor for a future match.
                if a[i] > b[j]:
                    current_max_lcis = max(current_max_lcis, dp[j])

        # The answer is the maximum value in the final dp table
        return max(dp) if dp else 0
    
# Time Complexity: O(n * m) where n and m are the lengths of arrays a and b.
# Space Complexity: O(m) for the dp array.