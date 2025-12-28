#Swap Kth nodes from ends

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def swapKth(self, head, k):
        if not head:
            return head

        # Step 1: count length
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        # If k is more than length
        if k > n:
            return head

        # If swapping same node (middle element in odd length)
        if 2*k - 1 == n:
            return head

        # Step 2: find kth from beginning
        x_prev, x = None, head
        for i in range(1, k):
            x_prev = x
            x = x.next

        # Step 3: find kth from end (n-k+1 from start)
        y_prev, y = None, head
        for i in range(1, n-k+1):
            y_prev = y
            y = y.next

        # Step 4: swap previous links
        if x_prev:
            x_prev.next = y
        if y_prev:
            y_prev.next = x

        # Step 5: swap next pointers
        x.next, y.next = y.next, x.next

        # Step 6: update head if needed
        if k == 1:
            head = y
        if k == n:
            head = x

        return head

#Time Complexity: O(n)
#Space Complexity: O(1)
#Where n is the length of the linked list.