#Lexicographically Largest String After K Deletions

class Solution:
    def maxSubseq(self, s, k):
        n = len(s)
        keep = n - k
        stack = []
        
        for i, ch in enumerate(s):
            while stack and k > 0 and stack[-1] < ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        
        # Only take first (n - k) characters from the stack
        return ''.join(stack[:keep])

#Time Complexity: O(n) where n is the length of the string
#Space Complexity: O(n) for the stack