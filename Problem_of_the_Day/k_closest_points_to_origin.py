#K Closest Points to Origin

import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We will use a max-heap of size k. Since Python's heapq is a min-heap,
        # we'll store negative distances to simulate a max-heap.
        # The heap will store tuples of (-distance_squared, [x, y]).
        max_heap = []

        for x, y in points:
            # Calculate the squared distance to avoid using sqrt().
            dist_sq = x*x + y*y
            
            # Push the negative distance and the point onto the heap.
            heapq.heappush(max_heap, (-dist_sq, [x, y]))
            
            # If the heap is now larger than k, remove the farthest point.
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # The heap now contains the k closest points. Extract just the points.
        return [point for dist, point in max_heap]
    
# Time Complexity: O(N log k) where N is the number of points.
# Space Complexity: O(k) for the heap.
# Where k is the number of closest points to find.