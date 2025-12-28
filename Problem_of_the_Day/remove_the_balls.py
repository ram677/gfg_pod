#Remove the balls

class Solution:
    def findLength(self, color, radius):
        stack = []
        
        for i in range(len(color)):
            # If stack is not empty and current ball matches the top ball
            if stack and stack[-1][0] == color[i] and stack[-1][1] == radius[i]:
                # Remove the matching pair by popping from stack
                stack.pop()
            else:
                # Add current ball to stack
                stack.append((color[i], radius[i]))
        
        return len(stack)

#Time Complexity: O(n) where n is the number of balls
#Space Complexity: O(n) for the stack.