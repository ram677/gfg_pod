#Minimum Cost of ropes

import heapq
from typing import List

class Solution:
  def minCost(self, arr: List[int]) -> int:
    # If there's one or zero ropes, no cost is incurred.
    if len(arr) <= 1:
        return 0
        
    # Step 1: Turn the list of ropes into a min-heap.
    heapq.heapify(arr)
    
    total_cost = 0
    
    # Step 2: Loop until only one rope remains.
    while len(arr) > 1:
        # Extract the two shortest ropes.
        rope1 = heapq.heappop(arr)
        rope2 = heapq.heappop(arr)
        
        # The cost of this connection is their sum.
        current_cost = rope1 + rope2
        total_cost += current_cost
        
        # Add the new, combined rope back to the heap.
        heapq.heappush(arr, current_cost)
        
    return total_cost
  
# Time Complexity: O(N log N) where N is the number of ropes.
# Space Complexity: O(N) for the min-heap.