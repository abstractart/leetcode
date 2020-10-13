class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_index = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in value_index:
                return [i, value_index.get(complement)]
            
            value_index[nums[i]] = i
        
