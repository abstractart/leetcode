from bisect import bisect_left as bsearch

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        
        middle = bsearch(nums, 0)
        n = middle - 1
        p = middle
        
        negative = range(0, p)
        positive = range(p, len(nums))
        while(n in negative and p in positive):
            if nums[n] * nums[n] >= nums[p] * nums[p]:
                result.append(nums[p] * nums[p])
                p += 1 
            else:
                result.append(nums[n] * nums[n])
                n -= 1
        
        while(n in negative):
            result.append(nums[n] * nums[n])
            n -= 1
        
        while(p in positive):
            result.append(nums[p] * nums[p])
            p += 1
        
        return result
