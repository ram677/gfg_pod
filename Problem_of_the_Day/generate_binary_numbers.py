#Generate Binary Numbers

import collections

class Solution:
  def generateBinary(self, n):
    q = collections.deque()
    q.append("1")
    
    result = []
    
    for _ in range(n):
      current = q.popleft()
      result.append(current)
      
      q.append(current + "0")
      q.append(current + "1")
      
    return result
  
#Time Complexity: O(n) where n is the number of binary numbers to generate.
#Space Complexity: O(n) for the queue and result list.