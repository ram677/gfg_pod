#Longest Span in two Binary Arrays

class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        diff = [a1[i] - a2[i] for i in range(n)]

        prefix_sum = 0
        max_len = 0
        hash_map = {}

        for i in range(n):
            prefix_sum += diff[i]

            if prefix_sum == 0:
                max_len = i + 1  # span from 0 to i

            if prefix_sum in hash_map:
                max_len = max(max_len, i - hash_map[prefix_sum])
            else:
                hash_map[prefix_sum] = i

        return max_len

#Time Complexity: O(n) where n is the length of the input arrays
#Space Complexity: O(n) for the hash_map