#The Painter's Partition Problem-II

class Solution:
    def minTime(self, arr, k):
        # Helper function to check if it's possible to paint all boards
        # within 'time_limit' using at most 'k' painters.
        def isPossible(time_limit):
            painters_needed = 1
            current_time = 0
            
            for length in arr:
                # If a single board is larger than the limit, it's impossible
                if length > time_limit:
                    return False
                
                # If adding this board exceeds the limit, assign to next painter
                if current_time + length > time_limit:
                    painters_needed += 1
                    current_time = length
                    # If we need more painters than available, return False
                    if painters_needed > k:
                        return False
                else:
                    current_time += length
            
            return True

        # Binary Search on the Answer
        low = max(arr)  # Minimum possible max time (must paint largest board)
        high = sum(arr) # Maximum possible max time (one painter paints all)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            if isPossible(mid):
                ans = mid
                high = mid - 1  # Try for a smaller time
            else:
                low = mid + 1   # Need more time
                
        return ans
    
# Time Complexity: O(n log m) where n is the number of boards and m is the sum of the lengths of the boards (the search space for the maximum time).
# Space Complexity: O(1) as we are using only constant extra space for variables.