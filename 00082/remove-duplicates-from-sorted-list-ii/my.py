class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        
        if head.val == head.next.val:
            tail = self.deleteDuplicates(head.next)
            
            if tail and tail.val == head.val:
                return tail.next
            return tail
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
