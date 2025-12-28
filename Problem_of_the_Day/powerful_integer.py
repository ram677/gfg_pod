class Solution:
    def powerfulInteger(self, intervals, k):
        events = []
        
        # Mark +1 at start, -1 at end+1
        for start, end in intervals:
            events.append((start, 1))
            events.append((end + 1, -1))
        
        # Sort events by position
        events.sort()

        count = 0
        max_powerful = -1
        prev = None

        for point, change in events:
            if prev is not None and count >= k:
                # All integers in [prev, point - 1] are powerful
                max_powerful = max(max_powerful, point - 1)
            
            count += change
            prev = point
        
        return max_powerful
    
#Time Complexity: O(n log n) — for sorting events
#space Complexity: O(n)  — to store events list
# where n is the number of intervals
