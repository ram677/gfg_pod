#Find H-Index

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h

#Time Complexity: O(n log n) due to sorting.
#Space Complexity: O(1).
#Where n is the number of citations.