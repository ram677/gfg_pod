#Longest subarray with Atmost two distinct integers

from collections import defaultdict

class Solution:
    def totalElements(self, arr):
        left = 0
        freq = defaultdict(int)
        max_len = 0

        for right in range(len(arr)):
            freq[arr[right]] += 1

            # If more than 2 distinct integers, shrink window from left
            while len(freq) > 2:
                freq[arr[left]] -= 1
                if freq[arr[left]] == 0:
                    del freq[arr[left]]
                left += 1

            # Update maximum length
            max_len = max(max_len, right - left + 1)

        return max_len

#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(1) since we are using only a constant amount of space.