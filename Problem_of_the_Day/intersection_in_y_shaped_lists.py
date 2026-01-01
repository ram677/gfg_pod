#Intersection in Y Shaped Lists

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def intersectPoint(self, head1, head2):
        # Helper to get the length of a linked list
        def get_length(head):
            length = 0
            curr = head
            while curr:
                length += 1
                curr = curr.next
            return length
            
        len1 = get_length(head1)
        len2 = get_length(head2)
        
        # Reset pointers to heads
        ptr1 = head1
        ptr2 = head2
        
        # Move the pointer of the longer list ahead by the difference in lengths
        diff = abs(len1 - len2)
        
        if len1 > len2:
            for _ in range(diff):
                ptr1 = ptr1.next
        else:
            for _ in range(diff):
                ptr2 = ptr2.next
                
        # Move both pointers until they collide
        while ptr1 and ptr2:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return None # Should not happen based on problem constraints
    
# Time Complexity: O(N + M), where N and M are the lengths of the two linked lists.
# Space Complexity: O(1).