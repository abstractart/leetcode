# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = self.length(head)
        if l - n == 0: return head.next

        node = self.findNthNode(head, l - n)
        node.next = node.next.next

        
        return head
        
    
    def findNthNode(self, head, n):
        if n == 1: return head
        if not head: return head
        
        return self.findNthNode(head.next, n - 1)
    
    
    def length(self, head):
        r = 0
        
        while(head):
            r += 1
            head = head.next
    
        return r
