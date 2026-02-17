#Maximum number of overlapping Intervals

class Solution:
    def overlapInt(self, arr):
        events = []
        
        # Create events: (time, type)
        # We use -1 for 'start' and 1 for 'end' purely for sorting purposes.
        # When sorting tuples, Python compares the first element, then the second.
        # By using -1 for start, (t, -1) will come before (t, 1).
        # This ensures we count the start of a new interval before the end of an old one
        # at the same timestamp, satisfying the inclusive overlap condition.
        for start, end in arr:
            events.append((start, -1))
            events.append((end, 1))
            
        # Sort events by time, then by type (-1 before 1)
        events.sort()
        
        max_overlaps = 0
        current_overlaps = 0
        
        for _, type in events:
            # If type is -1, it's a start event
            if type == -1:
                current_overlaps += 1
                max_overlaps = max(max_overlaps, current_overlaps)
            # If type is 1, it's an end event
            else:
                current_overlaps -= 1
                
        return max_overlaps
    
# Time Complexity: O(N log N) due to sorting, where N is the number of intervals.
# Space Complexity: O(N) for the events list, where N is the number of intervals.