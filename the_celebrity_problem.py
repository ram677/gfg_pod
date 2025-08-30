#The Celebrity Problem

class Solution:
    def celebrity(self, mat: list[list[int]]) -> int:
        n = len(mat)
        if n == 0:
            return -1

        # Step 1: Find a potential celebrity candidate using elimination.
        # The candidate is the only person who wasn't eliminated.
        candidate = 0
        for i in range(1, n):
            # If the current candidate knows person i, they can't be a celebrity.
            # Person i then becomes the new potential candidate.
            if mat[candidate][i] == 1:
                candidate = i
        
        # Step 2: Verify if the found candidate is truly a celebrity.
        for i in range(n):
            # We don't need to check the candidate against themself.
            if i == candidate:
                continue
            
            # Check the two celebrity conditions:
            # 1. The candidate knows person i.
            # 2. Person i does not know the candidate.
            # If either is true, the candidate is not a celebrity.
            if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                return -1
        
        return candidate

#Time complexity: O(n)
#Space complexity: O(1)
#Where n is the number of people in the party.