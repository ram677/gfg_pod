# Longest Prefix Suffix

class Solution:
    def getLPSLength(self, s):
        n = len(s)
        lps = [0] * n
        length = 0  # length of previous longest prefix suffix
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps[-1]  # Last value is the answer
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) for the lps array  
# Where n is the length of the input string.