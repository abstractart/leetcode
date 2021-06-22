class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        index = self.buildIndex(s)
        result = 0
        
        for w in words:
            if self.match(index, w): result += 1

        return result
    
    
    def buildIndex(self, s):
        index = {}
        
        for i, c in enumerate(s):
            if c not in index: index[c] = []
            
            index[c].append(i)
            
        
        return index
    
    
    def match(self, index, w):
        last = -1
    
        for c in w:
            if c not in index: return False
            
            newLast = last
            for i in index[c]:
                if i > newLast:
                    newLast = i
                    break
                
            if newLast == last:
                return False
            else:
                last = newLast
            
        return last != -1
