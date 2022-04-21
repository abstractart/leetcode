class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ranges = self.splitArray(nums)
        
        result = nums[0]
        for r in ranges:
            left = self.product(nums, r[0], r[1])
            right = self.product(nums, r[1] - 1, r[0] - 1)
            
            v = max(
                max(left),
                max(right)
            )
            
            result = max(result, v)
        
        return max(max(nums), result)
            
            
            
    def product(self, nums, start, finish):        
        step = 1
        if start > finish:
            step = -1
        
        multiplier = 1
        result = []
        for i in range(start, finish, step):
            n = nums[i]
            result.append(n * multiplier)
            multiplier = result[-1]
        
        return result
    
    def splitArray(self, nums):
        start = 0
        ranges = []
        while(start < len(nums)):
            if nums[start] == 0:
                start += 1
                continue
            
            finish = start
            while(finish < len(nums) and nums[finish] != 0):
                finish += 1
            
            
            ranges.append((start, finish))
            start = finish
        return ranges    
