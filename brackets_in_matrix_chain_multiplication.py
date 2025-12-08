#Brackets in Matrix Chain Multiplication

class Solution:
    def matrixChainOrder(self, arr):
        n = len(arr)
        # dp[i][j] stores the minimum number of multiplications 
        # needed to multiply matrices from index i to j.
        # Note: Matrices are 1-indexed (Matrix 1 to Matrix n-1).
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        # bracket[i][j] stores the optimal split index 'k'
        bracket = [[0 for _ in range(n)] for _ in range(n)]
        
        # L is the chain length
        for L in range(2, n):
            # i is the starting matrix index
            for i in range(1, n - L + 1):
                # j is the ending matrix index
                j = i + L - 1
                
                dp[i][j] = float('inf')
                
                # Try every possible split point k
                for k in range(i, j):
                    # Cost = cost(left) + cost(right) + cost(multiplication)
                    q = dp[i][k] + dp[k+1][j] + arr[i-1] * arr[k] * arr[j]
                    
                    if q < dp[i][j]:
                        dp[i][j] = q
                        bracket[i][j] = k
        
        # Helper function to construct the result string using the bracket table
        def construct_string(i, j):
            # Base case: single matrix
            if i == j:
                # Convert 1-based index to character (1->A, 2->B, etc.)
                return chr(ord('A') + i - 1)
            
            k = bracket[i][j]
            left = construct_string(i, k)
            right = construct_string(k + 1, j)
            
            return "(" + left + right + ")"
            
        return construct_string(1, n - 1)
    
# Time Complexity: O(n^3), where n is the number of matrices.
# Space Complexity: O(n^2), for the dp and bracket tables.