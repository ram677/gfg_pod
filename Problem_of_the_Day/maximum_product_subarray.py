#Maximum Product Subarray

class Solution:
    def maxProduct(self, arr):
        if not arr:
            return 0
            
        # Initialize variables
        # current_max: max product ending at the current position
        # current_min: min product ending at the current position
        # result: global maximum product found so far
        current_max = arr[0]
        current_min = arr[0]
        result = arr[0]
        
        for i in range(1, len(arr)):
            num = arr[i]
            
            # If current number is negative, max and min will swap
            if num < 0:
                current_max, current_min = current_min, current_max
            
            # Update current_max and current_min
            # We compare num itself with num * previous_extremes to handle 
            # cases where the subarray should reset at the current number (e.g., after a 0).
            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)
            
            # Update global result
            result = max(result, current_max)
            
        return result


# Time Complexity: O(n) where n is the length of the input array, as we traverse the array once.
# Space Complexity: O(1) as we are using only constant extra space to store the current maximum, minimum, and result.