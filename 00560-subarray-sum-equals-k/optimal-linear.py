class Solution:
    def subarraySum(self, nums, k: int) -> int:
        d = {}
        acc = 0
        
        count = 0
        for num in nums:
            acc += num
            
            if acc == k:
                count += 1
            if acc - k in d:
                count += d[acc - k]
            if acc not in d:
                d[acc] = 1
            else:
                d[acc] += 1
            
        
        return count
