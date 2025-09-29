#Maximum subarray sum 2

import collections

class Solution:
    def maxSubarrSum(self, arr, a, b):
        n = len(arr)
        
        # Step 1: Compute prefix sums. prefix[i] = sum(arr[0]...arr[i-1])
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
            
        max_sum = -float('inf')
        
        # Use a deque to find the minimum prefix sum in a sliding window.
        # The deque stores indices 'j' such that prefix[j] is increasing.
        dq = collections.deque()
        
        # 'i' represents the end index (exclusive) of the subarray.
        # The sum of arr[j...i-1] is prefix[i] - prefix[j].
        # Length is i-j. We need a <= i-j <= b, which means i-b <= j <= i-a.
        for i in range(a, n + 1):
            # The window for the starting index 'j' is [i-b, i-a].
            
            # Add the new rightmost element of the window (i-a) to the deque.
            # To maintain the increasing order, pop elements from the rear that are larger.
            while dq and prefix[dq[-1]] >= prefix[i - a]:
                dq.pop()
            dq.append(i - a)
            
            # Remove indices from the front of the deque that are no longer in the window.
            # The window's left boundary is i-b.
            if dq and dq[0] < i - b:
                dq.popleft()
            
            # The minimum prefix sum in the valid range is at the front of the deque.
            # Calculate the sum for the subarray ending at i-1 with the best start.
            if dq:
                current_sum = prefix[i] - prefix[dq[0]]
                max_sum = max(max_sum, current_sum)
                
        return max_sum
    
#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(n) in the worst case for the deque and prefix sum array.