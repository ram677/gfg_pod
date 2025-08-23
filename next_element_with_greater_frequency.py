#Next element with greater frequency

from collections import Counter

class Solution:
    def findGreater(self, arr):
        n = len(arr)
        freq = Counter(arr)
        res = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # Pop elements from the stack whose frequency is less than or equal to current's
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()
            
            # If stack is not empty, top is the next element with higher frequency
            if stack:
                res[i] = stack[-1]

            # Push current element to stack
            stack.append(arr[i])

        return res

#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(n) for the stack.