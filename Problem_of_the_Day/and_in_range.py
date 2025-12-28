#AND In Range

class Solution:
    def andInRange(self, l, r):
        move = 0
        while l != r:
            l >>= 1
            r >>= 1
            move += 1
        return l << move
    
# Time Complexity: O(log(max(l, r))), where max(l, r) is the maximum of the two numbers.
# Space Complexity: O(1), as we are using a constant amount of extra space.