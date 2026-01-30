#Interleave the First Half of the Queue with Second Half

from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        if n == 0:
            return
            
        mid = n // 2
        
        # Step 1: Extract the first half of the queue into a temporary structure.
        # We use an auxiliary deque for O(1) pops.
        temp = deque()
        for _ in range(mid):
            # Handle both 'deque' (popleft) and 'list' (pop(0)) inputs
            if hasattr(q, 'popleft'):
                temp.append(q.popleft())
            else:
                temp.append(q.pop(0))
        
        # Current State:
        # temp contains the First Half [e.g., 2, 4]
        # q contains the Second Half   [e.g., 3, 1]
        
        # Step 2: Interleave elements back into q
        # We append one from temp, then move one from the front of q to the back of q.
        for _ in range(mid):
            # 1. Append element from First Half (temp) to the back of q
            q.append(temp.popleft())
            
            # 2. Move element from Second Half (front of q) to the back of q
            if hasattr(q, 'popleft'):
                q.append(q.popleft())
            else:
                q.append(q.pop(0))
                
        # The queue 'q' is now modified in-place with interleaved elements.

# Time Complexity: O(n), where n is the number of elements in the queue.
# Space Complexity: O(n) for the temporary storage of the first half.