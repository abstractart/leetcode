class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = dict()
        
        for i in range(len(s)):
            d[indices[i]] = s[i]
            
            
        result = []
        for i in range(len(s)):
            result.append(d[i])
            
        return "".join(result)
