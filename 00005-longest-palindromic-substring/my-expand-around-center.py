class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        length = 1
        
        for i in range(len(s)):
            l1, r1 = self.fromMiddle(s, i, i)
            len1 = r1 - l1 + 1

            if len1 > length:
                left, right = l1, r1
                length = len1
                
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                continue
            
            l1, r1 = self.fromMiddle(s, i, i + 1)
            len1 = r1 - l1 + 1

            if len1 > length:
                left, right = l1, r1
                length = len1
        
        return s[left:right + 1]
            
        
    
    def fromMiddle(self, s, left, right):
        while(left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]):
            left -= 1
            right += 1
        
        return left, right
