class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        
        for i, e in enumerate(nums):            
            if target - e in h:
                return [i, h[target - e]]
            
            h[e] = i
