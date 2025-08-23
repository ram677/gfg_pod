#Substrings of length k with k-1 distinct elements

from collections import defaultdict

class Solution:
    def substrCount(self, s, k):
        if k > len(s): return 0
        
        count = 0
        freq = defaultdict(int)
        distinct = 0

        for i in range(len(s)):
            # Add the rightmost character
            if freq[s[i]] == 0:
                distinct += 1
            freq[s[i]] += 1

            # Remove the leftmost character when window exceeds size k
            if i >= k:
                freq[s[i - k]] -= 1
                if freq[s[i - k]] == 0:
                    distinct -= 1

            # Check valid window
            if i >= k - 1 and distinct == k - 1:
                count += 1

        return count

#Time Complexity: O(n) where n is the length of the string.
#Space Complexity: O(k) for the frequency map.