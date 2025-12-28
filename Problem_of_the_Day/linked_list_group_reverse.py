#Linked List Group Reverse

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        # Base case
        if not head or k == 1:
            return head

        # Step 1: Count nodes to check if there are at least k nodes
        current = head
        count = 0
        while current and count < k:
            current = current.next
            count += 1
        
        # Check if there's a full group of k nodes
        if count == k:
            # Step 2: Reverse the first k nodes
            prev = None
            curr = head
            i = 0
            while curr and i < k:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                i += 1
            
            # Step 3: Recursively reverse the rest and connect
            head.next = self.reverseKGroup(curr, k)
            
            # Step 4: Return the new head of this reversed group
            return prev
        
        else:
            # If less than k nodes are left, reverse them too (per the problem statement)
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

#Time complexity: O(n)
#Space complexity: O(n/k)
#Where n is the number of nodes in the linked list and k is the group size.