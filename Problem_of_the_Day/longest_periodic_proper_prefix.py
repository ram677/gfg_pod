#Longest Periodic Proper Prefix

class Solution:
    def compute_z_array(self, s: str) -> list[int]:
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i > r:
                l, r = i, i
                while r < n and s[r - l] == s[r]:
                    r += 1
                z[i] = r - l
                r -= 1
            else:
                k = i - l
                if z[k] < r - i + 1:
                    z[i] = z[k]
                else:
                    l = i
                    while r < n and s[r - l] == s[r]:
                        r += 1
                    z[i] = r - l
                    r -= 1
        return z

    def getLongestPrefix(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return -1

        z = self.compute_z_array(s)

        for i in range(n - 1, 0, -1):
            if z[i] == n - i:
                return i
        
        return -1
    
# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) for the z array    
# Where n is the length of the input string.