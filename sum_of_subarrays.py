#Sum of Subarrays

class Solution:
    def subarraySum(self, arr):
        total_sum = 0
        n = len(arr)

        for i in range(n):
            occurrences = (i + 1) * (n - i)
            total_sum += arr[i] * occurrences
            
        return total_sum

#Time Complexity: O(n) where n is the length of the input array.
#Space Complexity: O(1) since we are using a constant amount of space.