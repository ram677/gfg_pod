#Form the Largest Number

from functools import cmp_to_key

class Solution:
    def findLargest(self, arr):
        # Custom comparator function
        def compare(x, y):
            if x + y > y + x:
                return -1   # x should come before y
            elif x + y < y + x:
                return 1    # y should come before x
            else:
                return 0
        
        # Convert all integers to strings for concatenation
        arr = list(map(str, arr))
        
        # Sort using custom comparator
        arr.sort(key=cmp_to_key(compare))
        
        # Join sorted array into single string
        result = ''.join(arr)
        
        # Handle case like "000...0"
        return result if result[0] != '0' else '0'

#Time Complexity: O(n log n), where n is the number of elements in the array.
#Space Complexity: O(n), for storing the string representations of the numbers.