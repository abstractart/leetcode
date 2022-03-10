class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        tail = head
        r = 0
        
        while(l1 and l2):
            v = (l1.val + l2.val) + r
            
            l1.val = v % 10
            r = v // 10
            
            tail.next = l1
            tail = tail.next
            
            l1 = l1.next
            l2 = l2.next
            
        tmp = l1 or l2
        while(tmp and r):
            v = (tmp.val) + r

            tmp.val = v % 10
            r = v // 10

            tail.next = tmp
            tail = tail.next
            
            tmp = tmp.next
        
        if tmp:
            tail.next = tmp
        if r:
            tail.next = ListNode(r)
        
        return head.next
