#String stack

import collections
import bisect

class Solution:
    def stringStack(self, pat: str, tar: str) -> bool:

        n, m = len(pat), len(tar)

        if n < m:
            return False

        # Precompute positions of each character, separated by index parity.
        # This allows for efficient lookups.
        # positions maps (character, parity) to a sorted list of indices.
        positions = collections.defaultdict(list)
        for i, char in enumerate(pat):
            positions[(char, i % 2)].append(i)

        # The parity of the index of the first character of the subsequence (`i_1`) must 
        # match the parity of the total number of "extra" characters (`n - m`).
        start_parity = (n - m) % 2

        # Greedily search for the earliest valid subsequence.
        current_pat_idx = -1
        current_parity = start_parity

        for char_in_tar in tar:
            # The key to look up in our precomputed map.
            key = (char_in_tar, current_parity)
            
            # If a character with the required parity doesn't exist at all, we fail.
            if key not in positions:
                return False
            
            idx_list = positions[key]
            
            # Find the smallest index in `idx_list` strictly greater than `current_pat_idx`.
            # `bisect.bisect_right` efficiently finds the insertion point, which corresponds
            # to the index of the first element larger than `current_pat_idx`.
            insertion_point = bisect.bisect_right(idx_list, current_pat_idx)
            
            # If the insertion point is at the end of the list, no valid next index exists.
            if insertion_point == len(idx_list):
                return False
            
            # We found the next character in our subsequence. Update the last used index.
            current_pat_idx = idx_list[insertion_point]
            
            # For the next character in `tar`, the required index parity must alternate.
            current_parity = 1 - current_parity
            
        # If we successfully found a valid index for every character in `tar`, it's possible.
        return True
    
#Time Complexity: O(n log n + m log k) where n is the length of `pat`, m is the length of `tar`, and k is the maximum number of occurrences of any character in `pat`. The O(n log n) term comes from sorting the indices for each character, and the O(m log k) term comes from performing binary searches for each character in `tar`.
#Space Complexity: O(n) for storing the positions of characters in `pat`.# where n is the length of `pat` due to the storage of indices in the positions dictionary.