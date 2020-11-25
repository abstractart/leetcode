class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
            
        middle = len(lists) // 2
        return self.merge(
            self.mergeKLists(lists[0:middle]),
            self.mergeKLists(lists[middle:len(lists)])
        )
            
    
    def merge(self, i1, i2):
        head = tail = ListNode(0)

        while(i1 and i2):
            if i1.val <= i2.val:
                node = ListNode(i1.val)
                i1 = i1.next
            else:
                node = ListNode(i2.val)                
                i2 = i2.next
                
            tail.next = node
            tail = tail.next
        
        i = i1 or i2
        tail.next = i
        
        return head.next
