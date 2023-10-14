class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return [".".join(reversed(r)) for r in self.helper(s, 4, 0, len(s))]
        
    def helper(self, s, segments, start, stop):
        if segments == 1:
            if self.isValid(s, start, stop):
                return [[s[start:stop]]]
            return []
        else:
            result = []
            
            for i in range(1, 4):                
                if self.isValid(s, start, start + i):
                    children = self.helper(s, segments - 1, start + i, stop)
                    if children:
                        segment = s[start:start + i]
                        for r in children:
                            r.append(segment)
                            result.append(r)
                        
            return result
        
    
    def isValid(self, s, start, stop):
        if start not in range(len(s)) or stop > len(s):
            return False
        
        l = stop - start
        if l < 1 or l > 3:
            return False

        if l > 1 and s[start] == "0":
            return False
        
        if l == 3:
            if s[start] > "2":
                return False
            if s[start] == "2" and s[start + 1] > "5":
                return False
            if s[start] == "2" and s[start + 1] == "5" and s[start + 2] > "5":
                return False

        return True
