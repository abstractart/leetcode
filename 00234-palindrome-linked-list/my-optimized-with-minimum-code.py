class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:        
        slow, fast = head, head
        
        while(slow and fast and fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        slow.next = self.reverse(slow.next)
        
        left, right = head, slow.next
        while(right):
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True

    def reverse(self, head):
        acc = None
        
        while(head):
            newHead = head.next
            
            head.next = acc
            acc = head
            
            head = newHead
        
        return acc  
