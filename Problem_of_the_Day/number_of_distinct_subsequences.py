#Number of distinct subsequences

class Solution:
    def distinctSubseq(self, s):
        MOD = 10**9 + 7
        n = len(s)
        
        # dp[i] stores the number of distinct subsequences using the first i characters
        # Initialize with size n+1
        dp = [0] * (n + 1)
        
        # Base case: The empty subsequence
        dp[0] = 1
        
        # Dictionary to store the 1-based index of the last occurrence of each character
        last = {}
        
        for i in range(1, n + 1):
            char = s[i-1]
            
            # Step 1: Double the number of subsequences from the previous state
            dp[i] = (2 * dp[i-1]) % MOD
            
            # Step 2: If char has appeared before, remove duplicates
            if char in last:
                last_occurrence_index = last[char]
                # The duplicates correspond to the subsequences count just before 
                # the character's previous occurrence
                duplicates = dp[last_occurrence_index - 1]
                dp[i] = (dp[i] - duplicates + MOD) % MOD
            
            # Record the current index (1-based) as the last occurrence
            last[char] = i
            
        return dp[n]
    
# Time Complexity: O(n), where n is the length of the string.
# Space Complexity: O(n), for the dp array and the last occurrence dictionary.