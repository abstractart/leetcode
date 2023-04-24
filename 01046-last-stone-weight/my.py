import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] *= -1

        heapq.heapify(stones)
        while(len(stones) > 1):
            l = heapq.heappop(stones)
            r = heapq.heappop(stones)

            if l != r:
                heapq.heappush(stones, l - r)                
        

        if not len(stones):
            return 0 

        return heapq.heappop(stones) * -1
