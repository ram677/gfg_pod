#All Subsets Xor Sum

class Solution:
    def subsetXORSum(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        or_sum = 0
        for num in arr:
            or_sum |= num
            
        # The result is simply (OR sum of all elements) * 2^(n-1)
        # Using left shift for efficiency: or_sum << (n - 1)
        return or_sum << (n - 1)
    
# Time Complexity: O(n), where n is the number of elements in the array.
# Space Complexity: O(1), as we are using a constant amount of extra space.