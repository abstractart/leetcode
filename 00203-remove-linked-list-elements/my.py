class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head = ListNode(0, head)
        curr = head
        
        while(curr and curr.next):
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head.next
