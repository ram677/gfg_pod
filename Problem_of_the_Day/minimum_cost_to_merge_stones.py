#Minimum Cost to Merge Stones

from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        
        # 1. Feasibility Check
        if (n - 1) % (k - 1) != 0:
            return -1
            
        # 2. Prefix Sums for O(1) range sum calculation
        # prefix_sum[i] will store sum of stones[0...i-1]
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + stones[i]
            
        # 3. Initialize DP table
        # dp[i][j] stores the min cost to merge stones[i...j] as much as possible
        dp = [[0] * n for _ in range(n)]
        
        # 4. Interval DP
        # Iterate over the length of the subarray from k to n
        for length in range(k, n + 1):
            # Iterate over the start index i
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                # Try splitting at mid.
                # mid moves in steps of (k-1) to ensure the left part [i...mid] 
                # can always resolve to exactly 1 pile.
                for mid in range(i, j, k - 1):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j])
                
                # If the current subarray can be merged into exactly 1 pile
                if (length - 1) % (k - 1) == 0:
                    current_sum = prefix_sum[j + 1] - prefix_sum[i]
                    dp[i][j] += current_sum
                    
        return dp[0][n - 1]
    
# Time Complexity: O(n^3 / k) due to the three nested loops, where n is the number of stones.
# Space Complexity: O(n^2) for the DP table.