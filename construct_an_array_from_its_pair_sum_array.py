#Construct an array from its pair-sum array

class Solution:
    def constructArr(self, arr):
        m = len(arr)
        
        # Find n using quadratic formula
        # m = n*(n-1)/2  -->  n = (1 + sqrt(1+8m)) / 2
        import math
        n = int((1 + math.isqrt(1 + 8*m)) // 2)

        # If n==2, any numbers that sum to arr[0] are valid, e.g., [0, arr[0]]
        if n == 2:
            return [0, arr[0]]

        # Extract first three pair sums
        S01 = arr[0]
        S02 = arr[1]
        S12 = arr[n - 1]   # this is the sum of res[1] + res[2]

        # Compute first element
        res0 = (S01 + S02 - S12) // 2

        res = [0] * n
        res[0] = res0
        res[1] = S01 - res0
        res[2] = S02 - res0

        # Compute remaining values
        idx = 2
        for k in range(3, n):
            idx += 1
            res[k] = arr[idx - 1] - res0

        return res

# Time Complexity: O(n), where n is the length of the resulting array.
# Space Complexity: O(1), since we are using only a few extra variables.