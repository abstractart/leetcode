class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tail = head
        curr1, curr2 = l1, l2
        
        while(curr1 and curr2):
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
                
            tail = tail.next
            tail.next = None
            
        tail.next = curr1 or curr2
        
        return head.next
