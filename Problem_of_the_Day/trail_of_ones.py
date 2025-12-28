#Trail of ones

class Solution:
    def countConsec(self, n: int) -> int:
        if n < 2:
            return 0
        
        # Initialize DP arrays
        a = [0] * (n + 1)  # ends with 0
        b = [0] * (n + 1)  # ends with 1

        a[1] = 1
        b[1] = 1

        for i in range(2, n + 1):
            a[i] = a[i-1] + b[i-1]
            b[i] = a[i-1]
        
        # Total strings with no consecutive 1s
        no_consec_ones = a[n] + b[n]
        
        # Total binary strings of length n = 2^n
        total = 1 << n  # same as 2 ** n
        
        # Result = total - no_consec_ones
        return total - no_consec_ones

#Time Complexity: O(n) where n is the length of the binary string.
#Space Complexity: O(n) for the DP arrays.