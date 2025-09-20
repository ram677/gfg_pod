#Longest Subarray Length

class Solution:
    def longestSubarray(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        left_bound = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                left_bound[i] = stack[-1] + 1
            else:
                left_bound[i] = 0
            stack.append(i)
        
        right_bound = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                right_bound[i] = stack[-1] - 1
            else:
                right_bound[i] = n-1
            stack.append(i)
        
        ans = 0
        for i in range(n):
            length = right_bound[i] - left_bound[i] + 1
            if arr[i] <= length:
                if length > ans:
                    ans = length
        return ans
    
#Time Complexity: O(n) where n is the length of the array.
#Space Complexity: O(n) for the left_bound and right_bound arrays.