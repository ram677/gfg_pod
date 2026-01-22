#Sum of subarray ranges

class Solution:
    def subarrayRanges(self, arr):
        n = len(arr)
        
        # Helper to calculate the sum of maximums or minimums
        # is_max=True calculates Sum(Subarray Max)
        # is_max=False calculates Sum(Subarray Min)
        def get_sum(is_max):
            stack = [] # Stores indices
            # left[i] stores index of previous boundary
            # right[i] stores index of next boundary
            left = [-1] * n
            right = [n] * n
            
            for i in range(n):
                # For Max: Pop while stack top is strictly smaller than current (find Next Greater)
                # For Min: Pop while stack top is strictly greater than current (find Next Smaller)
                while stack and (
                    (arr[stack[-1]] < arr[i]) if is_max else (arr[stack[-1]] > arr[i])
                ):
                    right[stack.pop()] = i
                
                # The element remaining on stack is the Previous Greater/Smaller (Or Equal)
                if stack:
                    left[i] = stack[-1]
                stack.append(i)
            
            # Calculate total contribution
            total = 0
            for i in range(n):
                count = (i - left[i]) * (right[i] - i)
                total += arr[i] * count
            return total

        # The result is the difference between the sum of maximums and sum of minimums
        return get_sum(is_max=True) - get_sum(is_max=False)
    
# Time Complexity: O(N) where N is the length of arr.
# Space Complexity: O(N) for the stack and boundary arrays.