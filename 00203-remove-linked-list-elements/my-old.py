class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        prev = None
        
        while(curr):
            if curr.val == val: 
                if curr == head:
                    head = head.next
                    curr = head
                else:
                    prev.next = curr.next
                    curr = prev.next
            else:
                prev = curr
                curr = curr.next
        
        return head
