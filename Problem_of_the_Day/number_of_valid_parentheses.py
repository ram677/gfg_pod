#Number of Valid Parentheses

import math

class Solution:
    def findWays(self, n):
        # Valid parentheses must have an even length
        if n % 2 == 1:
            return 0
        
        k = n // 2
        
        # Calculate Catalan number using the direct factorial formula:
        # C_k = (2k)! / ((k + 1)! * k!)
        numerator = math.factorial(2 * k)
        denominator = math.factorial(k + 1) * math.factorial(k)
        
        return numerator // denominator
    
# Time Complexity: O(n) due to factorial calculations.
# Space Complexity: O(1) as we are using only a constant amount of extra space.