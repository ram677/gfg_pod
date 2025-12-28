#Rotate Deque By K

from collections import deque

class Solution:
    def rotateDeque(self, dq, type, k):
        if type == 1:
            dq.rotate(k)
        elif type == 2:
            dq.rotate(-k)


#Time Complexity: O(k) where k is the number of rotations.
#Space Complexity: O(1) as we are using the deque in place.