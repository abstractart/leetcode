class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return head
        if not head.next: return head
        
        first = head
        second = head.next
        
        tail = second.next
                
        second.next = first
        first.next = self.swapPairs(tail)
        
        return second
