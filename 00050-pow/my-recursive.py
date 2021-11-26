class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.myPow(x, -n)
            
        if n == 0: return 1
        if n == 1: return x
        
        if n % 2 == 0:
            v = self.myPow(x, n // 2)
            
            return v * v
        else:
            v = self.myPow(x, (n - 1) // 2)
            return v * v * x
