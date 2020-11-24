class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        multiplier = 1
        
        for i in reversed(range(len(s))):
            result += (ord(s[i]) - 64) * multiplier
            multiplier *= 26
        
        return result
