class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = dict()
        
        for i in range(len(nums)):            
            if target - nums[i] in value_index:
                return [i, value_index.get(target - nums[i])]
            
            value_index[nums[i]] = i
        
