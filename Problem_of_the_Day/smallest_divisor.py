#Smallest Divisor

import math

class Solution:
    def smallestDivisor(self, arr, k):
        def compute_sum(divisor):
            return sum((num + divisor - 1) // divisor for num in arr)
        
        left, right = 1, max(arr)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            total = compute_sum(mid)
            if total <= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

#Time Complexity: O(n log m) where n is the number of elements in the array and m is the maximum element
#Space Complexity: O(1) for the variables used