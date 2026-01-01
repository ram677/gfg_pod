#Palindrome Linked List

class Solution:
    def isPalindrome(self, head):
        # Base case: An empty list or single node is a palindrome
        if not head or not head.next:
            return True

        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 'slow' is now at the middle of the list.
        
        # Step 2: Reverse the second half of the list starting from 'slow'
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # 'prev' is now the head of the reversed second half.
        
        # Step 3: Compare the first half and the reversed second half
        left = head
        right = prev
        
        while right: # We only need to check until the end of the reversed half
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
            
        return True
    
# Time Complexity: O(N), where N is the number of nodes in the linked list.
# Space Complexity: O(1).