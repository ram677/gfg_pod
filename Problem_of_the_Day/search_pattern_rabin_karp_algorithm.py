#Search Pattern (Rabin-Karp Algorithm)

class Solution:
    def search(self, pat, txt):
        m, n = len(pat), len(txt)
        if m > n:
            return []

        base = 256 
        mod = 10**9 + 7 

        h = 1
        for _ in range(m - 1):
            h = (h * base) % mod

        p_hash = 0
        t_hash = 0 

        for i in range(m):
            p_hash = (base * p_hash + ord(pat[i])) % mod
            t_hash = (base * t_hash + ord(txt[i])) % mod

        result = []

        for i in range(n - m + 1):
            if p_hash == t_hash:
                if txt[i:i+m] == pat:
                    result.append(i + 1) 

            if i < n - m:
                t_hash = (t_hash - ord(txt[i]) * h) % mod
                t_hash = (t_hash * base + ord(txt[i + m])) % mod
                t_hash = (t_hash + mod) % mod

        return result

#Time Complexity: O(n) where n is the length of the text
#Space Complexity: O(1) for the hash values