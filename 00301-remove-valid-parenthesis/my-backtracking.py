class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        return self.helper(set([s]))
    
    def helper(self, strs):
        if len(strs) == 0: return []
        
        valid = []
        invalid = set()
        
        for s in strs:
            if self.isValid(s):
                valid.append(s)
            else:
                v = self.variants(s)
                invalid.update(v)
        
        
        if len(valid) > 0: return valid
        return self.helper(invalid)
        
        
    def variants(self, s):
        result = set()
        
        for i in range(len(s)):
            result.add(s[:i] + s[i + 1:])
    
        return result
    
    
    def isValid(self, s):
        curr = 0
        
        for c in s:
            if c == "(": curr += 1
            if c == ")": curr -= 1
            
            if curr < 0: return False
        
        return curr == 0
