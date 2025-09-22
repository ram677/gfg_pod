#Max of min for every window size

class Solution:
    def maxOfMins(self, arr):
        n = len(arr)

        # left[i] = index of the Previous Smaller Element
        # right[i] = index of the Next Smaller Element
        left = [-1] * n
        right = [n] * n
        stack = []

        # Calculate left boundaries (Previous Smaller Element)
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # Clear stack and calculate right boundaries (Next Smaller Element)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        # ans[l] will store the maximum value among all elements arr[i]
        # for which arr[i] is the minimum in a window of maximum possible length l.
        ans = [0] * (n + 1)
        for i in range(n):
            length = right[i] - left[i] - 1
            ans[length] = max(ans[length], arr[i])

        # The answer for a window of size k must be at least the answer
        # for a window of size k+1. We propagate maximums from right to left.
        for i in range(n - 1, 0, -1):
            ans[i] = max(ans[i], ans[i+1])
            
        # The result at index i is for window size i+1.
        # We return the part of the ans array for window sizes 1 to n.
        return ans[1:]
    
#Time Complexity: O(n) where n is the number of elements in the array.
#Space Complexity: O(n) for the left, right, and ans arrays and the stack used for boundary calculations.