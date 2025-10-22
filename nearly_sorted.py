#Nearly sorted

import heapq
from typing import List

class Solution:
    def nearlySorted(self, arr: List[int], k: int) -> List[int]:
        """
        Sorts a nearly sorted array using a min-heap.
        """
        n = len(arr)
        
        # 1. Create a min-heap from the first k+1 elements.
        # We take min(n, k+1) to handle cases where the array is smaller than k+1.
        heap_size = min(n, k + 1)
        heap = arr[:heap_size]
        heapq.heapify(heap)
        
        # This index will track where to place the next sorted element in the array.
        write_idx = 0
        
        # 2. Iterate through the rest of the array.
        for read_idx in range(heap_size, n):
            # Pop the smallest element from the heap and place it in the array.
            arr[write_idx] = heapq.heappop(heap)
            write_idx += 1
            
            # Add the next element from the array into the heap.
            heapq.heappush(heap, arr[read_idx])
            
        # 3. Empty the remaining elements from the heap into the array.
        while heap:
            arr[write_idx] = heapq.heappop(heap)
            write_idx += 1
            
        return arr
    
# Time Complexity: O(N log k) where N is the number of elements in the array.
# Space Complexity: O(k) for the heap.
# Where k is the maximum distance an element is from its sorted position.