class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        if not head.next: return head
        
        if head.val == head.next.val:
            return self.deleteDuplicates(head.next)
        
        head.next = self.deleteDuplicates(head.next)
        
        return head
