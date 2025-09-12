#Minimize the Heights II

import sys

class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()

        ans = arr[n-1] - arr[0]

        for i in range(1, n):
            # Check for invalid operation (negative height)
            if arr[i] - k < 0:
                continue

            # New maximum height: either the largest element decreased by k
            # or the previous element increased by k.
            max_height = max(arr[i-1] + k, arr[n-1] - k)

            # New minimum height: either the smallest element increased by k
            # or the current element decreased by k.
            min_height = min(arr[0] + k, arr[i] - k)

            # Update the answer
            ans = min(ans, max_height - min_height)

        return ans
    
#Time Complexity: O(n log n) due to the sorting step.
#Space Complexity: O(1) as we are using a constant amount of extra space.
# where n is the length of the input array arr.