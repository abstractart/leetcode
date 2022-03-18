class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        
        curr = head
        while(curr):
            newCurr = curr.next
            curr.next = None
            stack.append(curr)
            curr = newCurr
            
        result = ListNode(0)
        tail = result
        i, j = 0, len(stack) - 1
        while(i <= j):
            if i == j:
                tail.next = stack[i]
                tail = tail.next
            else:
                tail.next = stack[i]
                tail = tail.next
                
                tail.next = stack[j]
                tail = tail.next
            
            i += 1
            j -= 1
            
        return result.next
