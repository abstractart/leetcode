class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = range(0, 1)
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    new = range(i, j + 1)
                    if len(r) < len(new):
                        r = new
        
        return s[r.start:r.stop]
        
        return s[r]
    def isPalindrome(self, s, i, j):        
        while(i < j):
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
