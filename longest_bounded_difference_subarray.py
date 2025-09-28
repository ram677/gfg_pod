#Longest Bounded-Difference Subarray

import collections
from typing import List

class Solution:
    def longestSubarray(self, arr: List[int], x: int) -> List[int]:
        n = len(arr)
        if n == 0:
            return []
        
        # Deques to store indices of min and max candidates
        min_dq = collections.deque()
        max_dq = collections.deque()
        
        left = 0
        max_len = 0
        start_index = 0
        
        for right in range(n):
            # 1. Add the new element (at index 'right') to the deques
            
            # Maintain monotonically increasing min_dq
            while min_dq and arr[min_dq[-1]] >= arr[right]:
                min_dq.pop()
            min_dq.append(right)
            
            # Maintain monotonically decreasing max_dq
            while max_dq and arr[max_dq[-1]] <= arr[right]:
                max_dq.pop()
            max_dq.append(right)
            
            # 2. Check and shrink the window from the left
            # while the window is invalid
            while arr[max_dq[0]] - arr[min_dq[0]] > x:
                # If the element leaving the window (at 'left')
                # is the current min, remove it from the deque
                if min_dq[0] == left:
                    min_dq.popleft()
                
                # If it's the current max, remove it
                if max_dq[0] == left:
                    max_dq.popleft()
                    
                # Shrink the window
                left += 1
            
            # 3. Update max_len
            # At this point, the window [left...right] is valid
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                start_index = left
                
        # Return the longest subarray found
        return arr[start_index : start_index + max_len]

#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(n) in the worst case for the deques.