class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.helper(5, n)
    
    
    def helper(self, k, n):
        if n == 1 or k == 1:
            return k
        
        return self.helper(k - 1, n) + self.helper(k, n - 1)
