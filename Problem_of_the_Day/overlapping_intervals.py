#Overlapping Intervals

class Solution:
    def mergeOverlap(self, arr):
        # 1. Sort intervals by their start time
        arr.sort(key=lambda x: x[0])
        
        # Initialize result with the first interval
        res = [arr[0]]
        
        # 2. Iterate through the rest of the intervals
        for i in range(1, len(arr)):
            current = arr[i]
            last_merged = res[-1]
            
            # Check for overlap
            # If current start is <= last merged end
            if current[0] <= last_merged[1]:
                # Merge them by maximizing the end time
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add current interval to result
                res.append(current)
                
        return res
    
# Time Complexity: O(n log n) due to sorting, where n is the number of intervals.
# Space Complexity: O(n) for the result list in the worst case.