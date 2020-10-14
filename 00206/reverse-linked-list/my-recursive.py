class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseListRec(head, None)
    
    def reverseListRec(self, source, target):
        if not source: return target
        
        node = source
        source = source.next

        node.next = target
        target = node
        
        return self.reverseListRec(source, target)
        
