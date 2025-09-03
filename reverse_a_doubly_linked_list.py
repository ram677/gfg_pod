#Reverse a Doubly Linked List

"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head

        curr = head
        prev_node = None

        while curr:
            # Swap next and prev
            curr.prev, curr.next = curr.next, curr.prev
            prev_node = curr
            # Move to the next node (which is prev after swap)
            curr = curr.prev

        # prev_node is the new head
        return prev_node

#Time Complexity: O(n)
#Space Complexity: O(1)
#Where n is the number of nodes in the doubly linked list.