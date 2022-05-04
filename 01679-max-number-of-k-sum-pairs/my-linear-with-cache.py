class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cache = self.buildCache(nums)
        result = 0
        for left in nums:
            right = k - left
            if right in cache:
                if right == left:
                    result += len(cache[left]) // 2
                else: 
                    result += min(len(cache[left]), len(cache[right]))
                    cache[right] = []
                
                cache[left] = []

                
        return result
    
    
    def buildCache(self, nums):
        d = {}
        
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = set()
            
            d[n].add(i)
        
        return d
        
