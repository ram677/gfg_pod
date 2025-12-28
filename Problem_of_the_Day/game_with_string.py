#Game with String

import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        freq = Counter(s)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)

        while k > 0 and max_heap:
            top = heapq.heappop(max_heap)
            top += 1  # since it's negative, this means reducing the frequency by 1
            k -= 1
            if top != 0:
                heapq.heappush(max_heap, top)

        return sum(x * x for x in max_heap)

#Time Complexity: O(n log n) where n is the length of the string
#Space Complexity: O(n) for the frequency counter