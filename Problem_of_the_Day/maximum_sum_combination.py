#Maximum Sum Combination

import heapq

class Solution:
    def topKSumPairs(self, a, b, k):
        n = len(a)
        a.sort(reverse=True)
        b.sort(reverse=True)

        max_heap = []
        visited = set()

        # Initial pair (a[0] + b[0], (0, 0))
        heapq.heappush(max_heap, (-(a[0] + b[0]), 0, 0))
        visited.add((0, 0))

        result = []

        while k > 0 and max_heap:
            current_sum, i, j = heapq.heappop(max_heap)
            result.append(-current_sum)
            k -= 1

            # Next pair in row (i+1, j)
            if i + 1 < n and (i + 1, j) not in visited:
                heapq.heappush(max_heap, (-(a[i + 1] + b[j]), i + 1, j))
                visited.add((i + 1, j))

            # Next pair in column (i, j+1)
            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(max_heap, (-(a[i] + b[j + 1]), i, j + 1))
                visited.add((i, j + 1))

        return result

#Time Complexity: O(n log n) where n is the length of the arrays.
#Space Complexity: O(n) for the max heap and visited set.