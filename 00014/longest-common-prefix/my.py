class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        if len(strs) == 0: return ""
        
        result = []
        
        for i in range(min(map(len, strs))):
            chars = []
            
            for s in strs:
                chars.append(s[i])
            
            if len(set(chars)) > 1: break
            
            result.append(strs[0][i])
            
        
        return "".join(result)
