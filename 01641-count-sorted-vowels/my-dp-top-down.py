class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.helper(5, n, {})
    
    
    def helper(self, k, n, acc):
        if n == 1 or k == 1:
            return k
        
        if (n, k) in acc:
            return acc[(n, k)]
        
        result = 0
        for i in range(1, k + 1):
            result += self.helper(i, n - 1, acc)
        
        acc[(n, k)] = result
        return acc[(n, k)]
