#Max Score from Subarray Mins

class Solution:
    def maxSum(self, arr):
        n = len(arr)
        max_score = 0
        stack = []

        for i in range(n):
            # Maintain a decreasing stack for mono-stack
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                # Compare with previous element (nearest smaller)
                max_score = max(max_score, arr[i] + arr[stack[-1]])
            if i > 0:
                # Compare with previous directly
                max_score = max(max_score, arr[i] + arr[i - 1])
            stack.append(i)

        return max_score

#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(n) for the stack.