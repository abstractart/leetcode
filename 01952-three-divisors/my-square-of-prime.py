from math import sqrt

class Solution:
    def isThree(self, n: int) -> bool:
        if n == 1:
            return False
        
        if not sqrt(n).is_integer():
            return False
        
        return self.isPrime(int(sqrt(n)))
            
            
    def isPrime(self, n):
        for i in range(2, n // 2):
            if n % i == 0: return False
            
        return True
