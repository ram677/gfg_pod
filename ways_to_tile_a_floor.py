#Ways To Tile A Floor

from typing import List

class Solution:
    def numberOfWays(self, n: int) -> int:
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # We use two variables to store the previous two values
        # in the sequence, similar to calculating Fibonacci.
        # 'a' will represent dp[i-2] and 'b' will represent dp[i-1].
        a = 1  # Corresponds to dp[1]
        b = 2  # Corresponds to dp[2]
        
        # Iterate from 3 up to n
        for _ in range(3, n + 1):
            # Calculate the current dp value
            current = a + b
            
            # Shift the pointers
            a = b
            b = current
            
        # 'b' will hold the final answer for dp[n]
        return b   

# Time Complexity: O(n) where n is the length of the floor.
# Space Complexity: O(1) since we are using only a constant amount of space.  
