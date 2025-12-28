#Wildcard Pattern Matching

class Solution:
    def wildCard(self, txt, pat):
        n = len(txt)
        m = len(pat)
        
        # dp[i][j] stores whether txt[:i] matches pat[:j]
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        
        # Base case: Empty text matches empty pattern
        dp[0][0] = True
        
        # Base case: Empty text matches pattern only if pattern starts with '*'
        for j in range(1, m + 1):
            if pat[j-1] == '*':
                dp[0][j] = dp[0][j-1]
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # If characters match or pattern has '?', inherit from diagonal
                if pat[j-1] == txt[i-1] or pat[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                
                # If pattern has '*', look left (match 0) or look up (match 1+)
                elif pat[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                
                # Else, it's a mismatch
                else:
                    dp[i][j] = False
                    
        return dp[n][m]
    
# Time Complexity: O(n * m) where n and m are the lengths of txt and pat respectively.
# Space Complexity: O(n * m) for the DP table.