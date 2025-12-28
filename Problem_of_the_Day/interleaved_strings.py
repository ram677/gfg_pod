#Interleaved Strings

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        
        # Basic length check
        if n + m != l:
            return False
        
        # We use a 1D DP array to save space. 
        # dp[j] will represent dp[i][j] from the 2D logic.
        dp = [False] * (m + 1)
        
        # Base case: dp[0][0] is True
        dp[0] = True
        
        # Initialize the first row (using only s2)
        for j in range(1, m + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]
            
        # Iterate through s1 (rows)
        for i in range(1, n + 1):
            # Initialize the first column for this row (using only s1)
            # dp[0] currently holds the value for the previous row (i-1, 0)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            
            # Iterate through s2 (columns)
            for j in range(1, m + 1):
                # Option 1: Character comes from s1 (look up / current col in prev row)
                from_s1 = dp[j] and s1[i - 1] == s3[i + j - 1]
                
                # Option 2: Character comes from s2 (look left / prev col in current row)
                from_s2 = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                
                dp[j] = from_s1 or from_s2
                
        return dp[m]
    
# Time Complexity: O(n * m) where n and m are the lengths of s1 and s2 respectively.
# Space Complexity: O(m) for the DP array.