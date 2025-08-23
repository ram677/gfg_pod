#Longest Substring with K Uniques

class Solution:
    def longestKSubstr(self, s, k):
        n = len(s)
        if n == 0 or k == 0:
            return -1

        left = 0
        max_len = -1
        char_map = {}

        for right in range(n):
            # Include current character in window
            char_map[s[right]] = char_map.get(s[right], 0) + 1

            # Shrink window if unique characters exceed k
            while len(char_map) > k:
                char_map[s[left]] -= 1
                if char_map[s[left]] == 0:
                    del char_map[s[left]]
                left += 1

            # Check if current window has exactly k distinct characters
            if len(char_map) == k:
                max_len = max(max_len, right - left + 1)

        return max_len

        
#Time Complexity: O(n) where n is the length of the string.
#Space Complexity: O(k) for the character map.
#Where k is the number of unique characters allowed in the substring.