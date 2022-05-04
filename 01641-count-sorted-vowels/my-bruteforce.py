class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.helper(5, n)
    
    
    def helper(self, k, n):
        if n == 1:
            return k
        
        if k == 1:
            return 1
        
        result = 0
        
        for i in range(1, k + 1):
            result += self.helper(i, n - 1)
            
        return result
