from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        
        heap = []
        for n, count in c.items():
            heapq.heappush(heap, (count, n))
            
            if len(heap) > k:
                heapq.heappop(heap)

        return [n[1] for n in heap]
