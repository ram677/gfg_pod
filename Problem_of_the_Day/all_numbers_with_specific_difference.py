#All numbers with specific difference

class Solution:
    def getCount(self, n, d):
        # Helper function to calculate sum of digits
        def sum_digits(num):
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s
            
        # Binary Search to find the first number 'x' such that x - sum_digits(x) >= d
        low = 1
        high = n
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid satisfies the condition
            if mid - sum_digits(mid) >= d:
                ans = mid
                # If valid, try to find a smaller valid number
                high = mid - 1
            else:
                # If invalid, we need a larger number
                low = mid + 1
        
        # If no number satisfies the condition, return 0
        if ans == -1:
            return 0
            
        # All numbers from ans to n satisfy the condition
        return n - ans + 1
    
# Time Complexity: O(log n * log n) due to binary search and sum of digits calculation, where n is the input number.
# Space Complexity: O(1) as we are using only constant extra space for variables.