#Optimal binary search tree

class Solution:
    def minCost(self, keys, freq):
        n = len(keys)
        
        # dp[i][j] stores the optimal cost for keys[i...j]
        # Size is n x n.
        dp = [[0] * n for _ in range(n)]
        
        # Precompute sum of frequencies for range [i, j]
        # freq_sum[i][j] = sum(freq[i...j])
        # This can also be done on the fly or using a 1D prefix sum array.
        # Let's use a simple 1D prefix sum for O(1) query.
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + freq[i]
            
        def get_sum(i, j):
            if i > j: return 0
            return prefix_sum[j+1] - prefix_sum[i]

        # Iterate over length of the sub-segment
        for length in range(1, n + 1):
            # Iterate over start index
            for i in range(n - length + 1):
                j = i + length - 1
                
                # Assume infinity initially
                dp[i][j] = float('inf')
                
                # The sum of frequencies for this range is constant regardless of the root
                current_range_sum = get_sum(i, j)
                
                # Try every key k in range [i, j] as the root
                for k in range(i, j + 1):
                    # Cost of left subtree
                    left_cost = dp[i][k-1] if k > i else 0
                    
                    # Cost of right subtree
                    right_cost = dp[k+1][j] if k < j else 0
                    
                    # Total cost = cost of children + current nodes pushed down 1 level
                    # Being pushed down 1 level effectively adds their sum one more time.
                    # Or simpler: Root is level 1 (adds sum once), children are level+1.
                    # Recursive step logic:
                    # Cost = left_cost + right_cost + current_range_sum
                    total = left_cost + right_cost + current_range_sum
                    
                    if total < dp[i][j]:
                        dp[i][j] = total
                        
        return dp[0][n-1]
    
# Time Complexity: O(n^3), where n is the number of keys.
# Space Complexity: O(n^2), for the dp table.