#Maximum Non-Overlapping Odd Palindrome Sum

class Solution:
    def maxSum(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        # Manacher (odd-length palindromes)
        rad = [0] * n
        center, right = 0, -1
        for i in range(n):
            if i > right:
                k = 1
            else:
                mirror = 2 * center - i
                k = min(rad[mirror] + 1, right - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            rad[i] = k - 1
            if i + rad[i] > right:
                center, right = i, i + rad[i]

        # maxLenEndingAt[end] and maxLenStartingAt[start]
        maxEnd = [0] * n
        maxStart = [0] * n
        for i in range(n):
            L = 2 * rad[i] + 1
            start = i - rad[i]
            end = i + rad[i]
            if L > 0:
                if L > maxEnd[end]:
                    maxEnd[end] = L
                if L > maxStart[start]:
                    maxStart[start] = L

        # Propagate to fill smaller nested palindromes
        # If there is a palindrome of length X ending at pos i+1,
        # there is a palindrome of length at least X-2 ending at pos i.
        for i in range(n - 2, -1, -1):
            cand = maxEnd[i + 1] - 2
            if cand > maxEnd[i]:
                maxEnd[i] = cand

        # Similarly for starts: forward propagation
        for i in range(1, n):
            cand = maxStart[i - 1] - 2
            if cand > maxStart[i]:
                maxStart[i] = cand

        # Build prefix best (best palindrome length ending at or before i)
        left_best = [0] * n
        left_best[0] = maxEnd[0]
        for i in range(1, n):
            left_best[i] = max(left_best[i - 1], maxEnd[i])

        # Build suffix best (best palindrome length starting at or after i)
        right_best = [0] * n
        right_best[n - 1] = maxStart[n - 1]
        for i in range(n - 2, -1, -1):
            right_best[i] = max(right_best[i + 1], maxStart[i])

        # Combine at every split between i and i+1
        ans = 0
        for i in range(n - 1):
            ans = max(ans, left_best[i] + right_best[i + 1])

        return ans

# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the length of the input string s.