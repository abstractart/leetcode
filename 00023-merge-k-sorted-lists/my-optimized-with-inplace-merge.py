class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        
        while(len(lists) > 1):                    
            lists.insert(0, (self.merge(lists.pop(), lists.pop())))
            
        return lists[0]
    
    
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
