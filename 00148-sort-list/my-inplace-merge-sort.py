class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return head
        if head and not head.next: return head
        
        node = self.split(head)
        return self.merge(
            self.sortList(head),
            self.sortList(node)
        )
        
        
    
    def merge(self, l1, l2):
        curr1, curr2 = l1, l2
        head = ListNode(0)
        tail = head
        
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
    
    def split(self, head):
        slow = head
        fast = head.next
        prev = None
        while(fast):
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next
        
        prev.next = None
        return slow
