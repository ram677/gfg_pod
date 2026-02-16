#Meeting Rooms

class Solution:
    def canAttend(self, arr):
        # If there are no meetings or just one, we can always attend.
        if not arr:
            return True
            
        # Sort meetings by their start time (first element of each sub-array)
        # Time Complexity: O(N log N)
        arr.sort(key=lambda x: x[0])
        
        # Iterate through the sorted meetings starting from the second one
        for i in range(1, len(arr)):
            current_start = arr[i][0]
            previous_end = arr[i-1][1]
            
            # Check if the current meeting starts before the previous one ends
            if current_start < previous_end:
                return False
                
        return True
    
# Time Complexity: O(N log N) due to sorting, where N is the number of meetings.
# Space Complexity: O(1) if we ignore the input array, otherwise O(N) due to the space used by the sorting algorithm.