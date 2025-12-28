#Substrings with K Distinct

class Solution:
    def countSubstr(self, s, k):
        def atMostK(s, k):
            n = len(s)
            count = {}
            res = 0
            left = 0
            for right in range(n):
                count[s[right]] = count.get(s[right], 0) + 1
                while len(count) > k:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
                res += (right - left + 1)
            return res

        return atMostK(s, k) - atMostK(s, k - 1)

#Time Complexity: O(n) where n is the length of the string
#Space Complexity: O(k) for the count dictionary.
#Where k is the number of distinct characters.