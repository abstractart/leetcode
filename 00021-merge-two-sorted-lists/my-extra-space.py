class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tail = head
        
        while(l1 and l2):
            if l1.val > l2.val:
                node = ListNode(l2.val)
                l2 = l2.next
            else:
                node = ListNode(l1.val)
                l1 = l1.next
            
            tail.next = node
            tail = tail.next
            
        tail.next = l1 or l2
        
        return head.next
