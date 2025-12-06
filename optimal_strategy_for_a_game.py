#Optimal Strategy For A Game

class Solution:
    def maximumAmount(self, arr):
        n = len(arr)
        # dp[i] stores the maximum margin (my_score - opp_score) 
        # for the current subarray length.
        # Initially (length 1), the margin is just the value of the coin itself.
        dp = list(arr)
        
        # Iterate over 'gap' (length of the subarray - 1)
        # We start from gap=1 (length 2) up to n-1
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                
                # Option 1: Pick left coin (arr[i])
                # Subtract the opponent's best margin from the remaining range [i+1...j]
                # Note: dp[i+1] currently holds the result for range [i+1...j]
                pick_left = arr[i] - dp[i+1]
                
                # Option 2: Pick right coin (arr[j])
                # Subtract the opponent's best margin from the remaining range [i...j-1]
                # Note: dp[i] currently holds the result for range [i...j-1]
                pick_right = arr[j] - dp[i]
                
                # Update dp[i] with the maximum of the two options
                if pick_left > pick_right:
                    dp[i] = pick_left
                else:
                    dp[i] = pick_right
                    
        # The final answer is derived from the total sum and the max margin
        total_sum = sum(arr)
        return (total_sum + dp[0]) // 2
    
# Time Complexity: O(n^2), where n is the number of coins.
# Space Complexity: O(n), for the dp array.