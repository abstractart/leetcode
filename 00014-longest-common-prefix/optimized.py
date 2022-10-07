class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        if len(strs) == 0: return ""
        
        result = []
        
        for i, c in enumerate(strs[0]):
            for s in strs:
                if i < len(s) and s[i] == c:
                    continue
                
                return "".join(result)

            result.append(c)
        
        return "".join(result)
