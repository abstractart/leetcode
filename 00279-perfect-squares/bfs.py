from queue import Queue
from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:
        q = Queue()
        q.put((n, 0))
        
        while(q.qsize() > 0):
            n, squares = q.get()
            if n == 0: return squares
            if self.isSquare(n): return squares + 1
            
            for i in reversed(range(1, int(sqrt(n)) + 1)):
                q.put((n - i * i, squares + 1))
    
    def isSquare(self, n):
        return int(sqrt(n)) ** 2 == n
