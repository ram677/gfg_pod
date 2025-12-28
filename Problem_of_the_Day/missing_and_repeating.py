#Missing And Repeating

class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        # Expected Sum and Sum of Squares for 1 to n
        # Use integer arithmetic to handle large numbers (Python does this automatically)
        expected_sum = (n * (n + 1)) // 2
        expected_sq_sum = (n * (n + 1) * (2 * n + 1)) // 6
        
        # Actual Sum and Sum of Squares from the array
        actual_sum = 0
        actual_sq_sum = 0
        
        for num in arr:
            actual_sum += num
            actual_sq_sum += num * num
            
        # Differences
        # val1 = R - M
        val1 = actual_sum - expected_sum
        
        # val2 = R^2 - M^2 = (R - M)(R + M)
        val2 = actual_sq_sum - expected_sq_sum
        
        # Calculate R + M
        # R + M = (R^2 - M^2) / (R - M)
        sum_RM = val2 // val1
        
        # Solve for R (Repeating) and M (Missing)
        # R = ( (R + M) + (R - M) ) / 2
        repeating = (sum_RM + val1) // 2
        
        # M = ( (R + M) - (R - M) ) / 2
        missing = (sum_RM - val1) // 2
        
        return [repeating, missing]
    
# Time Complexity: O(n), where n is the length of the array.
# Space Complexity: O(1), since we are using only a few extra variables.