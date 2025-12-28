#Find K Smallest Sum Pairs

import heapq
from typing import List

class Solution:
    def kSmallestPair(self, arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
        """
        Finds the k pairs with the smallest sums from two sorted arrays.
        """
        # Handle edge cases where one of the arrays is empty.
        if not arr1 or not arr2:
            return []
            
        min_heap = []
        result = []
        
        # Step 2: Seed the heap with the first k pairs using the first element of arr2.
        # We only need to consider the first k elements of arr1 initially,
        # as any pair beyond that is unlikely to be in the smallest k sums.
        for i in range(min(k, len(arr1))):
            # Push (sum, index_in_arr1, index_in_arr2)
            heapq.heappush(min_heap, (arr1[i] + arr2[0], i, 0))

        # Step 3: Extract the k smallest pairs.
        while k > 0 and min_heap:
            # Pop the pair with the current smallest sum.
            current_sum, i, j = heapq.heappop(min_heap)
            result.append([arr1[i], arr2[j]])
            
            # If there's a next element in arr2 for the current element from arr1,
            # push the new pair as a candidate.
            if j + 1 < len(arr2):
                heapq.heappush(min_heap, (arr1[i] + arr2[j + 1], i, j + 1))
            
            k -= 1
            
        return result
    
# Time Complexity: O(k log min(k, N)) where N is the length of arr1.
# Space Complexity: O(min(k, N)) for the min-heap.
# Whwere k is the number of pairs to find.