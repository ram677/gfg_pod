#All Palindromic Partitions

class Solution:
    def palinParts(self, s):
        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                substr = s[start:end]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return res


#Time Complexity: O(n^2) where n is the length of the string
#Space Complexity: O(n) for the recursion stack