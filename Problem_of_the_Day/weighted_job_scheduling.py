#Weighted Job Scheduling

import bisect
from typing import List

class Solution:
    def maxProfit(self, jobs: List[List[int]]) -> int:
        n = len(jobs)
        
        # Sort jobs by their end time
        jobs.sort(key=lambda x: x[1])
        
        # dp[i] will store the max profit for the first i+1 jobs
        dp = [0] * n
        # Base case: max profit for just the first job
        dp[0] = jobs[0][2]

        for i in range(1, n):
            current_profit = jobs[i][2]
            current_start = jobs[i][0]
            
            # Find the latest non-overlapping job 'j'
            # We perform a binary search on the end times of jobs[0...i-1]
            
            # We can't use bisect directly on the list of lists easily.
            # A manual binary search is clear.
            j = -1 # Index of the last non-overlapping job
            low = 0
            high = i - 1
            
            while low <= high:
                mid = (low + high) // 2
                if jobs[mid][1] <= current_start:
                    # This job is non-overlapping, it's a candidate
                    j = mid
                    low = mid + 1 # Try to find a later one
                else:
                    # This job overlaps, search earlier
                    high = mid - 1
            
            # Add profit from the last non-overlapping job, if one exists
            if j != -1:
                current_profit += dp[j]

            # Option 2: Skip the current job
            profit_if_skip = dp[i - 1]
            
            # Store the max of taking or skipping the current job
            dp[i] = max(current_profit, profit_if_skip)
            
        # The final answer is the max profit using all jobs
        return dp[n - 1]
    
# Time Complexity: O(n log n) due to sorting and binary search for each job.
# Space Complexity: O(n) for the dp array.
# Where n is the number of jobs.