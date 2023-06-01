import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k

        for n in nums:
            self.add(n)


    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        
        return self.h[0]
