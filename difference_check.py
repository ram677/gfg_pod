# Difference Check

class Solution:
    def minDifference(self, arr):
        def time_to_seconds(t):
            h, m, s = map(int, t.split(":"))
            return h * 3600 + m * 60 + s

        # Convert times to seconds
        times = [time_to_seconds(t) for t in arr]
        times.sort()

        # Initialize minimum difference with large value
        min_diff = float('inf')

        # Check difference between adjacent times
        for i in range(1, len(times)):
            diff = times[i] - times[i-1]
            min_diff = min(min_diff, diff)

        # Check wrap-around time (24h = 86400 seconds)
        wrap_diff = 86400 - times[-1] + times[0]
        min_diff = min(min_diff, wrap_diff)

        return min_diff

# Time Complexity: O(n log n) due to sorting  
# Space Complexity: O(n) for storing the converted times
# Where n is the number of time strings in the input list.