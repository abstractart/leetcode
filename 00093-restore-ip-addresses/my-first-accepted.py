class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = self.helper(s, 4)
        
        for r in result:
            r.reverse()
        
        return [".".join(r) for r in result]
        
    def helper(self, s, segments):
        if segments == 1:
            if self.isValid(s):
                return [[s]]
            return []
        else:
            result = []
            
            for i in range(1, 4):
                if self.isValid(s[0:i]):
                    for r in self.helper(s[i:], segments - 1):
                        r.append(s[0:i])
                        result.append(r)
                        
            return result
        
    
    def isValid(self, s):
        if len(s) not in range(1, 4):
            return False
        
        if len(s) > 1 and s[0] == "0":
            return False
        
        if len(s) == 3 and int(s) > 255:
            return False

        return True
