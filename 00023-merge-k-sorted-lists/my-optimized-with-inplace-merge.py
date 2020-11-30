from queue import SimpleQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0: return None
        
        q = SimpleQueue()
        for l in lists:
            q.put(l)

        
        while(q.qsize() > 1):                    
            q.put(self.merge(q.get(), q.get()))
            
        return q.get()
    
    
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
