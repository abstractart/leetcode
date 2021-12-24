class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
    
    
    def reverse(self, head, newHead):
        if head is None:
            return newHead
        
        tmp = head.next
        head.next = newHead
        newHead = head
        
        return self.reverse(tmp, newHead)
