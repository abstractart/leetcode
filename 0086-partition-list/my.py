class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:        
        leftHead = ListNode(0)
        leftTail = leftHead
        
        rightHead = ListNode(0)
        rightTail = rightHead
        
        
        curr = head
        while(curr):
            if curr.val < x:
                leftTail.next = curr
                leftTail = leftTail.next
            else:
                rightTail.next = curr
                rightTail = rightTail.next
            
            curr = curr.next
        
        rightTail.next = None
        leftTail.next = rightHead.next
        
        return leftHead.next
