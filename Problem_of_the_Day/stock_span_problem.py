#Stock span problem

class Solution:
    def calculateSpan(self, arr):
        n = len(arr)
        span = [0] * n
        stack = []  # Stores indices of days
        
        for i in range(n):
            # Pop elements that are less than or equal to the current price
            # because they cannot be the "blocking" day for the current day
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            # If stack is empty, it means all previous prices were smaller
            if not stack:
                span[i] = i + 1
            else:
                # The top of the stack is the nearest previous day with a higher price
                span[i] = i - stack[-1]
            
            # Push the current index onto the stack
            stack.append(i)
            
        return span
    
# Time Complexity: O(N) where N is the number of days (length of arr).
# Space Complexity: O(N) for the stack and span array.