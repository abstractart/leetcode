class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        
        for s in strs:
            k = "".join((sorted(s)))
            
            if k not in d: d[k] = []
            
            d[k].append(s)
        
        return d.values()
        
