from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = [None] * (len(nums) + 1)
        
        counts = Counter(nums)
        
        for n, count in counts.items():
            if r[count] is None:
                r[count] = []
                
            r[count].append(n)
        
        result = []
        
        while(len(result) < k):
            while(r[-1] is None):
                r.pop()
            
            result.extend(r.pop())
        
        return result
