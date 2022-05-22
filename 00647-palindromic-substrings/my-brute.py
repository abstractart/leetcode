class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.brute(s)
    
    def brute(self, s):
        n = len(s)
        result = 0
        for i in range(n):
            for j in range(i, n):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    result += 1
        
        return result
