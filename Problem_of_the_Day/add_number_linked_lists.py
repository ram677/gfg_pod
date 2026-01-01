#Add Number Linked Lists

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    # Helper function to reverse a linked list
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addTwoLists(self, head1, head2):
        # 1. Reverse both lists to align LSBs (Least Significant Bits)
        l1 = self.reverse(head1)
        l2 = self.reverse(head2)
        
        dummy = Node(0)
        curr = dummy
        carry = 0
        
        # 2. Perform addition
        while l1 or l2 or carry:
            val1 = l1.data if l1 else 0
            val2 = l2.data if l2 else 0
            
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            
            curr.next = Node(digit)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # 3. Reverse the result to restore MSB at head
        result = self.reverse(dummy.next)
        
        # 4. Remove leading zeros from the output
        # Example: if result is 0->0->6->3, move head to 6.
        # Check 'result.next' to ensure we don't remove the single '0' if the sum is 0.
        while result and result.data == 0 and result.next:
            result = result.next
            
        return result
    
# Time Complexity: O(max(N, M)) where N and M are the lengths of the two linked lists.
# Space Complexity: O(1) if we don't count the output list, otherwise O(max(N, M)) for the output list.