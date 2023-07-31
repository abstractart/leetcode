from heapq import heappop, heappush

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []

        for i, l in enumerate(lists):
            if l:
                heappush(h, (l.val, i))
            
        r = ListNode()
        tail = r
        while(h):
            val, i = heappop(h)
            
            tail.next = lists[i]
            tail = tail.next

            if lists[i].next:
                heappush(h, (lists[i].next.val, i))
                
                lists[i] = lists[i].next

        
        return r.next
