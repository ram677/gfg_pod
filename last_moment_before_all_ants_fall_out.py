#Last Moment Before All Ants Fall Out

class Solution:
    def getLastMoment(self, n: int, left: list[int], right: list[int]) -> int:
        max_time = 0

        # Calculate time for ants moving left
        for pos in left:
            max_time = max(max_time, pos)

        # Calculate time for ants moving right
        for pos in right:
            max_time = max(max_time, n - pos)

        return max_time

#Time Complexity: O(n) where n is the length of the input lists.
#Space Complexity: O(1) since we are using a constant amount of space.