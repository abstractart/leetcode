# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        size = 0
        links = dict()
        i = 0
        curr = head

        while(curr):
            links[i] = curr
            curr = curr.next
            
            size += 1
            i += 1
            
        if n == size: return head.next
            
        links[size - n - 1].next = links.get(size - n + 1)
        
        return head
        
