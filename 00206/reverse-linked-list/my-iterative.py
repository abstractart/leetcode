class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        
        while(head):
            newHead = head.next
            
            head.next = reverse
            reverse = head
            
            head = newHead
        
        return reverse
