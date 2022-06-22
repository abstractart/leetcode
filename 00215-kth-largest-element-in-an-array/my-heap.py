from heapq import heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        
        for n in nums:
            if len(h) < k:
                heappush(h, n)
                continue
            
            minimum = heappop(h)
            if n > minimum:
                heappush(h, n)
            else:
                heappush(h, minimum)
        
        return heappop(h)
