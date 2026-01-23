#Maximum People Visible in a Line

class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        # Initialize boundaries
        # left[i] stores the index of the nearest person to the left with height >= arr[i]
        left = [-1] * n
        # right[i] stores the index of the nearest person to the right with height >= arr[i]
        right = [n] * n
        
        # 1. Find Previous Greater or Equal Element (Left Boundaries)
        stack = []
        for i in range(n):
            # Remove people strictly smaller than current person
            # The first person remaining is the nearest one >= current
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            
            if stack:
                left[i] = stack[-1]
            
            stack.append(i)
            
        # 2. Find Next Greater or Equal Element (Right Boundaries)
        stack = []
        for i in range(n - 1, -1, -1):
            # Remove people strictly smaller than current person
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            
            if stack:
                right[i] = stack[-1]
            
            stack.append(i)
            
        # 3. Calculate max visible people
        max_visible = 0
        for i in range(n):
            # The range (left[i], right[i]) contains people strictly smaller than arr[i]
            # visible count = (right boundary) - (left boundary) - 1
            current_visible = right[i] - left[i] - 1
            if current_visible > max_visible:
                max_visible = current_visible
                
        return max_visible

# Time Complexity: O(n), where n is the number of people in the array.
# Space Complexity: O(n) for the left and right boundary arrays and the stack.