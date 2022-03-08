class Solution:
    def numDecodings(self, s: str) -> int:
        return self.helper(s, {})
    
    def helper(self, s, cache):
        if s in cache:
            return cache[s]
        
        if not len(s):
            cache[s] = 1
        elif s[0] == '0':
            cache[s] = 0
        elif len(s) == 1:
            cache[s] = 1
        else:
            cache[s] = self.helper(s[1:], cache)
            if int(s[0:2]) < 27:
                cache[s] += self.helper(s[2:], cache)
        
        return cache[s]
