from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        
        heap = []
        for n, count in c.items():
            heapq.heappush(heap, (-count, n))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result
