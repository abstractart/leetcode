class Solution:
    def isPalindrome(self, s: str) -> bool:
        finish = len(s) - 1
        start = 0
        
        while(start < finish):
            if not self.isValid(s[start]):
                start += 1
                continue
            if not self.isValid(s[finish]):
                finish -= 1
                continue
                
            if not self.lettersEqual(s[start], s[finish]): return False
            
            start += 1
            finish -= 1
        
        return True
            
    def isLetter(self, c):
        code = ord(c)
        return (code >= 97 and code <= 122) or (code >= 65 and code <= 90)
    
    def isNumber(self, c):
        code = ord(c)
        return (code >= 48 and code <= 57)
    
    def isValid(self, c):
        return self.isNumber(c) or self.isLetter(c)
    
    def lettersEqual(self, c1, c2):        
        if c1 == c2: return True
        if (self.isLetter(c1) and self.isLetter(c2)):
            return abs(ord(c1) - ord(c2)) == 32
        
        return False
        
        
