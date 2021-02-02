from math import factorial

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = dict()
        
        
        for i in range(len(nums)):
            n = nums[i]
            if n not in d: d[n] = []
                
            d[n].append(i)
            
        result = 0

        for k in d:
            if len(d[k]) >= 2:
                result += self.combinations(2, len(d[k]))
            
        
        return result


    def combinations(self, r, n):
        return factorial(n) // (factorial(r) * factorial(n - r))
