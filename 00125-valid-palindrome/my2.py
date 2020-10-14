class Solution(object):
    def isPalindrome(self, s):
        buffer = []
        
        for c in s.lower():
            if self.isValid(c): buffer.append(c)
        
        return self.isListPalindrome(buffer)
    
    def isLetter(self, c):
        return ord(c) in range(97, 123)
    
    def isNumber(self, c):
        return ord(c) in range(48, 58)
    
    def isValid(self, c):
        return self.isNumber(c) or self.isLetter(c)
    
    def isListPalindrome(self, l):
        cp = l.copy()
        cp.reverse()
        
        return l == cp
