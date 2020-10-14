class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        
        slow = head
        fast = slow
        
        while(slow and fast and fast.next):
            if fast.next == slow: return True
            
            fast = fast.next.next
            slow = slow.next
            
        return False
