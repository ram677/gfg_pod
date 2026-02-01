#K Sized Subarray Maximum

from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        # Optimization 1: Edge case for k=1
        if k == 1:
            return arr
            
        n = len(arr)
        dq = deque()
        result = []
        
        # Optimization 2: Process the first 'k' elements separately
        # to initialize the deque. This avoids the 'if i >= k-1' check inside the main loop.
        for i in range(k):
            # Remove elements smaller than the current one
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
        
        # Add the maximum of the first window
        result.append(arr[dq[0]])
        
        # Process the remaining elements
        for i in range(k, n):
            # 1. Remove element that is sliding out of the window
            # We check equality because indices increase by 1 strictly.
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # 2. Maintain the deque in descending order of values
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            # 3. Add current element index
            dq.append(i)
            
            # 4. The front of the deque is always the maximum for the current window
            result.append(arr[dq[0]])
            
        return result
    
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(k), where k is the size of the subarray.