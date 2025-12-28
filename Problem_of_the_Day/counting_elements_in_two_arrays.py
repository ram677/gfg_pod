#Counting elements in two arrays

from bisect import bisect_right

class Solution:
    def countLessEq(self, a, b):
        b.sort()
        result = []
        
        for num in a:
            count = bisect_right(b, num)
            result.append(count)
        
        return result

#Time Complexity: O(n log n) where n is the length of array b
#Space Complexity: O(n) for the result array