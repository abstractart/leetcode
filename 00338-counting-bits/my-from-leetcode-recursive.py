class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)  
        for i in range(1, n + 1):
            result[i] = self.helper(i)
            
        return result
    
    def helper(self, n):
        if n <= 1:
            return n
        if n % 2 == 1:  
            return self.helper((n - 1) // 2) + 1
        
        return self.helper(n // 2)
