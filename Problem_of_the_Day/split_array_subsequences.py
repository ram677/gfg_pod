#Split Array Subsequences

from collections import defaultdict
import heapq
from typing import List

class Solution:
    def isPossible(self, arr: List[int], k: int) -> bool:
        # tails[x] is a min-heap of lengths of subsequences ending at x.
        tails = defaultdict(list)

        for num in arr:
            # Check if we can extend a subsequence ending at num - 1.
            if tails[num - 1]:
                # Greedily extend the shortest existing subsequence.
                length = heapq.heappop(tails[num - 1])
                heapq.heappush(tails[num], length + 1)
            else:
                # If not, we must start a new subsequence.
                heapq.heappush(tails[num], 1)

        # After processing all numbers, check if every formed subsequence
        # meets the length requirement.
        for num in tails:
            for length in tails[num]:
                if length < k:
                    return False
        
        return True
    
# Time Complexity: O(N log M) where N is the length of arr and M is the maximum number of subsequences ending with any number.
# Space Complexity: O(N) for the tails dictionary.