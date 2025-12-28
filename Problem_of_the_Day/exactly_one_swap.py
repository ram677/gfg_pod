#Exactly one swap

from collections import defaultdict

class Solution:
    def countStrings(self, s): 
        n = len(s)
        total_pairs = n * (n - 1) // 2
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        same = 0
        for count in freq.values():
            same += count * (count - 1) // 2
        distinct_pairs = total_pairs - same
        return distinct_pairs + (1 if same > 0 else 0)

#Time Complexity: O(n) where n is the length of the string
#Space Complexity: O(1) for the frequency dictionary