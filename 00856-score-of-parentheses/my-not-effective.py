class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s) <= 2: return 1
        indexes = self.split(s)
        
        
        result = 0
        for substring in indexes:
            if substring[1] - substring[0] == 1:
                result += 1
            else:
                start = substring[0] + 1
                finish = substring[1]
                result += self.scoreOfParentheses(s[start:finish]) * 2
        
        return result
    
    def split(self, s):
        if not s: return []

        level = 0        
        start = 0
        
        indexes = []
        for i in range(len(s)):
            if s[i] == "(":
                level += 1
            else:
                level -= 1
        
            if level == 0:
                indexes.append((start, i))
                start = i + 1
        return indexes
        
        
