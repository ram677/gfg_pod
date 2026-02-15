#Chocolate Distribution Problem

class Solution:
    def findMinDiff(self, arr, M):
        # Edge case: If there are no students or packets, difference is 0
        if M == 0 or len(arr) == 0:
            return 0
            
        # Sort the array to group closest values together
        arr.sort()
        
        # Initialize min_diff to a very large number
        min_diff = float('inf')
        
        # Sliding window of size M
        # The window covers indices from i to i + M - 1
        # We stop when the end of the window reaches the end of the array
        for i in range(len(arr) - M + 1):
            # The current difference is the last element of the window minus the first
            current_diff = arr[i + M - 1] - arr[i]
            
            if current_diff < min_diff:
                min_diff = current_diff
                
        return min_diff
    
# Time Complexity: O(n log n) due to sorting, where n is the number of packets.
# Space Complexity: O(1) if we ignore the input array, otherwise O(n) due to the space used by the sorting algorithm.