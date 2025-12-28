#Minimum Steps to Halve Sum

import heapq
from typing import List

class Solution:
  def minOperations(self, arr: List[int]) -> int:
    # Step 1: Calculate the initial and target sums.
    initial_sum = float(sum(arr))
    target_sum = initial_sum / 2.0
    
    # Step 2: Create a max-heap by storing negative values in a min-heap.
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    
    current_sum = initial_sum
    operations = 0
    
    # Step 3: Repeatedly halve the largest element until the sum is small enough.
    while current_sum > target_sum:
      operations += 1
      
      # Extract the largest element (which is the smallest negative number).
      largest_element = -heapq.heappop(max_heap)
      
      # Calculate the reduction in sum.
      reduction = largest_element / 2.0
      current_sum -= reduction
      
      # Push the new, halved element back into the heap.
      heapq.heappush(max_heap, -reduction)
      
    # Step 4: Return the total number of operations performed.
    return operations

# Time Complexity: O(N log N) where N is the number of elements in arr.
# Space Complexity: O(N) for the max-heap.