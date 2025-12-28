#Sort a linked list of 0s, 1s and 2s

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head

        # Create dummy heads for three lists
        head0 = Node(0)
        head1 = Node(0)
        head2 = Node(0)
        
        # Pointers to the tails of the three lists
        tail0 = head0
        tail1 = head1
        tail2 = head2
        
        current = head
        while current:
            if current.data == 0:
                tail0.next = current
                tail0 = current
            elif current.data == 1:
                tail1.next = current
                tail1 = current
            else: # current.data == 2
                tail2.next = current
                tail2 = current
            current = current.next
        
        # Connect the three lists
        # Connect 0s list to 1s list
        if head1.next:
            tail0.next = head1.next
        else:
            tail0.next = head2.next

        # Connect 1s list to 2s list
        if head2.next:
            tail1.next = head2.next
        else:
            tail1.next = None

        # Terminate the list
        tail2.next = None
        
        return head0.next

#Time complexity: O(n)
#Space complexity: O(1)
#Where n is the number of nodes in the linked list.