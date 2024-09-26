import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.h = [1]
        self.popped = set()

    def popSmallest(self) -> int:    
        val = heapq.heappop(self.h)
        self.popped.add(val)
        
        if len(self.h) == 0:
            heapq.heappush(self.h, val + 1)
        else:
            next = val + 1
            while(next  < self.h[0]):
                if next not in self.popped:
                    heapq.heappush(self.h, next)
                    break
                else:
                    next += 1

        
        return val
        

    def addBack(self, num: int) -> None:
        if num in self.popped:
            heapq.heappush(self.h, num)
            self.popped.remove(num)
