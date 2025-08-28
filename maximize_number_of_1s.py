#Maximize Number of 1's

class Solution:
    def maxOnes(self, arr: list[int], k: int) -> int:
        n = len(arr)
        left = 0
        zero_count = 0
        max_len = 0

        # 'right' pointer expands the window
        for right in range(n):
            # If we encounter a zero, increment our count
            if arr[right] == 0:
                zero_count += 1
            
            # If zero_count exceeds k, the window is invalid.
            # We must shrink it from the left until it's valid again.
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            
            # The current window [left, right] is valid.
            # Update the max_len.
            max_len = max(max_len, right - left + 1)
        
        return max_len

#Time Complexity: O(n)
#Space Complexity: O(1)
#Where n is the length of the input array