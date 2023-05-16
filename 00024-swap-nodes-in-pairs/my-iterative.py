class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        resultTail = result
        
        while(head):
            nextHead = head.next
            
            if head.next:
                resultTail.next = head.next
                resultTail = resultTail.next
                
                nextHead = head.next.next
            
            resultTail.next = head
            resultTail = resultTail.next
            resultTail.next = None

            head = nextHead

        return result.next
