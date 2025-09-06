#Find length of Loop

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        
        # Step 1: Detect the loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        # Step 2: If no loop, return 0
        if not fast or not fast.next:
            return 0
        
        # Step 3: Calculate the length of the loop
        count = 1
        temp = slow.next
        while temp != slow:
            temp = temp.next
            count += 1
            
        return count
    
#Time complexity: O(n)
#Space complexity: O(1)
#Where n is the number of nodes in the linked list.