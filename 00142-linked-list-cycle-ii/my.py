class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        
        cycle = False
        while(slow and fast):
            slow = slow.next
            
            if fast.next:
                fast = fast.next.next
            else:
                break
    
            if fast == slow:
                cycle = True
                break
        
        if not cycle: return None
        while(head != fast):
            fast = fast.next
            head = head.next
            
        return fast
